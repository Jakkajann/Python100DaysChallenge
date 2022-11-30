#Python web scrap

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="Day_48/chromedriver.exe")

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

event_times = [time.text for time in event_times]
event_names = [name.text for name in event_names]

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n],
    }

print(events)

driver.close()