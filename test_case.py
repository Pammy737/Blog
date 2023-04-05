from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from fixture import driver_fixture

use_fixtures = [driver_fixture]


def test_next_about(driver: Chrome):
    """to make sure website returns the about page (next parameter)  """

    # click about btn
    about_btn = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='navbarResponsive']/ul/li[2]/a")))
    about_btn.click()

    first_login_page = driver.current_url
    print(first_login_page)

    login_process(driver, first_login_page)

    print(driver.current_url)
    assert driver.current_url == "http://127.0.0.1:5000/about"


def test_next_comment(driver: Chrome):
    """to make sure website returns the previous post page (next parameter)  """

    # click post btn
    post_btn = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/a/h2")))
    post_btn.click()
    post_page = driver.current_url

    # comment
    enter_comment(driver)

    first_login_page = driver.current_url
    print(first_login_page)

    login_process(driver, first_login_page)

    print(driver.current_url)
    assert driver.current_url == post_page


def login_process(driver, first_login_page):
    # register page enter_register_data data
    if driver.current_url != first_login_page:
        enter_register_data(driver)
        enter_login_data(driver)
    else:
        # Login page enter_login_data data
        enter_login_data(driver)


def enter_login_data(driver):
    user_email = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "// *[ @ id = 'email']")))
    user_email.send_keys("test000@gmail.com")
    time.sleep(1)
    user_email.send_keys(Keys.TAB)
    password = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "// *[ @ id = 'password']")))
    password.send_keys("test000")
    password.send_keys(Keys.ENTER)


def enter_register_data(driver):
    username = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "// *[ @ id ='name']")))
    username.send_keys("test0000")
    username.send_keys(Keys.TAB)
    user_email = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    user_email.send_keys("test000@gmail.com")
    password = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    password.send_keys(Keys.TAB)
    password.send_keys("test000")
    password.send_keys(Keys.ENTER)


def enter_comment(driver):
    # switch to iframe (ckeditor)
    iframe = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)
    time.sleep(1)
    # comment box
    comment_box = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/p")))
    comment_box.send_keys("I am Test Comment")
    # leaving frame
    driver.switch_to.default_content()
    # click submit btn
    submit_btn = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
    submit_btn.click()
