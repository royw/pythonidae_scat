#!/usr/bin/env python3
# coding=utf-8
"""
This is the console entry point (from setup.py) for the Pythonidae Scat application.

"""
__docformat__ = 'restructuredtext en'

import os
import sys
from pprint import pformat


# noinspection PyDocstring
def hack_sys_path(debug=False):
    """
    When called the sys.path may contain this files directory when it really needs the
    parent directory (example, from repo root running "audrey2/audrey2.py"), then this
    directory.  So we need to remove this directory and this directory's parent where ever
    they are in the sys.path, then insert this directory's parent followed by this directory
    into the start of sys.path.

    ::

        Example file structure:

        * repo_root
        * repo_root/proj_package
        * repo_root/proj_package/main.py

        for the following to work:

        cd repo_root
        proj_package/main.py

        then sys.path needs to be:

            [repo_root, repo_root/proj_package, ...]

    .. note::

        Must be executed before importing any project specific packages

    """
    if debug:
        print("original sys.path: %s" % pformat(sys.path))
    this_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(this_dir)
    if debug:
        print("this_dir: %s" % this_dir)
        print("parent_dir: %s" % parent_dir)
    if this_dir in sys.path:
        sys.path.remove(this_dir)
    if parent_dir in sys.path:
        sys.path.remove(parent_dir)
    sys.path.insert(0, parent_dir)
    sys.path.insert(1, this_dir)
    if debug:
        print("adjusted sys.path: %s" % pformat(sys.path))


hack_sys_path()

from pythonidae_scat.pythonidae_scat_app import PythonidaeScatApp
from pythonidae_scat.pythonidae_scat_cli import PythonidaeScatCLI

__all__ = ('main',)


def main():
    """
    This is the console entry point.
    """

    cli = PythonidaeScatCLI()
    cli.execute(PythonidaeScatApp())


if __name__ == '__main__':
    main()
