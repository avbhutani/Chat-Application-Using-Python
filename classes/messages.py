import pickle
# Pickle module is used for serialization and deserialization

class Messages:
    def __init__(this):
        this.chatHistory = []

    # Method to update the current message list.
    def updateMessageList(this,msg,fetchedMessageList):
        fetchedMessageList.append(msg)
        return fetchedMessageList
    
    # Method to update the database.
    def updateDatabase(this,chatHistory):
        with open('database/chatHistory.txt','wb') as outfile:
            pickle.dump(chatHistory,outfile)
    
    # Method to get the message list
    def getMessageList(this):
        if(this.chatHistory):
            return this.chatHistory
        
    def printChatHistory(this):
        print(this.chatHistory)
        
    # Method to filter the chat between the sender and the receiver.
    def chatBetween(this,user1,user2,fetchedMessageList):
        filteredObjs = []
        # with open('chatHistory.txt','rb') as infile:
        #         chatHistoryFile = pickle.load(infile)
        for i in fetchedMessageList:
            if((i.getSender() == user1 and i.getReceiver() == user2) or (i.getSender() == user2 and i.getReceiver() == user1)):
                filteredObjs.append(i)
        return filteredObjs
    
    # Used to fetch the list already in the database. 
    def fetchDatabase(this):
        try:
            with open('database/chatHistory.txt', 'rb') as file:
                existing_list = pickle.load(file)
            return existing_list
        except FileNotFoundError:
            return []