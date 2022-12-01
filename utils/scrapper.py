
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import pickle
import sys
sys.setrecursionlimit(10000)
import os
from utils.util import *
from utils.request import *

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

def save(request):
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
        pickle.dump(request, fw)    

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
        # if response not in url_review_page_list:
        #     url_review_page_list.append(response)
            
            # test = list(map(lambda x: ', '.join(x[0],x[1]), test))
            # test = '\n'.join(test)
        # review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))
        #find_all : 지정한 태그의 내용을 모두 찾아 리스트로 반환
        reviews = soup.find_all("td",{"class":"title"})
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
        pickle_name = page
        pickle_name = str(pickle_name)
        time.sleep(0.5)
        break
    if mcode not in mcode_save:
        mcode_save = mcode
        mcode_save = str(mcode_save)
    save(response)
    mcode_list()
    review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))     #result = "\n".join(map(str, review_data))
    review_data = '\n'.join(review_data)                                            #with open(f'{movie}.txt', 'w', encoding="UTF-8") as fw:
    with open(f'{work_dir}/{mcode_save}/review.txt', "w", encoding="utf8") as f:                            #fw.write(result)
        f.write(str(review_data))