import classes.user as user
import classes.databasehandler as dataBaseHandler
dbAdmin = dataBaseHandler.DatabaseHandler()

class Users:
    def __init__(this):
        this.userList = []
        
    def addUser(this,username):
        temp_user = user.User(username)
        if((temp_user.checkValidUsername(username) )and (not this.checkExistence(username))):
            this.userList.append(temp_user)
            dbAdmin.updateDatabase(this.userList,"database/usersList") 
            
    def removeUser(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                this.userList.remove(i)
                dbAdmin.updateDatabase(this.userList,"database/usersList")
                
    def fetchUser(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                return i
        return -1        
        
    def updateUserDetails(this,username,key,value):
        temp_user = user.User(username)
        for i in this.userList:
            if(i== username):
                temp_user.setDetails(key,value)
                dbAdmin.updateDatabase(this.userList,"database/usersList")
                   
    def checkExistence(this,username):
        for i in this.userList:
            if(i.getUsername() == username):
                return True
        return False