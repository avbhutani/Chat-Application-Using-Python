import uuid,time

class Message:
    # Add the sender and receiver for each message in each class.
    def __init__(this,sender,receiver):
        this.messageId = uuid.uuid1()
        this.timeStamp = time.time()
        this.sender = sender
        this.receiver = receiver
        
    def setMessage(this,msg):
        this.msg = msg

    def getSender(this):
        return this.sender
    
    def getReceiver(this):
        return this.receiver
    
    def getTimeStamp(this):
        return this.timeStamp
    
    def getMessageId(this):
        return this.messageId
     