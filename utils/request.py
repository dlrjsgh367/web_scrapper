import functools
from threading import Thread
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pickle
import os
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
                    print("오류발생")
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
                print("오류 발생")
                raise ret
            return ret
        return wrapper
    return deco

@timeout(10)
def url_request(url:str, dir=None):
    '''
    url을 입력받으면 html을 출력해주는 함수입니다.
    '''

    response = urlopen(url)
    if response.status == 200:
        print("정상 응답")
        if dir is None:
            return response
        else:
            soup = BeautifulSoup(response, 'html.parser')
            file_name = dir.split('\\')[-1]
            file_dir = '\\'.join(dir.split('\\')[:-1])
            if file_name in os.listdir(file_dir):
                print(f"{file_name} 은 이미 저장 되어있습니다.")
            else:
                with open(dir, 'wb') as fw:    
                    pickle.dump(soup, fw)
                    print(f"{file_name} 을 정상적으로 저장했습니다.")
    return response
