from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user = os.environ.get("LINKEDIN_USER")
pw = os.environ.get("LINKEDIN_PASSWORD")
phone = os.environ.get("PHON_NUM")

driver = webdriver.Chrome(executable_path="Day_49/chromedriver.exe")

driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fjobs%2Fapplication-settings%2F%3FhideTitle%3Dtrue&fromSignIn=true&trk=cold_join_sign_in")

email_box = driver.find_element(By.NAME, "session_key")
email_box.send_keys(user)
password_box = driver.find_element(By.NAME, "session_password")
password_box.send_keys(pw)
submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

time.sleep(1)
submit_button.click()

job_tab = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job_tab.click()

time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container__link")

for job in jobs:
    print(job.text)

jobs[0].click()

time.sleep(1)

apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
apply_button.click()
