import pytest
import os
from api.lenvendo import LenvendoAPI


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL"))


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.option.base_url


@pytest.fixture(scope="session")
def lenvendo_api(base_url):
    return LenvendoAPI(base_url)
