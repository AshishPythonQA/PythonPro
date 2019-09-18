import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Excel import ExcelOperations


class chapter1Test4:
    def Chapter1_Test4(self, url):
        excel = ExcelOperations.ExcelData()
        try:
            driver = webdriver.Firefox()
            driver.get(url)
            driver.maximize_window()
            # Implicit Wait
            driver.implicitly_wait(5)
            driver.find_element_by_link_text("Chapter1").click()
            time.sleep(1)
            driver.find_element_by_id("radiobutton").click()
            time.sleep(1)
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            time.sleep(1)
            driver.find_element_by_id("secondajaxbutton").click()
            time.sleep(1)
            driver.find_element_by_id("loadajax").click()
            time.sleep(1)
            textdata = driver.find_element_by_tag_name("p").text  # in Java we use .getText()
            time.sleep(1)
            print(textdata)
            driver.find_element_by_xpath("//input[@id='storeinput']").send_keys(excel.readData("Sheet1", 2, 1))
            time.sleep(1)

            # select class to select dropdowns
            select = Select(driver.find_element_by_id("selecttype"))

            # by value
            for opt in select.options:
                select.select_by_value("Selenium RC")

            # by index
            for index in range(len(select.options)):
                select.select_by_index(index)
                time.sleep(1)

            time.sleep(2)
            driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter1.png")
            time.sleep(1)
            excel.writeData("Chapter1_Data", "D6", "PASS")
            driver.close()

        except Exception as e:
            excel.writeData("Chapter1_Data", "D6", "FAIL")
            time.sleep(1)
            excel.writeData("Chapter1_Data", "E6", str(e))
            print("Exception occurred : %s" % e)
