import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class chapter4Screen:
    def Chapter4(self, url):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_link_text("Chapter4").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Test input")
        time.sleep(1)

        # selecting drop downs
        select = Select(driver.find_element_by_id("selecttype"))

        # select options by values
        for opt in select.options:
            select.select_by_value("Selenium RC")
            time.sleep(1)
        time.sleep(2)

        # select options by index
        for index in range(len(select.options)):
            select.select_by_index(index)
            time.sleep(1)

        time.sleep(2)
        driver.find_element_by_id("nextBid").send_keys("40")
        time.sleep(2)
        # Action class
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_id("hoverOver")).perform()
        time.sleep(2)
        # Explicit Wait
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.alert_is_present())

        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element_by_id("blurry").send_keys("hello")
        driver.find_element_by_id("selectLoad").click()
        time.sleep(2)
        popuptext = driver.switch_to.alert.text
        time.sleep(2)
        driver.switch_to.alert.accept()
        if popuptext == "hello":
            print("the pop up value is '%s'" % popuptext)
        else:
            print("incorrect value")
        driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter4.png")
        time.sleep(1)
        driver.close()
