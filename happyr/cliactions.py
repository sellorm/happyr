"""
happyr
"""

import os
import subprocess
from typing import Any
import happyr.helpers


def do_style(args: Any) -> None:
    """
    interface to the {styler} package
    """
    lib = happyr.helpers.set_lib(args.library)

    if args.package:
        r_cmd = f'styler::style_pkg(pkg="{args.package}", include_roxygen_examples = FALSE)'

    if args.file:
        r_cmd = f'styler::style_file(path="{args.file}", include_roxygen_examples = FALSE)'

    if args.dir:
        r_cmd = f'styler::style_dir(path="{args.dir}", include_roxygen_examples = FALSE)'
    
    r_binary = happyr.helpers.which_r(path=args.rpath, status=1)

    if os.environ["DEVMODE"] == "on":
        print(r_cmd)

    subprocess.run(
        [r_binary, "-s", "-e", r_cmd],
        check=False,
    )


def do_lint(args: Any) -> None:
    """
    Interface to R's {lintr} package
    """
    lib = happyr.helpers.set_lib(args.library)

    if args.package:
        r_cmd = f'lintr::lint_package(path="{args.package}")'

    if args.file:
        r_cmd = f'lintr::lint(filename="{args.file}")'

    if args.dir:
        r_cmd = f'lintr::lint_dir(path="{args.dir}")'
    
    r_binary = happyr.helpers.which_r(path=args.rpath, status=1)

    if os.environ["DEVMODE"] == "on":
        print(r_cmd)

    subprocess.run(
        [r_binary, "-s", "-e", r_cmd],
        check=False,
    )

