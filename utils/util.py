import os
import time



def get_time():
    now = time.localtime()
    s = "%04d-%02d-%02d %02d시%02d분" % (now.tm_year, now.
        tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    return s

def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s


def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)    