from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/AadityaKharkia/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(by=By.ID, value="bigCookie")

