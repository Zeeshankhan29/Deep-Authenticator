import pymongo
from dotenv import load_dotenv
import os
from face_auth.constants import MONGODB_URL,DATABASE_NAME,COLLECTION_NAME
load_dotenv()



class Mongodbclient:
    def __init__(self,DATABASE_NAME:str,COLLECTION_NAME:str):
        # if 'localhost' in MONGODB_URL:
            self.client = pymongo.MongoClient(MONGODB_URL)
            self.database = DATABASE_NAME
            self.collection = COLLECTION_NAME




    def connection(self):
        database = self.client[self.database]
        collection = database[self.collection]

        return collection.insert_one({'interview':'Pass1'})
    


if __name__=='__main__':
    ob = Mongodbclient(DATABASE_NAME,COLLECTION_NAME)
    ob.connection()