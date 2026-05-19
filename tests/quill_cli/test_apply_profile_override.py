"""Regression tests for _apply_profile_override QUILL_HOME guard (issue #22502).

When QUILL_HOME is set to the quill root (e.g. systemd hardcodes
QUILL_HOME=/root/.quill), _apply_profile_override must still read
active_profile and update QUILL_HOME to the profile directory.

When QUILL_HOME is already a profile directory (.../profiles/<name>),
_apply_profile_override must trust it and return without re-reading
active_profile (child-process inheritance contract).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest


def _run_apply_profile_override(
    tmp_path, monkeypatch, *, quill_home: str | None, active_profile: str | None,
    argv: list[str] | None = None,
):
    """Run _apply_profile_override in isolation.

    Returns the value of os.environ["QUILL_HOME"] after the call,
    or None if unset.
    """
    quill_root = tmp_path / ".quill"
    quill_root.mkdir(parents=True, exist_ok=True)

    if active_profile is not None:
        (quill_root / "active_profile").write_text(active_profile)

    if active_profile and active_profile != "default":
        (quill_root / "profiles" / active_profile).mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    if quill_home is not None:
        monkeypatch.setenv("QUILL_HOME", quill_home)
    else:
        monkeypatch.delenv("QUILL_HOME", raising=False)

    monkeypatch.setattr(sys, "argv", argv or ["quill", "gateway", "start"])

    from quill_cli.main import _apply_profile_override
    _apply_profile_override()

    return os.environ.get("QUILL_HOME")


class TestApplyProfileOverrideQuillHomeGuard:
    """Regression guard for issue #22502.

    Verifies that QUILL_HOME pointing to the quill root does NOT suppress
    the active_profile check, while QUILL_HOME already pointing to a
    profile directory IS trusted as-is.
    """

    def test_quill_home_at_root_with_active_profile_is_redirected(
        self, tmp_path, monkeypatch
    ):
        """QUILL_HOME=/root/.quill + active_profile=coder must redirect
        QUILL_HOME to .../profiles/coder.

        Bug scenario from #22502: systemd sets QUILL_HOME to the quill root
        and the user switches to a profile via `quill profile use`.
        Before the fix, the guard returned early and active_profile was ignored.
        """
        quill_root = tmp_path / ".quill"
        quill_root.mkdir(parents=True, exist_ok=True)

        result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            quill_home=str(quill_root),
            active_profile="coder",
        )

        assert result is not None, "QUILL_HOME must be set after profile redirect"
        assert "profiles" in result, (
            f"Expected QUILL_HOME to point into profiles/ dir, got: {result!r}"
        )
        assert result.endswith("coder"), (
            f"Expected QUILL_HOME to end with 'coder', got: {result!r}"
        )

    def test_quill_home_already_profile_dir_is_trusted(self, tmp_path, monkeypatch):
        """QUILL_HOME=.../profiles/coder must not be overridden even when
        active_profile says something different.

        Preserves the child-process inheritance contract: a subprocess spawned
        with QUILL_HOME already set to a specific profile must stay in that
        profile.
        """
        quill_root = tmp_path / ".quill"
        profile_dir = quill_root / "profiles" / "coder"
        profile_dir.mkdir(parents=True, exist_ok=True)

        (quill_root / "active_profile").write_text("other")

        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("QUILL_HOME", str(profile_dir))
        monkeypatch.setattr(sys, "argv", ["quill", "gateway", "start"])

        from quill_cli.main import _apply_profile_override
        _apply_profile_override()

        assert os.environ.get("QUILL_HOME") == str(profile_dir), (
            "QUILL_HOME must remain unchanged when already pointing to a profile dir"
        )

    def test_quill_home_unset_reads_active_profile(self, tmp_path, monkeypatch):
        """Classic case: QUILL_HOME unset + active_profile=coder must set
        QUILL_HOME to the profile directory (existing behaviour must not regress).
        """
        result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            quill_home=None,
            active_profile="coder",
        )

        assert result is not None
        assert "coder" in result

    def test_quill_home_unset_default_profile_no_redirect(self, tmp_path, monkeypatch):
        """active_profile=default must not redirect QUILL_HOME."""
        quill_root = tmp_path / ".quill"
        quill_root.mkdir(parents=True, exist_ok=True)

        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("QUILL_HOME", raising=False)
        monkeypatch.setattr(sys, "argv", ["quill", "gateway", "start"])
        (quill_root / "active_profile").write_text("default")

        from quill_cli.main import _apply_profile_override
        _apply_profile_override()

        assert os.environ.get("QUILL_HOME") is None
# quill: tests
