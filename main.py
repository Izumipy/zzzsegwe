from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import random
import os

EMAIL = 'weebxedit.ss@gmail.com'
PASSWORD = 'dankmemer123'
CHANNEL = '1272198034440065024'
CHANNEL_NAME = '・anigame '
WAIT = 15

go_fishing = "//button[div/div/div[contains(text(), 'Go Fishing')]]"
right = "//button[div/div/img[@class='emoji' and @alt='AR']]"
left = "//button[div/div/img[@class='emoji' and @alt='AL']]"
up = "//button[div/div/img[@class='emoji' and @alt='AU']]"
down = "//button[div/div/img[@class='emoji' and @alt='AD']]"
catch = "//button[div/div/div[contains(text(), 'Catch')]]"

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('https://discord.com/login')

time.sleep(5)

EMAIL_field = driver.find_element(By.NAME, 'email')
PASSWORD_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

EMAIL_field.send_keys(EMAIL)
PASSWORD_field.send_keys(PASSWORD)

login_button.click()

time.sleep(10)

driver.get(CHANNEL)

time.sleep(10)

def catch_fish():
    message_input = driver.find_element(By.XPATH, f'//div[@aria-label="Message #{CHANNEL_NAME}"]')
    time.sleep(2)
    time.sleep(10)

    while True:
        try:
            message_input.send_keys('pls fish catch')
            message_input.send_keys(Keys.RETURN)

            start = driver.find_element(By.XPATH, "//button[div/div/div[contains(text(), 'Go Fishing')]]")
            driver.execute_script("arguments[0].click();", start)

            time.sleep(5)

            direction_button1 = random.choice([right, left, up, down])
            
            first_click = driver.find_element(By.XPATH, direction_button1)
            driver.execute_script("arguments[0].click();", first_click)
            time.sleep(random.uniform(0.5, 1.5))
            
            direction_button2 = random.choice([right, left, up, down])

            second_click = driver.find_element(By.XPATH, direction_button2)
            driver.execute_script("arguments[0].click();", second_click)
            time.sleep(random.uniform(0.5, 1.5))
            
            catch_button = driver.find_element(By.XPATH, catch)
            driver.execute_script("arguments[0].click();", catch_button)
            
            time.sleep(WAIT)
        except:
            pass

os.system('cls')

catch_fish()
