import os

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    os.environ['PATH'] += "drivers/"
    driver = None
    try:
        driver = Chrome()
        driver.get("https://demoqa.com/")
        click_an_element(driver,By.XPATH,"//div[@class='card mt-4 top-card'][1]")
        click_an_element(driver,By.XPATH,'(//div)[35]')
        time.sleep(10)
    except BaseException as be:
        print(be)
    finally:
        driver.close()

def click_an_element(driver,type,selector):
    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(driver.find_element(type,selector))
    ).click()

if __name__ == "__main__":
    main()