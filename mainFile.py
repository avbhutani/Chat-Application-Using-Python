import classes.messages as messages
import threading

user1 = input("Enter sender: ")
user2 = input("Enter receiver: ")
messageAdmin = messages.Messages(user1, user2)
m = True
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

                for i in finalList:
                    print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
                    print("\n")

                with open(file, 'w') as f:
                    f.write("False")
                m = False

def main():
    thread_check_updates = threading.Thread(target=checkForUpdates)
    thread_check_updates.start()

    while True:
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

                    for i in finalList:
                        print(i.getSender() + " > " + i.getReceiver() + " : " + i.msg)
                        print("\n")

                with open('database/flagfile.txt', 'w') as f:
                    f.write("True")

    print("The program ended successfully!")

if __name__ == "__main__":
    main()