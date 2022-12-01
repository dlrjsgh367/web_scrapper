from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import pickle
import sys
sys.setrecursionlimit(10000)
import functools
from threading import Thread
import datetime
import os
import sys


# s = datetime.datetime.now()
# print(s)
# s = "%04d-%02d-%02d %02:%02d:%02d" % (now.tm_year, now.tm_mon
    # , now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

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
    

    

# root_dir = "C:/Users/HAMA/code/web_scrapper/data"
# today = get_today()
# work_dir = root_dir + "/" + today


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


def mcode_list():
    """
    네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수입니다.
    """
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?&page=1')
    soup = BeautifulSoup(url, 'html.parser')
    soup = soup.select('#current_movie > option')
    line = []
    root_dir = "C:/Users/HAMA/code/web_scrapper/data"
    today = get_today()
    work_dir = root_dir + "/" + today 
    os.makedirs(work_dir, exist_ok=True)
    mcode_name = "mcode.txt"
    today = get_today
    for val in soup:
        code = val.get('value')
        if code is not None:
            # name = val.text
            line.append(code) #line.append([code,name])
    # line = list(map(lambda x: ' : '.join([str(x[0]),x[1]]), line))
    # make_folder(work_dir)
    line = "\n".join(line)
    with open(f"{work_dir}/{mcode_name}", "w", encoding="utf-8") as fw:
        fw.write(str(line))

# mcode_list()

# def save():
#     '''
#     지정한 영화의 모든 리뷰페이지의 html을 bs4 객체로 받아서 "@@".pickle 폴더에 저장하는 함수입니다.
#     '''
#     url = urlopen('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=49948&target=after')
#     soup = BeautifulSoup(url, 'html.parser')
#     with open('list.pickle', 'wb') as fw:
#         pickle.dump(soup, fw)

def save(bs4):
    '''
    지정한 영화의 모든 리뷰페이지의 html을 bs4 객체로 받아서 "@@".pickle 폴더에 저장하는 함수입니다.
    '''
    root_dir = "C:/Users/HAMA/code/web_scrapper/data"
    today = get_today()
    HTML_Folder = "HTML"
    work_dir = root_dir + "/" + today + "/" + mcode_save + "/" + HTML_Folder
    
    # os.makedirs(work_dir, exist_ok=True)
    # os.makedirs(pickle_name, exist_ok=True)
    make_folder(work_dir)
    # bs4name = url_request
    
    with open(f'{work_dir}/{pickle_name}.pickle', 'wb') as fw:    
        pickle.dump(bs4, fw)    
        #        데이터 폴더/날짜/영화제목코드폴더/HTML/피클저장
@timeout(10)
def url_request(url:str) -> BeautifulSoup:
    '''
    url을 입력받으면 html을 출력해주는 함수입니다.
    '''
    response = urlopen(url)
    return response

# url_request("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=49945&target=after&page=300")

def parsing(mcode):
    url_review_page_list = []
    global mcode_save
    mcode_save = []
    global pickle_name
    page = 1
    review_data = []
    root_dir = "C:/Users/HAMA/code/web_scrapper/data"
    today = get_today()
    work_dir = root_dir + "/" + today        
    while True:
        url_review_page = f"https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={mcode}&target=after&page={page}"
        response = url_request(url_review_page)
        soup = BeautifulSoup(response,'html.parser')
        if url_review_page not in url_review_page_list:
            url_review_page_list.append(url_review_page)
            # test = list(map(lambda x: ', '.join(x[0],x[1]), test))
            # test = '\n'.join(test)
        # review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))
        #find_all : 지정한 태그의 내용을 모두 찾아 리스트로 반환
        reviews = soup.find_all("td",{"class":"title"})
        # if reviews == "":
        #     print("작성된 리뷰가 없습니다.")
        #     break
        for review in reviews:
            sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
            
            if sentence != "":
                # global movie  
                # movie =  review.find("a",{"class":"movie color_b"}).get_text()
                score = review.find("em").get_text()
                review_data.append([int(score),sentence])
           
                
        finall = soup.select_one("#old_content > div.paging > div > a.pg_next")
        if finall is None:
            break
        
        page += 1
        # url_review_page + str(page)
        
        pickle_name = page
        pickle_name = str(pickle_name)
        time.sleep(0.5)
        # break
    if mcode not in mcode_save:
        mcode_save = mcode
        mcode_save = str(mcode_save)
    save(url_review_page_list)
    mcode_list()
    review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))     #result = "\n".join(map(str, review_data))
    review_data = '\n'.join(review_data)                                            #with open(f'{movie}.txt', 'w', encoding="UTF-8") as fw:
    with open(f'{work_dir}/{mcode_save}/review.txt', "w", encoding="utf8") as f:                            #fw.write(result)
        f.write(str(review_data))
# parsing(195973)

# print(time.time())
# 이포크타임이 UTC 타임인가, 로컬타임인가 알아보세요 UTC타임
# 로컬타임과 UTC타임의 차이점
# UTC  1972년 1월 1일부터 시행된 국제 표준시이며, 1970년 1월 1일 자정을 0 밀리초로 설정하여 기준을 삼아 그 후로 시간의 흐름을 밀리초로 계산한다.
# 로컬 현지시각
#old_content > div.paging > div > span
#old_content > div.paging > div > a.pg_next

# currentpath = os.getcwd() 현재 경로 알려주는거
# print(currentpath)





with open(f"C:/Users/HAMA/code/web_scrapper/data/2022-12-01/{mcode_save}/HTML/{pickle_name}.pickle","rb") as fr:
    data = pickle.load(fr)
print(data)













