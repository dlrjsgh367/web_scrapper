from urllib.request import urlopen
import functools
from threading import Thread
import pickle
import os
import logging

from bs4 import BeautifulSoup



def timeout(timeout):
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
    url을 입력받으면 html을 출력해주는 함수입니다.
    '''
    file_name = dir.split('/')[-1]
    file_dir = '/'.join(dir.split('/')[:-1])
    if file_name in os.listdir(file_dir):
        with open(dir, 'rb') as fr:
            soup = pickle.load(fr)
        # print(f"이미 저장된 {file_name} 을 불러왔습니다.")
        logging.info(f"이미 저장된 {file_name} 을 불러왔습니다.")
    else:
        try:
            response = url_request(url)
        except Exception as e:
            logging.warning(e)
            return

        soup = BeautifulSoup(response,'html.parser')
        if dir is None:
            return soup
        else:
            with open(dir, 'wb') as fw:    
                pickle.dump(soup, fw)
                # print(f"{file_name} 을 정상적으로 저장했습니다.")
                logging.info(f"{file_name} 을 정상적으로 저장했습니다.")
    return soup

@timeout(10)
def url_request(url):
    response = urlopen(url)
    if response.status == 200:
        logging.info("정상 응답")
    #elif response.status == .


    return response


print(urlopen)
    # 세이브로드는 리퀘스트를 조금하려고 쓰는것이니
    # 지금 코드에서 파일이 이미 있는 경우 리퀘스트하지않고 피클로드하도록 바꾸면 됩니다.

