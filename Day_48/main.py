from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

cookie_clicker = None
lang_select = None

chrome_driver_path = "Day_48/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

tab_1 = driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

lang_select = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
lang_select.click()

time.sleep(10)

print(cookie_clicker)
cookie_clicker = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]
timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie_clicker.click()

    if time.time() > timeout:
        
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store .content")
        item_prices = []

        for price in  all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append()

        cookie_upgrades = {}

        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids(n)

        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")
        
        cookie_count = int(money_element)

        affordable_upgrades = {}

        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_prices_affordable = max(affordable_upgrades)
        print(highest_prices_affordable)
        to_purchase_id = affordable_upgrades[highest_prices_affordable]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()