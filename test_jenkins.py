import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

def setup_function():
    global driver
    driver= webdriver.Chrome(service=ChromeDriver(ChromeDriverManager().install()))
    driver.get('https://alnafi.com/auth/sign-in')
    driver.maximize_window()

def teardown_function():

    driver.quit()


def mycred():
    return [
        ('munaim', 'mun@gmail.com'),
        ('munaim', 'mun@gmail.com'),
        ('munaim', 'mun@gmail.com'),
        ('munaim', 'mun@gmail.com')
    ]
@pytest.mark.parametrize('username,password',mycred())
def test_login(username,password):
    print('My test login')
    driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys(username)
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input').send_keys(password)
