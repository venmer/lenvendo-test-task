import logging
import os

import allure
import pytest
import selenium.webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from furl import furl


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL"))
    parser.addoption("--username", action="store", default=os.getenv("USERNAME"))
    parser.addoption("--password", action="store", dest='password', default=os.getenv("PASSWORD"))


@pytest.fixture(scope="session")
def username(request):
    return request.config.option.username


@pytest.fixture(scope="session")
def password(request):
    return request.config.option.password


@pytest.fixture(scope="session")
def base_url(request, username, password):
    url = furl(request.config.option.base_url)
    url.username = username
    url.password = password
    return url.tostr()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def browser(request):
    wd = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wd.maximize_window()

    yield wd

    if request.node.rep_call.failed:
        try:
            allure.attach(wd.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            logging.error("Failed to attach screenshot")

    wd.quit()
