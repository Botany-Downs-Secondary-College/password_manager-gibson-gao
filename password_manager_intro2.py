#password_manager.py
#create and display passwords for users
#P.Patchigalla, Feb 21


#initialise variables and lists

name = ""
age = int(0)
# create an empty list to store usernames and passwords for web/apps
password_list = []
# create a list with existing members and store new member details
member_list = ["bdsc", "pass123"]


# The menu() Function prints out the menu for user to choose an option
#and returns user option to main routine
def menu(name, age):

    print("Hello", name)

    if age < 13:
        print("Sorry, you do not qualify to open an account. ")
        exit()

    else:
    
        mode = input("""Choose a mode by entering the number:
        1: Add passwords 2: View passwords 3: Exit :""").strip()
        return mode

# Main routine - Run main program in a loop.

print("Welcome to Password Manager!!")
print("If you are 13 or older, You can store access details to web or mobile apps")

name = input("What is your name? ")
age = float(input ("How old are you? "))


while True:
    chosen_option = menu(name, age)
    
    if chosen_option == "1":
        #Call add_tasks function if user chooses 1
        print("Successful")
        #add_details()
        
    elif chosen_option == "2":
        #Call add_tasks function if the user chooses 1
        print("Successful")
        #view_list()
        
    elif chosen_option == "3":
        #Say goodbye and end programme
        break
    
    else:
        print("That was not avalid option, please try again")

print("Goodbye, thanks for using password manager")
            
