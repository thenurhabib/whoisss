import os
import time
import getpass
from time import sleep
from getpass import getpass

# Author Function
def authorInformation():
     print(
    """
Name       : Whoisss
Author     : Md. nur habib
Email      : mdnurhabib12@Gmail.com
GitHub     : github.com/thenurhabib
HackerRank : hackerrank.com/thenurhabib      
    """
)

authorInformation()

# username and Password
credentials = ["habib", "whois[habib]"]
# Get Username and Password from User
print("Before Using Whoisss You have to Login.\n")
getInputUsername = input("Enter Username : ")
getInputPassword = getpass("Enter Password : ")

# Password Validation
if getInputUsername == credentials[0] and getInputPassword[1]:
    # if username and password correct now run this script
    print("\nLoading, Please wait...")
    sleep(3)
    os.system("clear")
    # Gettings Whois Information
    getTargetWebsite = input("\nEnter Domain or IP Address: ").lower()
    os.system("reset")
    authorInformation()
    print(f"Searching for... Whois Lookup: {getTargetWebsite}")
    time.sleep(2)
    command = "whois " + getTargetWebsite
    informattionProcess = os.popen(command)
    results = str(informattionProcess.read())
    print(f"{results}Search complete [{command}]")
# if Username and Password wrong
else:
    print("Wrong Information. Please try Again later.")
