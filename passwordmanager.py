# Passwordmanager.py
import time as time
from datetime import date

# Functions

# Warinings
def user_warning():
    '''
   --> Before running the code make sure you have python 3.7 or above version installed and do not change code in any line cuz you know it runs
       by luck ;) jk xD... 
   --> Also this password manager is not connected to any online/offline server so there is  100% security...
   --> Do not change the code in system_time() function, else it may return corrupt time values... 
   --> The "password.txt" file will auto-generate in the folder...
   --> Do not delete the "password.txt"  file because it has the passwords saved in it...
   --> If you can see this, then the code will run smoothly... 
    '''
    return 0


# For maintaining logs
def system_time():
    '''This function returns current date and time to maintain log records of login'''
    # date
    today = date.today()
    date_now = today.strftime("%d/%m/%Y")
    # Blank Str
    blank = " "
    # time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_date_and_time = str(date_now) + str(blank) + str(current_time)
    return current_date_and_time

# Printing Warnings
print(user_warning.__doc__)

# This is an infinte loop that only terminates if you kill the terminal
while True:
    # opening the file password.txt
    txt = open("password.txt", "a+")
    txt.write("\n")

    # Entering time in txt file
    txt.write("Time of Login: ")
    txt.write(system_time())
    txt.write("\n")

    # app name input and converting it to lowercase ;)
    app_name = input("Enter the name of App(YouTube, Instagram, Google, etc...): ")
    app_name_lower = app_name.lower()
    
    # Running the code
    txt.write("App/Website: ") 
    txt.write(app_name_lower)
    txt.write("\n")
    x = input("Enter username: ")
    txt.write("Username: ")
    txt.write(x)
    txt.write("\n")
    y = input("Enter Password: ")
    txt.write("Password: ")
    txt.write(y)
    txt.write("\n")

# Enjoy ;)