from face_auth.config import Mongodbclient
from face_auth.constants import COLLECTION_NAME ,DATABASE_NAME


class UserData:
    def __init__(self,query) -> None:
        self.client = Mongodbclient(DATABASE_NAME,COLLECTION_NAME)
        self.query = query
    

    def connection_check(self):
        return self.client.Mongodbconnection()
    

    def user_data(self):
        self.client.get_user_data(query=self.query)

     


if __name__ =='__main__':
    ob = UserData({'interview':'Pass'})
    ob.user_data()