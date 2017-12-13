# from CheckModules import importcheck
# Imports necessary modules/functions
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Initiates user input variables - login details
def fetch_login_details(abs_username,abs_password,user_input = False):
    """Fetches login details, can accept user input if user_input == True"""
    if user_input == True: 
        print("Please provide your absalon username:")
        abs_username = input()
        print("Please provide your absalon password")
        abs_password = input()
    return ((abs_username,abs_password))

def launch_browser(download_directory,browser_choice = "Chrome"):
    """Launches a Chrome or Firefox browser using Selenium webdriver and sets"""
    if browser_choice == "Chrome":
        DRIVER = webdriver.Chrome()
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : download_directory}
        chromeOptions.add_experimental_option("prefs",prefs)
    if browser_choice == "Firefox":
        DRIVER = webdriver.Firefox()
    return DRIVER

# Access Absalon url and login to Absalon with provided username and 
def access_absalon(driver,login):
    driver.get("https://absalon.ku.dk")
    LOGIN_ELEMENT = driver.find_element_by_name("username")
    LOGIN_ELEMENT.clear()
    LOGIN_ELEMENT.send_keys(login[0])
    PASSWORD_ELEMENT = driver.find_element_by_name("password")
    PASSWORD_ELEMENT.clear()
    PASSWORD_ELEMENT.send_keys(login[1])
    PASSWORD_ELEMENT.send_keys(Keys.RETURN)
    return driver

#Access a specific course url's files (in this example, Statistics for Bioinformatics and eScience)
def access_abs_files_url(driver,download_dir,abs_course_number = "22297"):
    driver.get("https://absalon.ku.dk/courses/"+abs_course_number+"/files?")
    time.sleep(1)
    all_elements = driver.find_elements_by_class_name("ef-name-col__link")
    ACQUIRED_FILES = []
    FILES_IN_DIRECTORY = os.listdir(download_dir)
    FILES_IN_DIRECTORY.append("course_image")
    for download_element in all_elements:
        if download_element.text in FILES_IN_DIRECTORY:
            continue
        else:
            ACQUIRED_FILES.append(download_element.text)
            download_url = download_element.get_attribute("href")
            driver.get(download_url)
    return ACQUIRED_FILES
