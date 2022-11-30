import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException



class InstaFollower():

    def __init__(self, driver, url):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)

    def login(self, login, password):
        time.sleep(2)
        user_box = self.driver.find_element(By.NAME, "username")
        pw_box = self.driver.find_element(By.NAME, "password")
        submit_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")
        user_box.send_keys(login)
        pw_box.send_keys(password)
        submit_box.submit()


    def find_followers(self, similar_account):
        time.sleep(5)
        search_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_box.send_keys(similar_account)
        
        time.sleep(3)
        sm_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
        sm_box.click()
        time.sleep(2)

        followers = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        time.sleep(2)
        
        for _ in range(2):
            self.follow()
            modal = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self):
        time.sleep(2)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

        



