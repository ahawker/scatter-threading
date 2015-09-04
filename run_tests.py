#!/usr/bin/env python
"""
    run_tests.py
    ~~~~~~~~~~~~

    Entry point for running Scatter test suite.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

import os
import sys


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    sys.path.insert(0, os.path.abspath(os.path.join('..', 'scatter')))
    sys.path.insert(0, os.path.abspath(os.path.join('..', 'scatter-async')))

    import unittest
    unittest.main()
    #from scatter.tests import main
    #main()
