from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from fixture import driver_fixture

use_fixtures = [driver_fixture]


def test_next_about(driver: Chrome):
    """to make sure website returns the about page (next parameter)  """

    # click about btn
    about_btn = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='navbarResponsive']/ul/li[2]/a")))
    about_btn.click()

    print(driver.current_url)

    login_process(driver)

    print(driver.current_url)
    assert driver.current_url == "http://127.0.0.1:5000/about"


def test_next_comment(driver: Chrome):
    """to make sure website returns the previous post page (next parameter)  """

    # click post btn, if not post exists then create one
    try:
        post_btn = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/a/h2")))
        post_btn.click()
        print("clicked")
    except TimeoutException:
        print("I'm here")
        login_btn = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='navbarResponsive']/ul/li[3]/a")))
        login_btn.click()
        enter_login_data(driver)
        create_post(driver)
        post_btn = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/a/h2")))
        post_btn.click()
        logout = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='navbarResponsive']/ul/li[3]/a")))
        logout.click()

    finally:
        post_page = driver.current_url

    # comment
    enter_comment(driver)
    login_process(driver)

    print(driver.current_url)
    assert driver.current_url == post_page


def login_process(driver):
    # Login page enter_login_data data
    enter_login_data(driver)

    # register page enter_register_data data
    if "register" in driver.current_url:
        enter_register_data(driver)
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
    username.send_keys("test000")
    username.send_keys(Keys.TAB)
    user_email = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    user_email.send_keys("test000@gmail.com")
    password = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    password.send_keys(Keys.TAB)
    password.send_keys("test000")
    password.send_keys(Keys.ENTER)


def switch_to_iframe(driver):
    # switch to iframe (ckeditor)
    iframe = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)
    time.sleep(1)


def leave_frame(driver):
    # leaving frame
    driver.switch_to.default_content()
    # click submit btn
    submit_btn = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
    submit_btn.click()


def enter_comment(driver):
    switch_to_iframe(driver)
    # comment box
    comment_box = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/p")))
    comment_box.send_keys("I am Test Comment")
    leave_frame(driver)


def create_post(driver):
    post = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/a")))
    post.click()
    post_title = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "// *[ @ id = 'title']")))
    post_title.send_keys("Test")
    post_sub = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "// *[ @ id = 'subtitle']")))
    post_sub.send_keys("test")
    image = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "// *[@ id = 'img_url']")))
    image.send_keys(
        "https://images.unsplash.com/photo-1534644107580-3a4dbd494a95?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80")
    switch_to_iframe(driver)
    post_box = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, " html / body / p")))
    post_box.send_keys("I am test")
    leave_frame(driver)
