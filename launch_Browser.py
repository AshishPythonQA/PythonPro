# Selenium Basics
import time
import configparser
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SelBrowser:

    # multiple Window Handles
    driver = webdriver.Firefox()
    driver.get("http://demo.guru99.com/popup.php")
    time.sleep(1)
    driver.find_element_by_link_text("Click Here").click()
    time.sleep(1)
    size = len(driver.window_handles)
    print(size)
    window_before = driver.window_handles[0]
    for x in range(size):
        if window_before != driver.window_handles[x]:
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[x])
            time.sleep(1)
            driver.find_element_by_name("emailid").send_keys("vina@gmail.com")
            driver.find_element_by_name("btnLogin").click()
            driver.switch_to.window(window_before)
            #driver.quit()

    # Importing data from Properties File like username and pwd or DB details.
    # Header is mandatory for configparser with square braces i.e [ ]
    parser = configparser.RawConfigParser()
    parser.read("Test1.properties")
    username = parser.get("UserDetails", "username")
    password = parser.get("UserDetails", "pwd")
    print("The username is '%s' and password is '%s'" % (username, password))

    hostName = parser.get("DBDetails", "Hostname")
    port = parser.get("DBDetails", "port")
    sid = parser.get("DBDetails", "sid")
    print("The hostName is '%s', port is '%s', sid is '%s'" % (hostName, port, sid))

    # r - Read Lines
    # w+ - it indicates that it will create a new file if it does not exist and then write a File
    # a+ - it indicates that it will create a new file if it does not exist and then appends to a File
    # x - Creates a new file. If file already exists, the operation fails.
    # t - This is the default mode. It opens in text mode.
    # b - This opens in binary mode

    # Reading data from File
    readFile = open("inputFile.txt", 'r')
    lines = readFile.readlines()
    for r in lines:
        print(r)

    # Writing data to the file
    writeFile = open("inputFile.txt", 'w+')
    for i in range(0, 10):
        writeFile.write("The line numvber1 is %d \n" % (i+1))
    writeFile.close()

    # Appending data to existing file
    appendFile = open("inputFile.txt", 'a+')
    for i in range(1, 7):
        appendFile.write("Appending line number is %d \n" % (i+1))
    appendFile.close()

    # driver = webdriver.Firefox()
    driver.get("http://book.theautomatedtester.co.uk/")
    driver.maximize_window()
    # Implicit Wait
    driver.implicitly_wait(5)

    # Finding multiple elements in the main page.
    links = driver.find_elements_by_tag_name("a")
    for totalLinks in links:
        print(totalLinks.text)
    total = len(links)
    print("There are %d links in the homePage." % total)

    time.sleep(1)
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
    textData = driver.find_element_by_tag_name("p").text  # in Java we use .getText()
    time.sleep(1)
    print(textData)
    driver.find_element_by_xpath("//input[@id='storeinput']").send_keys("hello1")
    time.sleep(1)

    # select class to select dropdowns
    select = Select(driver.find_element_by_id("selecttype"))

    # by visible text
    for opt in select.options:
        print(opt.text)
        if opt.text == "Selenium Grid":
            select.select_by_visible_text(opt.text)
            print("selected "+opt.text+" dropdown")

    # by index
    for index in range(len(select.options)):
        select.select_by_index(index)
        time.sleep(1)

    time.sleep(2)
    driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter1.png")

    # Navigate to home page
    driver.find_element_by_link_text("Home Page").click()
    time.sleep(2)
    driver.find_element_by_link_text("Chapter3").click()
    time.sleep(2)
    fetchValue = driver.find_element_by_id("leftdiv").text
    print(fetchValue)
    time.sleep(1)

    # difference between text and getattribute()
    # https://stackoverflow.com/questions/32307702/difference-b-w-gettext-and-getattribute-in-selenium-webdriver
    attributeValue = driver.find_element_by_id("leftdiv").get_attribute("class")
    print(attributeValue)
    time.sleep(1)
    driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter3.png")

    # Navigate to home page
    driver.find_element_by_link_text("Index").click()
    time.sleep(1)
    driver.find_element_by_link_text("Chapter4").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@type='text']").send_keys("Test input")
    time.sleep(1)

    # selecting drop downs
    select = Select(driver.find_element_by_id("selecttype"))

    # select options by values
    for opt in select.options:
        if opt.text == "Selenium Grid":
            select.select_by_visible_text(opt.text)
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
    popupText = driver.switch_to.alert.text
    time.sleep(2)
    driver.switch_to.alert.accept()
    if popupText == "hello":
        print("the pop up value is '%s'" % popupText)
    else:
        print("incorrect value")
    driver.get_screenshot_as_file("C:\\Users\\VinayVinay\\Desktop\\Python_Selenium_Screenshot\\Chapter4.png")
    time.sleep(1)
    driver.quit()


""" driver.switch_to.frame()
    driver.switch_to.parent_frame()
    driver.switch_to.default_content()
    driver.close()  """
