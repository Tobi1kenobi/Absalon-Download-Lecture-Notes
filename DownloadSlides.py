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
    import placeholdermodulename
except ImportError:
    importcheck()

#Attempt to login to Absalon/KU intranet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


absalon_url = "https://absalon.ku.dk"
print("Please provide your absalon username:")
absalon_username = input()
print("Please provide your absalon password")
absalon_password = input()


driver = webdriver.Chrome()
driver.get(absalon_url)
login_elem = driver.find_element_by_name("username")
login_elem.clear()
login_elem.send_keys(absalon_username)
password_elem = driver.find_element_by_name("password")
password_elem.clear()
password_elem.send_keys(absalon_password)
password_elem.send_keys(Keys.RETURN)

