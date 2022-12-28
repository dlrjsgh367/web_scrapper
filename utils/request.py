from urllib.request import urlopen
import functools
from threading import Thread
import pickle
import os
import logging
import argparse

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser()
parser.add_argument("-f","--fdname",type=str,help="폴더 이름을 정합니다.")
args = parser.parse_args()

def timeout(timeout):
    '''
    timeout 데코레이터를 설정해주고, 메서드 실행시간이 지정한 시간을 지나면 raise를 통해 강제로 에러를 발생시켜 pass 해줍니다.
    url_request 함수에 데코레이터로 timeout 10초를 걸어주고, request(실행시간) 10초가 넘으면 에러를 발생 시켜 pass 합니다.
    '''
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]
            # 모든 timeout 데코레이터 사용한 메서드에 res 초기값을 error로 초기화
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                    #res[0] : api 데이터, 메서드를 실행시켜서 값을 저장
                except Exception as e:
                    res[0] = e
                    print("res[0] except", res[0]) #함수 자체가 실행이 안 되는 오류 처리
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print ('error starting thread')
                raise je
            ret = res[0]
            # print("ret", ret)
            #print("ret 타입", type(ret))
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

def url_bs4(url:str, dir=None):
    '''
    파라미터를 2개 받는데, 첫번째는 url, 2번째는 dir(경로)입니다. 아래 나오는 scrapper에서 사용됩니다.

    file_name : dir을 "/" 기준으로 나눠서 맨 마지막에 있는 dir을 의미합니다.
    "/" 기준으로 나눈 dir의 맨 마지막에 있는것은 pickle_name 입니다.
    pickle_name은 scrapper에 있는 save_dir에서 확인할수 있습니다.
    
    file_dir : 맨 마지막 dir을 제외하고 모든 dir을 "/" 기준으로 나눈뒤 "/" 가 있는 dir끼리 합칩니다. 
    file_dir의 값은 data_dir/today/mcode/HTML_Folder/pickle_name에서
    맨 마지막 dir을 제외 했으니 data_dir/today/mcode/HTML 이 되겠습니다. 
    '''
   
    # test = "test.txt"

    
    dir = dir.replace("\\", "/")
    file_name = dir.split('/')[-1]
    file_dir = '/'.join(dir.split('/')[:-1])
    # picke_url_or_dir = '/'.join(dir.split('/')[:-3])
    if file_name in os.listdir(file_dir):
        with open(dir, 'rb') as fr: #######################################################################
            soup = pickle.load(fr)
        logger.info(f"이미 저장된 {file_name} 을 불러왔습니다.")
        # print(f"이미 저장된 {file_name} 을 불러왔습니다.")
        # with open(f"{picke_url_or_dir}/pickle_url_or_dir.txt", "w", encoding="UTF-8") as f:
        #         f.write(str([url,dir]))
        #         logger.info("pickle 파일의 url과 dir을 저장했습니다.")
    else:
        try:
            response = url_request(url) #url_request 사용됨 .
        except Exception as e:
            # logging.warning(e)
            logger.warning(e)
            return

        soup = BeautifulSoup(response,'html.parser')
        if dir is None:
            return soup
        else:
            with open(dir, 'wb') as fw:    #######################################################################
                pickle.dump(soup, fw)
                # print(f"{file_name} 을 정상적으로 저장했습니다.")
                # logging.info(f"{file_name} 을 정상적으로 저장했습니다.")
                logger.info(f"{file_name} 을 정상적으로 저장했습니다.")
                pickle_url_dir(url, dir)
            # with open(f"{picke_url_or_dir}/pickle_url_or_dir.txt", "w", encoding="UTF-8") as f:
            #     f.write(str([url,dir]))
            #     logger.info("pickle 파일의 url과 dir을 저장했습니다.")
        return soup

@timeout(10)
def url_request(url):
    '''
    웹 사이트에 리퀘스트를 보내 정상값(200)이면
    logging.info("정상 응답")

    함수 동작이 끝나면 response 값을 return합니다.

    url_request 함수는 url_bs4 함수에 사용되었습니다.
    '''
    response = urlopen(url)
    if response.status == 200:
        # logging.info("정상 응답")
        logger.info("정상 응답")
    #elif response.status == .


    return response
print(urlopen)
    

def pickle_url_dir(url:str, dir=None):
    dir = dir.replace("\\", "/")
    picke_url_or_dir = '/'.join(dir.split('/')[:-3])
    with open(f"{picke_url_or_dir}/pickle_test.txt", "a", encoding="utf8") as f:
        list1 = []
        list1.append(([url,dir]))
        # list1 = list(map(lambda x: ', '.join([str(x)]), list1)) 
        list1 = list(map(lambda x: ', '.join([str(x[0]),x[1]]), list1)) 
        list1 = '\n'.join(list1)  
        # list1 = list(map(lambda x: ', '.join([str(x[0]),x[1]])), list1) 
        f.write(str(list1) + "\n")
        
        # a = (url,dir)
        #     # a = list(map(lambda x: './'.join([str(x[0]),x[1]]), a)) 
        # a = a.strip("./")
        # a = '\n'.join(a)  

        # f.write(str(a))
        # f.write(dir+ "\n")
        logger.info("txt 저장댐")

