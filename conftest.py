"""Records each test's owning Bazel target as a JUnit XML property.

Every py_test target sets the TEST_SELECTOR_PRIMARY env var to its own
label. When running under plain pytest (no Bazel), the env var is unset
and this hook does nothing.
"""

import os
import time

import pytest


def pytest_collection_modifyitems(items):
    target = os.environ.get("TEST_SELECTOR_PRIMARY")
    if not target:
        return
    for item in items:
        item.user_properties.append(("buildkite.tag.test.selector.primary", target))


@pytest.fixture(autouse=True)
def _simulate_test_duration():
    # Real assertions here run in ~0ms, which makes reported durations
    # uninteresting for demos (e.g. duration-based test splitting). Sleep
    # a bit so each test reports a non-zero, semi-realistic duration.
    time.sleep(0.2)
