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
        1: Add passwords 3: View passwords 4: Exit :""").strip()
        return mode


        
    

# Main routine - Run main program in a loop.


print("Welcome to Password Manager!!")

name = input("What is your name? ")
age = int(input ("How old are you? "))

while True:
    #asking for user input and .upper() function converts user input to upper case
    member = input("Please enter | L for log in or | N for new account: ").upper()

    if member == "L":
        m_username = input("Enter username: ")
        m_password = input("Enter password: ")
        if m_username and m_password in member_list:
            print("username and password match!!")
        break
    elif member == "N":
        m_username = input("Enter username: ")
        m_password = input("Choose password at least 8 characters long, Enter password: ").strip()
            
        member_list.append([m_username, m_password])
        print("Your account created!!")
        break
        
    else:
        print("That was not a valid option, please enter L for log in or N for creating new account: ")
        
    
while True:
    chosen_option = menu(name, age)
    
    if chosen_option == "1":
        #Call add_tasks function if user chooses 1
        print("Successful, write add_passwords function")
        #add_details()
        
    elif chosen_option == "2":
        #Call add_tasks function if the user chooses 1
        print("Successful, write view_passwords funtion")
        #view_passwords()
        
    elif chosen_option == "3":
        #Say goodbye and end programme
        break
    
    else:
        print("That was not avalid option, please try again")

 

print("Goodbye, thanks for using password manager")
            
            
