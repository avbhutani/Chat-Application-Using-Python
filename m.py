import redis
import classes.messages as messages
import threading
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
user1 = input("Enter sender: ")
user2 = input("Enter receiver: ")
m = True
messageAdmin = messages.Messages(user1, user2)

# Lock for synchronizing console printing
print_lock = threading.Lock()

def checkForUpdates():
    while True:
        file = 'database/flagfile.txt'
        search_string = "True"
        with open(file) as f:
            if search_string in f.read():
                check_file = messageAdmin.checkFileStatus("database/chatHistory.txt")

                if check_file != 0:
                    fetchedList = messageAdmin.returnDataBaseContent("database/chatHistory")
                else:
                    fetchedList = []

                if check_file != 0:
                    finalList = messageAdmin.chatBetween(user1, user2, fetchedList)

                print("\n")
                for i in finalList:
                    print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
                    print("\n")
                print("Enter message: ")
                m = False
                with open(file, 'w') as f:
                    f.write("False")

# Create and start the thread for checking updates
thread_check_updates = threading.Thread(target=checkForUpdates)
thread_check_updates.daemon = True
thread_check_updates.start()

while True:
    print("\n")
    with print_lock:
        msg = input("Enter message: ")
    if msg == "!q":
        break

    if msg != "":
        messageObj = messageAdmin.createMessage(msg)
        check_file = messageAdmin.checkFileStatus("database/chatHistory.txt")

        if check_file != 0:
            fetchedList = messageAdmin.returnDataBaseContent("database/chatHistory")
        else:
            fetchedList = []

        updatedList = messageAdmin.updateMessageList(messageObj, fetchedList)
        messageAdmin.updateDataBaseContent(updatedList, 'database/chatHistory')

        check_file = messageAdmin.checkFileStatus("database/chatHistory.txt")
        if check_file != 0:
            finalList = messageAdmin.chatBetween(user1, user2, fetchedList)

            with print_lock:
                for i in finalList:
                    print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
                    print("\n")

        m = True
        with open('database/flagfile.txt', 'w') as f:
            f.write("True")

print("The program ended successfully!")
