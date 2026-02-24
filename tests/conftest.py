# tests/conftest.py
"""Test configuration for the Todo API project.

Ensures that the repository root is added to ``sys.path`` so that the
``app`` package can be imported reliably when the test suite is executed via
``pytest``.
"""
import sys
import os

# Add the project root (one level up from the tests directory) to the import path.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
