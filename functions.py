def checkValidUsername(username):
    arr = ['_','.']
    underscore_count = 0
    username = username.lower()
    for i in username:
        ascii_value = ord(i)
        if(i == '_'):
            underscore_count += 1
        if((i not in arr and ascii_value not in range(97,122)) or underscore_count>2):
           return False
        
    return True

# The function will return 1 or 0, based on whether the username is valid or not