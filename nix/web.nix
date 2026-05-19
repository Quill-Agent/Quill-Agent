# nix/web.nix — Quill Web Dashboard (Vite/React) frontend build
{ pkgs, quillNpmLib, ... }:
let
  src = ../web;
  npmDeps = pkgs.fetchNpmDeps {
    inherit src;
    hash = "sha256-H98reD4N++WroZOQ9NFrKtC5aiHj6KqaYDzUOiZA2bE=";
  };

  npm = quillNpmLib.mkNpmPassthru { folder = "web"; attr = "web"; pname = "quill-web"; };

  packageJson = builtins.fromJSON (builtins.readFile (src + "/package.json"));
  version = packageJson.version;
in
pkgs.buildNpmPackage (npm // {
  pname = "quill-web";
  inherit src npmDeps version;

  doCheck = false;

  buildPhase = ''
    npx tsc -b
    npx vite build --outDir dist
  '';

  installPhase = ''
    runHook preInstall
    cp -r dist $out
    runHook postInstall
  '';
})
