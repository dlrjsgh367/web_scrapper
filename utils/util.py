import os
import time
import pickle


def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s



def make_folder(*dir):
    folder_dir = os.path.join(*dir)
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)
        print(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 폴더가 생성되었습니다.\n")
    else:
        print(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 는 이미 존재하는 폴더입니다.\n")

def save(request, mcode, pickle_name):
    '''
    지정한 영화의 모든 리뷰페이지의 html을 bs4 객체로 받아서 "@@".pickle 폴더에 저장하는 함수입니다.
    '''
    data_dir = "./data"
    today = get_today()
    HTML_Folder = "HTML"
    pickle_name = f'{pickle_name}.pickle'
    make_folder(data_dir,today,mcode,HTML_Folder)
    print(f"{mcode}의 리뷰페이지를 {data_dir}/{today}/{mcode}/{HTML_Folder} 에 가져오고 있습니다")
    if pickle_name in os.listdir(os.path.join(data_dir,today,mcode,HTML_Folder)):
        print(f"{pickle_name} 은 이미 저장 되어있습니다.")
    else:
        with open(os.path.join(data_dir,today,mcode,HTML_Folder,pickle_name), 'wb') as fw:    
            pickle.dump(request, fw)    
            print(f"{pickle_name} 을 정상적으로 저장했습니다.")
    
    

    
    