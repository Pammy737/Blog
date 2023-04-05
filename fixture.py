import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(name="driver", scope="function")
def driver_fixture():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url="http://127.0.0.1:5000/")
    yield driver
    driver.quit()