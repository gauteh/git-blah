import pytest

import pytest


def pytest_addoption(parser):
    parser.addoption(
            "--show-plot", action="store_true", default=False, help="show plots"
            )


@pytest.fixture
def show_plot(pytestconfig):
    return pytestconfig.getoption('show_plot')

