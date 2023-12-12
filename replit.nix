{ pkgs }: {
  deps = [
    pkgs.print(numpy.__version__)
  ];
}