# https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
# The above link provides the list of keyboard commands.

from pywinauto import keyboard
from selenium import webdriver
import time


class winAuto(object):
    def automation(self):
        driver = webdriver.Firefox()
        try:
            driver.get("https://www.seleniumhq.org/download/")
            driver.maximize_window()
            driver.find_element_by_xpath("//td[text()='Java']/..//*[contains(text(),'Download')]").click()
            time.sleep(1)
            # Handling windows based pop using pywinauto package.
            keyboard.send_keys("{TAB}")
            keyboard.send_keys("{TAB}")
            time.sleep(1)
            keyboard.send_keys("{TAB}")
            keyboard.send_keys("{TAB}")
            keyboard.send_keys("{ENTER}")
        except Exception as e:
            print("Error occured:")
            print(str(e))
        else:
            print("Else block will work only when there is no exception. But Finally block will execute all the times.")
        finally:
            driver.close()


# Creating object of class winauto().
obj = winAuto()
# Calling automation method by creating object of winauto.
obj.automation()
