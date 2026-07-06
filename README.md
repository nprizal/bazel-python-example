# bazel-python-example

A small Python + pytest project. It has four small libraries, each with one
or more pytest test files.

## Layout

```
.
├── requirements.txt      # pip dependencies (pytest)
├── pytest.ini            # scopes pytest discovery to the source packages
├── calculator/
│   ├── calculator.py
│   ├── calculator_test.py
│   ├── calculator_divide_test.py
│   ├── calculator_modes_test.py
│   └── calculator_props_test.py
├── stringutil/
│   ├── stringutil.py
│   ├── stringutil_test.py
│   └── stringutil_palindrome_test.py
├── mathutil/
│   ├── mathutil.py
│   ├── mathutil_test.py
│   └── mathutil_prime_test.py
└── listutil/
    ├── listutil.py
    ├── listutil_test.py
    └── listutil_chunk_test.py
```

## Running the tests

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest
```
