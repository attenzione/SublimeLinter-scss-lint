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

import logging
import re
from SublimeLinter.lint import RubyLinter

logger = logging.getLogger('SublimeLinter.plugin.scsslint')

RULE_RE = r'^(\w+)'

class ScssLint(RubyLinter):

    """Provides an interface to the scss-lint executable."""

    cmd = ('ruby', '-S', 'scss-lint', '${args}', '${file}')
    regex = r'^.+?:(?P<line>\d+)(?::(?P<col>\d+))? (?:(?P<error>\[E\])|(?P<warning>\[W\])) (?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    word_re = r'[^\s]+[\w]'
    defaults = {
        'selector': 'source.css - meta.attribute-with-value, source.sass, source.scss'
    }

    def reposition_match(self, line, col, m, vv):
      if col != None and m.near:
        text = vv.select_line(m.line)
        near = self.strip_quotes(m.near)
        rule_match = re.search(RULE_RE, m.message)
        rule_name = rule_match.group() if rule_match else None

        # PseudoElement rule return incorrect 'near' string
        if rule_name == 'PseudoElement':
          # return the same when 'near' is None
          # linter.py:978
          match = self.word_re.search(text) if self.word_re else None
          if match:
            start = match.start()
            length = len(match.group())
          else:
            start = 1
            length = len(text) - 1
          return line, start, start + length

        # SelectorFormat return column 1, which is incorrect
        elif rule_name == 'SelectorFormat':
          real_col = text.find(near)
          if real_col >= 0 and real_col != col:
            return super().reposition_match(line, real_col, m, vv)

      return super().reposition_match(line, col, m, vv)
