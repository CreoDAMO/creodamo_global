{pkgs}: {
  deps = [
    pkgs.glibc
    pkgs.glibcLocales
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.glibcLocales
    ];
  };
}
