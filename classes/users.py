import classes.user as user
import pickle

class Users:
    def __init__(this):
        this.userList = []
        
    # Method to add a new user to the list, checking if the user is not already there and if the username is valid, then add.
    def addUser(this,username):
        temp_user = user.User(username)
        if((temp_user.checkValidUsername(username) )and (not this.checkExistence(username))):
            this.userList.append(temp_user)
            with open('database/usersList.txt','wb') as outfile:
                pickle.dump(this.userList,outfile)
            
    def removeUser(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                this.userList.remove(i)
                with open('database/usersList.txt','wb') as outfile:
                    pickle.dump(this.userList,outfile)

    def updateUserDetails(this,username,key,value):
        temp_user = user.User(username)
        for i in this.userList:
            if(i== username):
                temp_user.setDetails(key,value)
                with open('database/usersList.txt','wb') as outfile:
                    pickle.dump(this.userList,outfile)
                  
    def showAllUsers(this):
        for i in this.userList:
            print(i.username)

    def checkExistence(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                return True
        return False
    
    def fetchUser(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                return i
        return -1