import os
import time
import pickle



def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s


def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)    

def save(request, mcode, pickle_name):
    '''
    지정한 영화의 모든 리뷰페이지의 html을 bs4 객체로 받아서 "@@".pickle 폴더에 저장하는 함수입니다.
    '''
    data_dir = "./data"
    today = get_today()
    HTML_Folder = "HTML"
    pickle_name = f'{pickle_name}.pickle'
    make_folder(os.path.join(data_dir,today,mcode,HTML_Folder))
    with open(os.path.join(data_dir,today,mcode,HTML_Folder,pickle_name), 'wb') as fw:    
        pickle.dump(request, fw)    