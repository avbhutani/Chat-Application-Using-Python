import classes.users as users
import classes.message as message
import os
import classes.messages as messages
import classes.dataBaseHandler as dataBaseHandler
# Importing the necessary modules.

user1 = input("Enter sender: ")

user2 = input("Enter receiver: ")

messageAdmin = messages.Messages(user1,user2)

while(True):
    msg = input("Enter message: ")
    if(msg == "!q"):
        break
    
    if(msg != ""):
        messageObj = messageAdmin.createMessage(msg)
        
        # Checking if the database is empty.
        check_file = os.stat("database/chatHistory.txt").st_size 
        
        # If it is not empty, then fetch all the messages currently in the file.
        if(check_file != 0):
            fetchedList = messageAdmin.returnDataBaseContent("database/chatHistory")
        else:
            fetchedList = []
        # Else create an empty list.
        
        # Now update the fetched list with the current message.
        updatedList = messageAdmin.updateMessageList(messageObj,fetchedList)
        
        # Update the database with the updated list.
        messageAdmin.updateDataBaseContent(updatedList,'database/chatHistory')
    
    # Filter all the messages from the list for the sender to receiver as well as receiver to sender.
    finalList = messageAdmin.chatBetween(user1,user2,fetchedList)

    # Print all the required messages.
    for i in finalList: 
        print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
        print("\n")
        
print("The program ended successfully!")