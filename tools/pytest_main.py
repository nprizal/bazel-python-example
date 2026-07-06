"""Shared Bazel py_test entry point for running tests under pytest.

Bazel's py_test rule executes a single file directly, unlike the `pytest`
CLI which discovers and imports test files itself. Every py_test target
sets `main = "//tools:pytest_main.py"` and passes its real test file's
runfile path via `args = ["$(location :the_test.py)"]`, so the actual test
files stay plain, idiomatic pytest with no Bazel-specific code.
"""

import os
import sys

import pytest

if __name__ == "__main__":
    args = sys.argv[1:]
    xml_path = os.environ.get("XML_OUTPUT_FILE")
    if xml_path:
        args.append(f"--junitxml={xml_path}")
    sys.exit(pytest.main(args))
