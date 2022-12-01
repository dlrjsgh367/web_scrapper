import functools
from threading import Thread
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

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
            print("ret 타입", type(ret))
            if isinstance(ret, BaseException):
                print("오류 발생")
                raise ret
            return ret
        return wrapper
    return deco

@timeout(10)
def url_request(url:str) -> BeautifulSoup:
    '''
    url을 입력받으면 html을 출력해주는 함수입니다.
    '''

    response = urlopen(url)
    return response