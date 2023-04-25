"""
happyr main
"""

import sys
import happyr.cli


def main() -> None:
    """
    Kicks everything off for the cli tool
    """
    args = happyr.cli.arg_parser(sys.argv[1:])
    try:
        args.func(args)
    except AttributeError:
        happyr.cli.arg_parser(["-h"])
