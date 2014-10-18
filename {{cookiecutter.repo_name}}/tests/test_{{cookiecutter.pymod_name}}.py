#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.pymod_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

import unittest

from {{ cookiecutter.pymod_name }} import {{ cookiecutter.pymod_name }}


class Test{{ cookiecutter.pymod_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
