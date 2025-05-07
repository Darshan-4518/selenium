import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.environ['PATH'] += "drivers/"

driver =  webdriver.Chrome()
driver.get("https://demoqa.com/")
title = "DEMOQA"
try:
    assert title in driver.title
except AssertionError:
    print(f"title is not {title}")

forms_redirection_ele = driver.find_element(By.XPATH,"//div[@class='card mt-4 top-card'][2]")
forms_redirection_ele.click()
practice_form_label = driver.find_element(By.XPATH,"//div[@class='element-list collapse show']/ul/li")
# print(practice_form_label.get_attribute("id"))
practice_form_label.click()
fn = driver.find_element(By.ID,"firstName")
fn.send_keys("darshan")
ln = driver.find_element(By.CSS_SELECTOR,"#lastName")
ln.send_keys("virani")
email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("darshan4518@gamil.com")
male_gen_radio = driver.find_element(By.XPATH,"//div[@class='custom-control custom-radio custom-control-inline'][1]/input[@id='gender-radio-1']")
male_gen_radio.click()
time.sleep(10)