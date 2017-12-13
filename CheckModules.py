#First must check if all packages needed are installed

test_lom = ["numpy","scipy","Bio"]
for i in range(len(test_lom)):
    test_lom[i] = "import "+test_lom[i]
    exec(test_lom[i])


def importcheck(list_of_modules):
    for cur_module in list_of_modules:
        print(str(cur_module))
        cur_module = "import " + cur_module
        try:
            exec(cur_module)
        except ImportError:
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

