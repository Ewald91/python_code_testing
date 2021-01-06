import logging
from datetime import datetime

logger = logging.getLogger() #provide '__name__' to getLogger for only logs from this module
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s')

now = datetime.now()
file_handler = logging.FileHandler(f'logs/app/{now.strftime("%d%m%Y")}logic.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter) 
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

