# bazel-python-example

A small Python + pytest project, also buildable/testable with Bazel via
Bzlmod and `rules_python`. It has four small libraries, each with one or
more pytest test files.

## Layout

```
.
├── requirements.txt      # pip dependencies (pytest), used by both plain pip and Bazel's pip.parse
├── pytest.ini            # scopes plain `pytest` discovery to the source packages
├── MODULE.bazel          # Bzlmod module + rules_python/pip dependencies
├── .bazelrc              # build/test defaults
├── .bazelversion         # pins the Bazel version
├── tools/
│   └── pytest_main.py    # shared py_test entry point (see "How Bazel runs tests" below)
├── calculator/
│   ├── calculator.py
│   ├── calculator_test.py
│   ├── calculator_divide_test.py
│   ├── calculator_modes_test.py
│   ├── calculator_props_test.py
│   └── BUILD.bazel
├── stringutil/
│   ├── stringutil.py
│   ├── stringutil_test.py
│   ├── stringutil_palindrome_test.py
│   └── BUILD.bazel
├── mathutil/
│   ├── mathutil.py
│   ├── mathutil_test.py
│   ├── mathutil_prime_test.py
│   └── BUILD.bazel
└── listutil/
    ├── listutil.py
    ├── listutil_test.py
    ├── listutil_chunk_test.py
    └── BUILD.bazel
```

## Running the tests with plain pytest

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest
```

## Running the tests with Bazel

You need Bazel. The easiest way is [Bazelisk](https://github.com/bazelbuild/bazelisk),
which reads `.bazelversion` and downloads the right Bazel for you.

```sh
brew install bazelisk
```

Run every test in the project:

```sh
bazel test //...
```

Run the tests for a single target:

```sh
bazel test //calculator:calculator_test
bazel test //stringutil:stringutil_test
bazel test //mathutil:mathutil_test
bazel test //listutil:listutil_test
```

Build everything without running tests:

```sh
bazel build //...
```

### How Bazel runs tests

Bazel's `py_test` rule executes a single file directly (`python
calculator_test.py`), unlike the `pytest` CLI, which discovers and imports
test files itself. To bridge that gap without adding any Bazel-specific code
to the test files themselves, every `py_test` target points `main` at a
shared entry point, `//tools:pytest_main.py`, and passes its real test
file's path via `args`. The test files stay identical to the plain-pytest
version.
