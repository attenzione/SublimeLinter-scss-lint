#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sergey Margaritov
# Copyright (c) 2013 Sergey Margaritov
#
# License: MIT
#

"""This module exports the JSHint plugin linter class."""

import os
from SublimeLinter.lint import Linter, util


class Scss(Linter):

    """Provides an interface to the scss-lint executable."""

    syntax = ('sass', 'scss')
    executable = 'scss-lint'
    regex = r'^.+?:(?P<line>\d+) (?:(?P<error>\[E\])|(?P<warning>\[W\])) (?P<message>.+)'
    # cmd = 'scss-lint'

    def cmd(self):
        """
        Return a string with the command line to execute.

        We define this method because we want to use the .scsslintrc files,
        and we can't rely on scss-lint to find them, because we are using stdin.
        """

        command = [self.executable_path]
        scsslintrc = util.find_file(os.path.dirname(self.filename), '.scss-lint.yml')

        if scsslintrc:
            command += ['--config', scsslintrc]

        return command + ['@']
