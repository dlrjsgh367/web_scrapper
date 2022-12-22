
import time
import logging
import os

logger = logging.getLogger(__name__)

def get_today():
    '''
    설명 : 오늘날짜를 리턴하는 함수입니다.
    '''
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s

def get_today2():
    '''
    설명 : 오늘날짜를 리턴하는 함수입니다.
    '''
    now = time.localtime()
    s = "%04d-%02d-%02d %02dː%02dː%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return s




def make_folder(*dir):
    '''
    설명 : 폴더를 생성하는 함수입니다. 폴더 생성을 성공하면 폴더가 생성되었다고 출력
    이미 폴더가 생성 되어있다면 이미 존재하는 폴더인것만 알려주고 다른 동작은 취하지 않습니다.
    '''
    folder_dir = os.path.join(*dir)
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)
        logger.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 폴더가 생성되었습니다.\n")
        # logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 폴더가 생성되었습니다.\n")

    else:
        logger.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 는 이미 존재하는 폴더입니다.\n")
        # logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 는 이미 존재하는 폴더입니다.\n")
        

            


    
    