from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/AadityaKharkia/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url ="http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_driver_path)
driver.get(url=url)

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

while True:
    cookie.click()
