import classes.message as message
import classes.users as users
import classes.dataBaseHandler as dataBaseHandler
usersAdmin = users.Users()
dataBaseAdmin = dataBaseHandler.DatabaseHandler()
class Messages:
    def __init__(this,sender,receiver):
        this.chatHistory = []
        this.sender = sender
        this.receiver = receiver
        usersAdmin.addUser(sender)
        usersAdmin.addUser(receiver)
        
    def returnDataBaseContent(this,path):
        dataBaseAdmin = dataBaseHandler.DatabaseHandler()
        return dataBaseAdmin.fetchDatabase(path)
        
    def updateDataBaseContent(this,arguementList,path):
        dataBaseAdmin = dataBaseHandler.DatabaseHandler()
        dataBaseAdmin.updateDatabase(arguementList,path)
    
    def createMessage(this,msg):
        m = message.Message(this.sender,this.receiver)
        m.setMessage(msg)
        return m
        
    def updateMessageList(this,msg,fetchedMessageList):
        fetchedMessageList.append(msg)
        return fetchedMessageList
    
    def getMessageList(this):
        if(this.chatHistory):
            return this.chatHistory
        
    def chatBetween(this,user1,user2,fetchedMessageList):
        filteredObjs = []
        for i in fetchedMessageList:
            if((i.getSender() == user1 and i.getReceiver() == user2) or (i.getSender() == user2 and i.getReceiver() == user1)):
                filteredObjs.append(i)
        return filteredObjs