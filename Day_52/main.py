
from insta_follower import InstaFollower
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "Day_52/chromedriver.exe"
login = "login"
pw = "senha!"
insta_url = "https://www.instagram.com/accounts/login/"

similar_account = "lucasinutilismo"

driver = InstaFollower(chrome_driver, insta_url)

driver.login(login, pw)

driver.find_followers(similar_account)