"""Records each test's owning Bazel target as a JUnit XML property.

Every py_test target sets the TEST_SELECTOR_PRIMARY env var to its own
label. When running under plain pytest (no Bazel), the env var is unset
and this hook does nothing.
"""

import os


def pytest_collection_modifyitems(items):
    target = os.environ.get("TEST_SELECTOR_PRIMARY")
    if not target:
        return
    for item in items:
        item.user_properties.append(("buildkite.tag.test.selector.primary", target))
