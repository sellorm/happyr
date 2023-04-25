# happyr - "fitR, happyR"

Brings R's {styler} and {lintr} packages to the command line.

Make your R code fitR and happyR with the happyR cli tool.


## Installation

Install from PyPI:

```bash
# python3 -m pip install happyr
```


## Usage

```bash
happyr --help
```

```output
usage: happyr [-h] [-v] [-c CRAN] [-R RPATH] [-l LIBRARY] {style,lint} ...

A CLI for R's {styler} and {lintr} packages

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CRAN, --cran CRAN  CRAN mirror to use [default: `getOption('repos')`]
  -R RPATH, --rpath RPATH
                        path to your R installation [default: $PATH]
  -l LIBRARY, --library LIBRARY
                        path to the R library to use [default: `.libPaths()`]

Commands:
  {style,lint}
    style               Users {styler} to style your code
    lint                lists installed packages

For more information please see the docs
```

To style with {styler}:

```bash
happyr style --help
```

```output
usage: happyr style [-h] [-p PACKAGE | -f FILE | -d DIR]

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGE, --package PACKAGE
                        styles a package at the supplied path
  -f FILE, --file FILE  styles a file at the supplied path
  -d DIR, --dir DIR     styles a directory at the supplied path
```

To lint with {lintr}:

```bash
happyr lint --help
```

```output
usage: happyr lint [-h] [-p PACKAGE | -f FILE | -d DIR]

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGE, --package PACKAGE
                        lints a package at the supplied path
  -f FILE, --file FILE  lints a file at the supplied path
  -d DIR, --dir DIR     lints a directory at the supplied path
```



## License

MIT (c) Mark Sellors

