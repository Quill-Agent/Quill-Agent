"""Resolve QUILL_HOME for standalone skill scripts.

Skill scripts may run outside the Quill process (e.g. system Python,
nix env, CI) where ``quill_constants`` is not importable.  This module
provides the same ``get_quill_home()`` and ``display_quill_home()``
contracts as ``quill_constants`` without requiring it on ``sys.path``.

When ``quill_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``quill_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``QUILL_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from quill_constants import display_quill_home as display_quill_home
    from quill_constants import get_quill_home as get_quill_home
except (ModuleNotFoundError, ImportError):

    def get_quill_home() -> Path:
        """Return the Quill home directory (default: ~/.quill).

        Mirrors ``quill_constants.get_quill_home()``."""
        val = os.environ.get("QUILL_HOME", "").strip()
        return Path(val) if val else Path.home() / ".quill"

    def display_quill_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``quill_constants.display_quill_home()``."""
        home = get_quill_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
