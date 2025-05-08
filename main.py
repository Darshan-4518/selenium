import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os

def main():
    os.environ['PATH'] += "drivers"

    driver = None

    try:
        driver =  webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://demoqa.com")
        click_an_element(driver=driver,type=By.XPATH,selector_value="//div[@class='category-cards'][1]/div[2]")
        click_an_element(driver=driver,type=By.XPATH,selector_value='//div[@class="element-list collapse show"]/ul/li')
        send_value(driver=driver,type=By.ID,selector_value="firstName",display_value="darshan")
        send_value(driver=driver,type=By.CSS_SELECTOR,selector_value="#lastName",display_value="virani")
        send_value(driver=driver,type=By.XPATH,selector_value="//div[@class='col-md-9 col-sm-12'][1]/input",display_value="darshan123@gmail.com")
        click_an_element(driver=driver,type=By.XPATH,selector_value="""//div[@id="genterWrapper"]/div[@class='col-md-9 col-sm-12']/div[@class="custom-control custom-radio custom-control-inline"][1]/label""")
        send_value(driver=driver,type=By.ID,selector_value="""userNumber""",display_value="9874561230")
        # send_value(driver=driver,type=By.ID,selector_value="dateOfBirthInput",display_value="23 May 2025")
        click_an_element(driver=driver,type=By.XPATH,selector_value="//div[@class='custom-control custom-checkbox custom-control-inline'][1]/label")
        click_an_element(driver=driver,type=By.XPATH,selector_value="//div[@class='custom-control custom-checkbox custom-control-inline'][2]/label")
        click_an_element(driver=driver,type=By.XPATH,selector_value="//div[@class='custom-control custom-checkbox custom-control-inline'][3]/label")
        send_value(driver=driver,type=By.CSS_SELECTOR,selector_value="#subjectsInput",display_value="cricket")
        send_value(driver=driver,type=By.XPATH,selector_value="//input[@type='file']",display_value=f"{os.getcwd()}/drivers/chromeDriver")
        time.sleep(5)
        send_value(driver=driver,type=By.TAG_NAME,selector_value="textarea",display_value="this is selenium script to fill the form")
        click_an_element(driver=driver,type=By.XPATH,selector_value='//div[@class=" css-1wy0on6"]')
        # press_the_key(driver=driver,key=Keys.RETURN)
        click_an_element(driver=driver,type=By.ID,selector_value="submit")

        time.sleep(10)
    except Exception as e:
        print(e)
    finally:
        driver.close()

def click_an_element(driver,type,selector_value):
    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((type,selector_value))
    ).click()

def send_value(driver,type,selector_value,display_value):
    element = WebDriverWait(driver,10).until(
        EC.visibility_of(driver.find_element(type,selector_value))
    )
    element.clear()
    element.send_keys(display_value)
def date_set(driver,type,selector_value,display_value):
    date_ele = WebDriverWait(driver,10).until(
        EC.visibility_of(driver.find_element(type,selector_value))
    )
    date_ele.clear()
    driver.execute_script(f"arguments[0].value = '{display_value}';", date_ele)

def press_the_key(driver,key):
    ActionChains(driver).send_keys(key).perform()

if __name__ == "__main__":
    main()