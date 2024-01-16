import pickle

class DatabaseHandler:
    def fetchDatabase(this,path):
        try:
            with open(path + '.txt', 'rb') as file:
                existing_list = pickle.load(file)
            return existing_list
        except FileNotFoundError:
            return []
    
    def updateDatabase(this,arguementList,path):
        with open(path+ '.txt','wb') as outfile:
            pickle.dump(arguementList,outfile)