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
import requests
import sys

session = requests.Session()
print("Please provide your absalon username:")
absalon_username = input()
print("Please provide your absalon password:")
absalon_password = input()
absalon_url = "https://intranet.ku.dk/CookieAuth.dll?GetLogon?curl=Z2F&reason=0&formdir=7"
absalon_login = {'username': absalon_password,
                 'password': absalon_username}

posted_request = session.post(absalon_url,absalon_login)
print("New URL: ", posted_request.url)
print("Status Code: ", posted_request.status_code)
print("History: ", posted_request.history)

#Attempt to access a logged-in page
r = session.get('https://absalon.ku.dk/profile')
