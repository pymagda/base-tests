import pytest

@pytest.fixture
def lead(variables):
    return variables['lead']

@pytest.fixture
def lead_statuses(variables):
    return variables['lead_statuses']
