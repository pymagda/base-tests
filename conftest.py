import pytest
from selenium import webdriver

@pytest.fixture
def driver(variables):
    return variables['driver']

@pytest.fixture
def url(driver):
    return driver['url']

@pytest.fixture
def wait(driver):
    return driver['wait']

@pytest.fixture
def window_width(driver):
    return driver['window'][0]

@pytest.fixture
def window_height(driver):
    return driver['window'][1]

@pytest.fixture
def driver_setup(request):
    url = request.getfuncargvalue("url")
    wait = request.getfuncargvalue("wait")
    window_width = request.getfuncargvalue("window_width")
    window_height = request.getfuncargvalue("window_height")
    request.instance.driver = webdriver.Chrome()
    request.instance.driver.get(url)
    request.instance.driver.implicitly_wait(wait)
    request.instance.driver.set_window_size(window_width, window_height)

    def teardown():
        request.instance.driver.quit()

    request.addfinalizer(teardown)

@pytest.fixture
def user(variables):
    return variables['user']
