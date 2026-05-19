# nix/packages.nix — Quill Agent package built with uv2nix
{ inputs, ... }:
{
  perSystem =
    { pkgs, inputs', ... }:
    let
      quillAgent = pkgs.callPackage ./quill-agent.nix {
        inherit (inputs) uv2nix pyproject-nix pyproject-build-systems;
        npm-lockfile-fix = inputs'.npm-lockfile-fix.packages.default;
        # Only embed clean revs — dirtyRev doesn't represent any upstream
        # commit, so comparing it would always claim "update available".
        rev = inputs.self.rev or null;
      };
    in
    {
      packages = {
        default = quillAgent;
        tui = quillAgent.quillTui;
        web = quillAgent.quillWeb;

        fix-lockfiles = quillAgent.quillNpmLib.mkFixLockfiles {
          packages = [ quillAgent.quillTui quillAgent.quillWeb ];
        };
      };
    };
}
