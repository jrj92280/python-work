import os
import random
import time

from selenium import webdriver

username = os.environ.get("USERNAME")
password = os.environ.get('PASSWORD')

if not username or not password:
    raise RuntimeError('USERNAME & PASSWORD are required environment variables.')


#
def run():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # seconds

    driver.get('https://www.linkedin.com')

    username_input = driver.find_element_by_id('login-email')
    username_input.send_keys(username)

    password_input = driver.find_element_by_id('login-password')
    password_input.send_keys(password)

    sign_in_button = driver.find_element_by_id("login-submit")
    sign_in_button.click()

    random_sleep()

    my_network_icon = driver.find_element_by_id('mynetwork-tab-icon')
    my_network_icon.click()

    random_sleep()

    invite_buttons = driver.find_elements_by_css_selector("*[data-control-name='invite']")

    for invite_button in invite_buttons:
        invite_button.click()
        random_sleep()

    driver.quit()


def random_sleep():
    sleep_time = random.randint(2, 7)
    time.sleep(sleep_time)


if __name__ == '__main__':
    run()
