import os
import logging
import sys


logs_dir ='logs'

os.makedirs(logs_dir,exist_ok=True)
log_path = os.path.join(logs_dir,'running_logs.log')



logging.basicConfig(level=logging.INFO,format=('[%(asctime)s] : [%(name)s] : [%(levelname)s] : [%(message)s]'),
                    handlers=[logging.FileHandler(log_path)
                              ,logging.StreamHandler(sys.stdout)])