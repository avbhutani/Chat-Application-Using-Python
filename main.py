# This is a username validation system in python, it will accept all the username in any case
# The username can consist of the symbols '_' or '.' and any other symbol includance will be considered as an invalid username.

# We have included the function in another file named  "functions.py" and then we will use the function included in that file in our current file.
# The functions folder will be used as an object and the functions contained in it can be used as the methods and the arguements can be directly passed to it.
import functions
username = input("Enter the username\n").lower()

# The below line will raise an exception if the username is empty.
if (not username):
    raise Exception("Username can't be empty")

username_validation = functions.checkValidUsername(username)

if(username_validation):
    print("Valid Username")
else:
    print("Not a valid Username")