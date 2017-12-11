#First must check if all packages needed are installed
def importcheck():
    print("Module not found, would you like to install it? Y/N")
    for i in range(5):
        install_response = input()
        if install_response == "Y":
            #install module
            break
        elif install_response == "N":
            print("Cannot proceed without required modules")
            quit()
        elif i == 4:
            print("Invalid input has been given ",i+1," times")
            quit()
        else:
            print("Invalid input, try again. Would you like to install the missing module Y/N?")
            continue


try:
    pass
    #import placeholdermodulename
except ImportError:
    importcheck()

#Attempt to login to Absalon/KU intranet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


absalon_url = "https://absalon.ku.dk"
stats_course_files_url = "https://absalon.ku.dk/courses/22297/files?"
print("Please provide your absalon username:")
absalon_username = input()
print("Please provide your absalon password")
absalon_password = input()

# Launch a Chrome browser, access the absalon URL
options = webdriver.ChromeOptions()
options.add_argument('--window-size=500,500')
driver = webdriver.Chrome(chrome_options=options)
#driver.set_window_size(10, 10)
driver.get(absalon_url)

#Login to Absalon with provided username and password
login_elem = driver.find_element_by_name("username")
login_elem.clear()
login_elem.send_keys(absalon_username)
password_elem = driver.find_element_by_name("password")
password_elem.clear()
password_elem.send_keys(absalon_password)
password_elem.send_keys(Keys.RETURN)

#Access a specific course url's files (in this example, Statistics for Bioinformatics and eScience)
driver.get(stats_course_files_url)
all_elements = driver.find_elements_by_class_name("ef-name-col__text")
for element in all_elements:
    print(element.text)

#Check current working directory for presence of the files, if absent then downloads them to working directory
#Might output the list to a file and so unwanted files aren't repeatedly downloaded



#Finally close browser
driver.close()