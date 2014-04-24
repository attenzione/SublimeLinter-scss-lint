#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sergey Margaritov
# Copyright (c) 2013 Sergey Margaritov
#
# License: MIT
#

"""This module exports the scss-lint plugin linter class."""

import os
from SublimeLinter.lint import Linter, util


class Scss(Linter):

    """Provides an interface to the scss-lint executable."""

    syntax = ['sass', 'scss']
    executable = 'scss-lint'
    regex = r'^.+?:(?P<line>\d+) (?:(?P<error>\[E\])|(?P<warning>\[W\])) (?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    tempfile_suffix = 'scss'
    defaults = {
        '--include-linter:,': '',
        '--exclude-linter:,': ''
    }
    inline_overrides = ('bundle-exec', 'include-linter', 'exclude-linter')
    comment_re = r'^\s*/[/\*]'
    config_file = ('--config', '.scss-lint.yml', '~')

    def cmd(self):
        if self.get_view_settings().get('bundle-exec', False):
            return ['bundle', 'exec', self.executable]
        return [self.executable_path]