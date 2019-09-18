import time
from selenium import webdriver


class chapter3Screen:
    def Chapter3(self, url):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        # Implicit Wait
        driver.implicitly_wait(5)
        driver.find_element_by_link_text("Chapter3").click()
        time.sleep(2)
        fetchvalue = driver.find_element_by_id("leftdiv").text
        print(fetchvalue)
        time.sleep(1)
        # difference between text and getattribute()
        # https://stackoverflow.com/questions/32307702/difference-b-w-gettext-and-getattribute-in-selenium-webdriver
        attributevalue = driver.find_element_by_id("leftdiv").get_attribute("class")
        print(attributevalue)
        time.sleep(1)
        driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter3.png")
        time.sleep(1)
        driver.close()
