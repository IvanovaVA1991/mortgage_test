import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


@pytest.fixture(scope="session")
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())  # автоматически скачивать  и устанавливать нужный вебдрайвер менеджер
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)      # инициализация драввйреа
        yield driver
        driver.quit()