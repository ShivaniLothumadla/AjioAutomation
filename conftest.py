import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True)
def setup(request, browser, url='https://www.ajio.com/'):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'ff':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--url')

@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(autouse=True)
def url(request):
    return request.config.getoption('--url')

