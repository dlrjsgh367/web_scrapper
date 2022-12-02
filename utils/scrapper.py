
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import sys
sys.setrecursionlimit(10000)
import os
from utils.util import get_today, save, make_folder
from utils.request import url_request

def parsing_mcode_list():
    """
    네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수입니다.
    """
    # 디렉토리 설정
    data_dir = "./data"
    today = get_today()
    make_folder(os.path.join(data_dir,today))
    
    # url 요청
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?&page=1')
    soup = BeautifulSoup(url, 'html.parser')

    # 파싱
    soup = soup.select('#current_movie > option')
    mcode_list = []
    for val in soup:
        code = val.get('value')
        if code is not None:
            mcode_list.append(code) #line.append([code,name])
    mcode_list_str = "\n".join(mcode_list)

    # 파싱 결과 저장
    mcode_name = "mcode.txt"
    with open(os.path.join(data_dir,today,mcode_name), "w", encoding="utf-8") as fw:
        fw.write(str(mcode_list_str))
    return mcode_list
    

def parsing_reviews(mcode):
    '''
    지정한 영화코드의 모든 리뷰페이지를 가져오는 함수입니다.
    '''
    page = 1
    review_data = []
    data_dir = "C:/Users/HAMA/code/web_scrapper/data"
    today = get_today()
    
    # 어떤 영화(mcode)의 모든 리뷰페이지 가져오기
    while True:
        # url 요청
        url_review_page = f"https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={mcode}&target=after&page={page}"
        response = url_request(url_review_page)
        save(response.read(),mcode, page)
        soup = BeautifulSoup(response,'html.parser')
        # 파싱
        reviews = soup.find_all("td",{"class":"title"})
        for review in reviews:
            sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
            if sentence != "":
                # movie =  review.find("a",{"class":"movie color_b"}).get_text()
                score = review.find("em").get_text()
                review_data.append([int(score),sentence])
        finall = soup.select_one("#old_content > div.paging > div > a.pg_next")

        # 만약에 파싱후 얻을 내용이 없는 경우(맨 마지막 페이지의 경우) break
        if finall is None:
            break

        # 잠시 쉬고 다음페이지로 넘어가기
        time.sleep(0.5)
        page += 1

    # 얻은 리뷰를 저장
    review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))   
    review_data = '\n'.join(review_data)
    with open(os.path.join(data_dir,today,mcode,'review.txt'), "w", encoding="utf8") as f:
        f.write(str(review_data))