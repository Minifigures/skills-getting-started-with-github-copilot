from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(scope="session")
def baseline_activities():
    return deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(baseline_activities):
    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline_activities))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline_activities))


@pytest.fixture
def client():
    return TestClient(app_module.app)
