#from CheckModules import importcheck

# Initiates constant variables
absalon_url = "https://absalon.ku.dk"
stats_course_files_url = "https://absalon.ku.dk/courses/22297/files?"
which_browser = "Chrome"

# Perform importcheck for required modules

# Imports necessary modules/functions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import os

# Initiates user input variables - login details
print("Please provide your absalon username:")
absalon_username = input()
print("Please provide your absalon password")
absalon_password = input()
# print("What is your desired download directory")
# download_directory = input()

# Launch a Firefox browser
if which_browser == "Firefox":
    driver = webdriver.Firefox()

# Launch a Chrome browser, access the absalon URL
if which_browser == "Chrome":
    driver = webdriver.Chrome()

# Access Absalon url and login to Absalon with provided username and password
driver.get(absalon_url)
login_elem = driver.find_element_by_name("username")
login_elem.clear()
login_elem.send_keys(absalon_username)
password_elem = driver.find_element_by_name("password")
password_elem.clear()
password_elem.send_keys(absalon_password)
password_elem.send_keys(Keys.RETURN)

#Access a specific course url's files (in this example, Statistics for Bioinformatics and eScience)
driver.get(stats_course_files_url)
time.sleep(2)
all_elements = driver.find_elements_by_class_name("ef-name-col__link")
# os.chdir(download_directory)
files_in_dir = os.listdir()
files_in_dir.append("course_image")
print(files_in_dir)
for download_element in all_elements:
    print(download_element.text)
    if download_element.text in files_in_dir:
        continue
    else:
        print("Getting this element")
        download_url = download_element.get_attribute("href")
        print(download_url)
        driver.get(download_url)

#Check current working directory for presence of the files, if absent then downloads them to working directory
#Might output the list to a file and so unwanted files aren't repeatedly downloaded



#Finally close browser
driver.close()                                

