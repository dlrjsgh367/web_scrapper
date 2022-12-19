
import time
import sys
sys.setrecursionlimit(10000)
import os
import logging
from urllib.request import urlopen

from bs4 import BeautifulSoup

from utils.request import url_bs4
from utils.util import get_today, make_folder


def parsing_mcode_list():
    """
    네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수입니다.
    # 파싱 에서 soup은 select 메소드를 이용하여 현재상영중인 영화목록의 select를 가져온것입니다.
    """
   
    # 디렉토리 설정
    data_dir = "./data"
    today = get_today()
    make_folder(data_dir,today)
    
    # url 요청
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?&page=1')
    soup = BeautifulSoup(url, 'html.parser')

    # 파싱
    soup = soup.select('#current_movie > option')
    mcode_list = []
    for val in soup:
        code = val.get('value')
        if code is not None:
            mcode_list.append(code)
    mcode_list_str = "\n".join(mcode_list)
    # 파싱 결과 저장
    mcode_name = "mcode.txt"
    with open(os.path.join(data_dir,today,mcode_name), "w", encoding="utf-8") as fw:
        fw.write(str(mcode_list_str))
    return mcode_list
    

def parsing_reviews(mcode):
    '''
    지정한 영화코드의 모든 리뷰페이지를 파싱하는 함수입니다.
    '''
    
    page = 1
    review_data = []
    data_dir = "./data"
    today = get_today()
    HTML_Folder = "HTML"
    # 어떤 영화(mcode)의 모든 리뷰페이지 가져오기
    while True:
        # url 요청
        pickle_name = f"{page}.pickle"
        make_folder(data_dir,today,mcode,HTML_Folder)
        url_review_page = f"https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={mcode}&target=after&page={page}"
        save_dir = os.path.join(data_dir,today,mcode,HTML_Folder,pickle_name)
        soup = url_bs4(url_review_page, save_dir)
        if soup is None:
            break
                
        # 파싱
        try:
            reviews = soup.find_all("td",{"class":"title"})
            for review in reviews:
                sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
                if sentence != "":
                    # movie = review.find("a",{"class":"movie color_b"}).get_text() 영화 이름 뽑는 변수
                    score = review.find("em").get_text()
                    review_data.append([int(score),sentence])      

        except Exception as e:
            # print("파싱 에러")
            logging.warning("파싱 에러")
            # print(e)
            logging.warning(e)

        # 잠시 쉬고 다음페이지로 넘어가기
        
        
        # 만약에 파싱후 얻을 내용이 없는 경우(맨 마지막 페이지의 경우) break
        time.sleep(0.5)
        page += 1
        finall = soup.find(class_='pg_next')
        if finall is None:
            # print("마지막 페이지 입니다.")
            logging.info("마지막 페이지 입니다.")
            break
        break

    # 얻은 리뷰를 저장
    review_data = list(map(lambda x: ', '.join([str(x[0]),x[1]]), review_data))   
    review_data = '\n'.join(review_data)
    with open(os.path.join(data_dir,today,mcode,'review.txt'), "w", encoding="utf8") as f:
        f.write(str(review_data))
  