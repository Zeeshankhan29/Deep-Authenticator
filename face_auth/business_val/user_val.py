import re
import sys
from typing import Optional
from face_auth import logging
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')




class Loginvalidation:
    def __init__(self,email_id:str,password:str):
        self.email = email_id
        self.password = password
        self.pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"



    def validate(self):
        try:
            msg=''
            if self.email == '':
                msg += 'Email Id not provided!!!!'

            if self.password == '':
                msg += 'Password not provided!!!'

            if not self.email_valid():
                msg += 'Email is not Valid!!!'
            return msg

        except Exception as e:
            logging.exception(e)
    
    def email_valid(self) -> bool:
        try:
            if re.findall(self.pattern,self.email):
                logging.info('Email is valid')
                return True
        
            else:
                logging.info('Email is not valid')
                return False
        except Exception as e:
            logging.exception(e)



    def validate_login(self):
        try:
            if len(self.validate())!=0:
                return {'status':True,'msg':self.validate}
            
            return False

        except Exception as e:
            logging.exception(e)



    def verify_password(self,plain_password:str,hashed_password:str)->bool:
        try:
            bcrypt_context.verify(plain_password,hashed_password)

        except Exception as e:
            logging.exception(e)



    




if __name__=='__main__':
    ob = Loginvalidation('llkj@gmail.yahoo',256)
    ob.email_valid()







