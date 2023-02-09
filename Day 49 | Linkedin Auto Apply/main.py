import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "C:/Users/PC 28/Desktop/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url="https://www.linkedin.com/jobs/search/?currentJobId=3475808799&f_AL=true&f_WT=2&geoId=103644278&keywords=python%20development&location=United%20States&refresh=true"
driver.get(url=url)
time.sleep(2)

Sign_in = driver.find_element(By.CLASS_NAME,"nav__button-secondary")
Sign_in.click()
time.sleep(3)

Email = driver.find_element(By.ID, "username").send_keys("aadityakharkia10@gmail.com")
Password = driver.find_element(By.ID,"password").send_keys("")

sign = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign.click()
time.sleep(3)

job1 = driver.find_element(By.ID, "ember194")
job1.click()


time.sleep(3)
driver.quit()