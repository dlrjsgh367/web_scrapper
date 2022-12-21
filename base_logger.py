import logging


logger = logging
logger.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

mylogger = logging.getLogger("my")
mylogger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)

file_handler = logging.FileHandler('my.log')
mylogger.addHandler(file_handler)


logger.info('')