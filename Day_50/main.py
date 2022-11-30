from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Email and username changed

driver = webdriver.Chrome(executable_path="Day_50/chromedriver.exe")

driver.get("https://tinder.com/")
base_window = driver.window_handles[0]
time.sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="s-906875199"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
login_button.click()
time.sleep(1)
login_button = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_button.click()
time.sleep(1)
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
email = driver.find_element(By.NAME, "email")
email.send_keys("215641854@655665.com")
pw = driver.find_element(By.NAME, "pass")
pw.send_keys("541551154")
time.sleep(1)
login_face = driver.find_element(By.NAME, "login")
login_face.click()
time.sleep(5)
button_face = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div')
button_face.click()
time.sleep(2)
driver.switch_to.window(base_window)
d_button = driver.find_element(By.XPATH, '//*[@id="s-906875199"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
time.sleep(1)
d_button.click()