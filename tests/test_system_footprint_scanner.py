#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_system_footprint_scanner
----------------------------------

Tests for `system_footprint_scanner` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from system_footprint_scanner import system_footprint_scanner
from system_footprint_scanner import cli



class TestSystem_footprint_scanner(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'system_footprint_scanner.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
