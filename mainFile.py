import classes.users as users
import classes.message as message
import os
import classes.messages as messages
# Importing the necessary modules.

admin = users.Users()
user1 = input("Enter sender: ")
user2 = input("Enter receiver: ")
# Adding details of the sender and the reeciver and adding them as a user.
admin.addUser(user1)
admin.addUser(user2)

# Creating the message Admin to perform all the "Messages" class task
messageAdmin = messages.Messages()

while(True):
    # Taking the input from the user
    msg1 = message.Message(user1,user2)
    
    # Checking if the database is empty.
    check_file = os.stat("database/chatHistory.txt").st_size 
    
    # If it is not empty, then fetch all the messages currently in the file.
    if(check_file != 0):
        fetchedList = messageAdmin.fetchDatabase()
    else:
        fetchedList = []
    # Else create an empty list.
    
    # Now update the fetched list with the current message.
    updatedList = messageAdmin.updateMessageList(msg1,fetchedList)
    
    # Update the database with the updated list.
    messageAdmin.updateDatabase(updatedList)
    
    # Filter all the messages from the list for the sender to receiver as well as receiver to sender.
    finalList = messageAdmin.chatBetween(user1,user2,fetchedList)

    # Print all the required messages.
    for i in finalList: 
        print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
        print("\n")