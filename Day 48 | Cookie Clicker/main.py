from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/AadityaKharkia/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
for time in event_time:
    print(time.text)
event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
for events in event_name:
    print(events.text)

dis = {}

for i in range(0,len(event_time)):
    dis[i] = {
        "Time":event_time[i].text,
        "Event":event_name[i].text
    }
print(dis)

driver.quit()