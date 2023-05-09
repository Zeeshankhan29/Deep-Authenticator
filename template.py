from pathlib import Path
import os
import sys
import logging

logs_dir ='logs'

os.makedirs(logs_dir,exist_ok=True)
log_path = os.path.join(logs_dir,'running_logs.log')



logging.basicConfig(level=logging.INFO,format=('[%(asctime)s] : [%(name)s] : [%(levelname)s] : [%(message)s]'),
                    handlers=[logging.FileHandler(log_path)
                              ,logging.StreamHandler(sys.stdout)])

                    

files =[

'controller/__init__.py',
'controller/app_controller/__init__.py',
'controller/auth_controller/__init__.py',
'face_auth/__init__.py',
'face_auth/business_val/__init__.py',
'face_auth/config/__init__.py',
'face_auth/data_access/__init__.py',
'face_auth/entity/__init__.py',
'face_auth/exception/__init__.py',
'face_auth/logger/__init__.py',
'face_auth/utils/__init__.py',



]


for filepath in files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory :{filedir} for file:{filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating filepath :{filepath}")

    else:
        logging.info(f"{filename} already exists")


