from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/AadityaKharkia/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url ="https://orteil.dashnet.org/experiment/cookieclicker/"

cookie = driver.find_element(by=By.ID, value="bigCookie")

driver = webdriver.Chrome(chrome_driver_path)
driver.get(url=url)