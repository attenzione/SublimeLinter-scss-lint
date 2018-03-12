#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Sergey Margaritov
# Copyright (c) 2013 Sergey Margaritov
#
# License: MIT
#

"""This module exports the scss-lint plugin linter class."""

from SublimeLinter.lint import RubyLinter


class ScssLint(RubyLinter):

    """Provides an interface to the scss-lint executable."""

    syntax = ('css', 'sass', 'scss')
    cmd = ('ruby', '-S', 'scss-lint', '${args}', '${file}')
    regex = r'^.+?:(?P<line>\d+)(?::(?P<column>\d+))? (?:(?P<error>\[E\])|(?P<warning>\[W\])) (?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    defaults = {

    }
