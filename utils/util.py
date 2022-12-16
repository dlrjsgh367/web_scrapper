
import time
import logging
import os

def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s



def make_folder(*dir):
    folder_dir = os.path.join(*dir)
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)
        logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 폴더가 생성되었습니다.\n")
    else:
        logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 는 이미 존재하는 폴더입니다.\n")
        

            


    
    