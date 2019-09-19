# https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
# The above link provides the list of keyboard commands.

from pywinauto import keyboard, mouse
from selenium import webdriver
import time


driver = webdriver.Firefox()
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
driver.close()