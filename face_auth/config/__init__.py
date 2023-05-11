import pymongo
from dotenv import load_dotenv
import os
from face_auth.constants import MONGODB_URL,DATABASE_NAME,COLLECTION_NAME
load_dotenv()
from face_auth import logging



class Mongodbclient:
    client = pymongo.MongoClient(MONGODB_URL)
    def __init__(self,DATABASE_NAME:str,COLLECTION_NAME:str):
            self.database = DATABASE_NAME
            self.collection = COLLECTION_NAME




    def Mongodbconnection(self):
       client = Mongodbclient.client
       database = client[self.database]
       collection = database [self.collection]
       return collection

    def get_user_data(self, query):
        collection = self.Mongodbconnection()
        data = collection.find_one({'interveiw1': str(query)})
        if data:
            print(data)
        else:
            print("No data found.")
        

        
    


if __name__=='__main__':
    ob = Mongodbclient(DATABASE_NAME,COLLECTION_NAME)
    ob.get_user_data('Pass1')