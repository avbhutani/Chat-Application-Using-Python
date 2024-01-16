class User:
    def __init__(this,username):
        if(this.checkValidUsername(username)):
            this.initialize(username)
        this.data = dict()
         
    def initialize(this,username):
        this.username = username

    def setDetails(this,key,value):
        if(this.username):
            this.data[key] = value
        
    def getUsername(this):
        return this.username
    
    def getDetails(this):
        if this.username:
            return this.data

    def checkValidUsername(this,username):
        arr = ['_','.','1','2','3','4','5','6','7','8','9','0']
        underscore_count = 0
        username = username.lower()
        for i in username:
            ascii_value = ord(i)
            if(i == '_'):
                underscore_count += 1
            if((i not in arr and ascii_value not in range(97,122)) or underscore_count>2):
                return False
             
        return True