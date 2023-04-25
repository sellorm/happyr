"""
happyr
"""

import argparse
from typing import Optional, Sequence
from happyr.version import __version__
from happyr.cliactions import do_style, do_lint


def arg_parser(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """
    Parses cli arguments for the command cli tool
    """
    parser = argparse.ArgumentParser(
        prog="happyr",
        description="A CLI for R's {styler} and {lintr} packages",
        epilog="For more information please see the docs",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-c",
        "--cran",
        help="CRAN mirror to use [default: `getOption('repos')`]",
    )
    parser.add_argument(
        "-R",
        "--rpath",
        help="path to your R installation [default: $PATH]",
    )
    parser.add_argument(
        "-l",
        "--library",
        help="path to the R library to use [default: `.libPaths()`]",
    )
    subparser = parser.add_subparsers(title="Commands", dest="subcmd")
    cmd_style = subparser.add_parser("style", help="Users {styler} to style your code")
    cmd_style.set_defaults(func=do_style)
    cmd_style_group = cmd_style.add_mutually_exclusive_group()
    cmd_style_group.add_argument(
        "-p",
        "--package",
        help="styles a package at the supplied path",
    )
    cmd_style_group.add_argument(
        "-f",
        "--file",
        help="styles a file at the supplied path",
    )
    cmd_style_group.add_argument(
        "-d",
        "--dir",
        help="styles a directory at the supplied path",
    )
    cmd_lint = subparser.add_parser("lint", help="lists installed packages")
    cmd_lint.set_defaults(func=do_lint)
    cmd_lint_group = cmd_lint.add_mutually_exclusive_group()
    cmd_lint_group.add_argument(
        "-p",
        "--package",
        help="lints a package at the supplied path",
    )
    cmd_lint_group.add_argument(
        "-f",
        "--file",
        help="lints a file at the supplied path",
    )
    cmd_lint_group.add_argument(
        "-d",
        "--dir",
        help="lints a directory at the supplied path",
    )
    return parser.parse_args(args)
