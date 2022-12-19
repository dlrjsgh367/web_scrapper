# Web scrapper
## web_scrapper는 어떤 동작을 하나요?
  > 1. 네이버 영화 사이트에 현재상영중인 영화목록에 영화코드를 모두 가져옵니다.
  > 2. ./data/오늘날짜/영화코드/HTML폴더를 생성합니다.   
  > ./data/오늘날짜 폴더를 생성하고 1번에서 가져온 영화코드를 이름으로 폴더를 생성한 뒤 영화코드폴더에 HTML 폴더를 생성합니다.
  > 3. 리뷰 시작페이지 ~ 종료페이지 의 html을 .pickle 로 저장한뒤 HTML 폴더에 저장합니다.  리뷰는 pickle 저장이 끝나면 영화코드 폴더에 저장됩니다.  
 
## web scrapper의 구성
web_scrapper가 실행되려면 request, scrapper, util 이 3개의 파이썬 파일이 필요합니다.


 request  
```python
from urllib.request import urlopen
import functools
from threading import Thread
import pickle
import os
import logging

from bs4 import BeautifulSoup

설명 : timeout 데코레이터를 설정해주고, 메서드 실행시간이 지정한 시간을 지나면 raise를 통해 강제로 에러를 발생시켜 pass 해줍니다.
      request 마지막에 등장하는 url_request에 데코레이터로 timeout 10초를 걸어주고, request(실행시간) 10초가 넘으면
      에러를 발생 시켜 pass 합니다.
       
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

설명 : 파라미터를 2개 받는데, 첫번째는 url, 2번째는 dir(경로)입니다. 아래 나오는 scrapper에서 사용됩니다.
      file_name : dir(경로)을 "/" 기준으로 나눠서 맨 마지막에 있는것을 가르킵니다. dir(경로)의 맨 마지막에 있는것은 pickle_name 입니다.
      pickle_name은 scrapper에 있는 save_dir에서 확인할수 있습니다.
      
      file_dir : 맨 마지막 인덱스를 제외한 모든 dir을 "/" 기준으로 나눈뒤  "/" 가 있는 dir끼리 합칩니다. 
      file_dir의 값은 data_dir/today/mcode/HTML_Folder/pickle_name에서
      맨 마지막 인덱스를 제외 했으니 data_dir/today/mcode/HTML_Folder 가 되겠습니다. 
      
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
            response = url_request(url) # url_request 사용됨 .
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



설명 : 웹 사이트에 리퀘스트를 보내 정상값(200)이면
      logging.info("정상 응답")
      비정상값(.)이면
      아무동작 안하기
      함수 동작이 끝나면 response 값을 return합니다.
      url_request는 위에 있는 url_bs4에 사용되었습니다..
      
@timeout(10)
def url_request(url):
    response = urlopen(url)
    if response.status == 200:
        logging.info("정상 응답")
    #elif response.status == .


    return response
print(urlopen)
```
scrapper
```python

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
    
    설명 : 네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수입니다.
    
   
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
    
    설명 : 지정한 영화코드의 모든 리뷰페이지를 가져오는 함수입니다.
    
    
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
        soup = url_bs4(url_review_page, save_dir) # url_bs4의 url과 dir
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
```
util
```python

import time
import logging
import os

설명 : 오늘날짜를 리턴하는 함수입니다.
def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.
        tm_mon, now.tm_mday)
    return s


설명 : 폴더를 생성하는 함수입니다. 폴더 생성을 성공하면 폴더가 생성되었다고 출력
이미 폴더가 생성 되어있다면 이미 존재하는 폴더인것만 알려주고 다른 동작은 취하지 않습니다.
def make_folder(*dir):
    folder_dir = os.path.join(*dir)
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)
        logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 폴더가 생성되었습니다.\n")
    else:
        logging.info(f"{'/'.join(list(dir[:-1]))} 에 {dir[-1]} 는 이미 존재하는 폴더입니다.\n")
```

## 사용법 2가지  
### 파이썬  
### 도커  


## 파이썬
### 파이썬으로 web_scrapper를 실행해봅시다.
올려둔 파일중에 requirements.txt 가 있는데요. 이 파일은
web_scrapper를 실행할때 요구되는 라이브러리들을 안에 담아 두고있습니다. 
현재는 web_scrapper를 실행할때 필요한 라이브러리 설치가 안되어있는데요.
```
pip install -r requirements.txt
```
위에 커맨드를 입력하면 requirements.txt 안에 있는 라이브러리들이 설치됩니다.

라이브러리를 설치했다면 남은건 실행밖에 없겠네요
```
python main.py
```
파싱 시작
![image](https://user-images.githubusercontent.com/118237164/208344026-084d0947-0fce-43dc-8a72-2528ff99c2bd.png)
파싱 종료
![image](https://user-images.githubusercontent.com/118237164/208344128-30dc3db6-2d67-4b13-a3b3-c7eb97d58a40.png)

성공적으로 영화코드, 영화코드로 폴더 생성, 영화리뷰, 영화코드와 리뷰를 가져온 url의 HTML.pickle까지 저장이 되었습니다.


mcode(현재상영중인 영화목록코드).txt
![image](https://user-images.githubusercontent.com/118237164/208342994-ba976458-6a69-4267-be99-e8c55d56e99d.png)
별점과 리뷰 내용 
![image](https://user-images.githubusercontent.com/118237164/208343025-1a078ca6-f6da-43ac-846a-54033cc5d0a5.png)
별점과 리뷰 내용을 가져온 URL의 HTML (pickle)
![image](https://user-images.githubusercontent.com/118237164/208343039-405d54f9-988c-4f28-8d8e-5a4abffc94d8.png)





## 도커  
### 도커 컴포즈 이용하기
#### 도커 파일
도커 파일 안에는 web_scrapper를 실행할때 요구하는 라이브러리들이 있습니다.
```docker
FROM python:3.10.8


RUN python3 -m pip install beautifulsoup4==4.11.1 \
 && python3 -m pip install bs4==0.0.1 \
 && python3 -m pip install certifi==2022.12.7 \
 && python3 -m pip install soupsieve==2.3.2.post1 \
 && python3 -m pip install wincertstore==0.2
```
도커 컴포즈에 build를 이용하여 도커파일에 있는 라이브러리가 설치 되도록 작성해줍니다.
``` docker
vers: "3"
services:
  web_scrapper:
    container_name: naver_movie_scrapper (컨테이너 이름)
    build: . (.은 현재 경로에 있는 dockerfile 을 가르킨다.)
    working_dir: /usr/src
    volumes:
      - type: bind
        source: ./utils
        target: /usr/src/utils
      - type: bind
        source: ./main.py
        target: /usr/src/main.py
      - ./data:/usr/src/data
    command: bash -c
      "cd /usr/src
      && python /usr/src/main.py"
```
도커 컴포즈 세팅이 끝났다면 실행 해봅시다.
``` docker
docker-compose up -d (-d 는 백그라운드로 실행하는 옵션)
```

![image](https://user-images.githubusercontent.com/118237164/208042388-372eeb5c-448a-45ca-a0e0-db7e401ae53c.png)

도커가 실행중인것을 볼수 있는데요.
![image](https://user-images.githubusercontent.com/118237164/208042531-d68abe45-7fa5-4be4-a4ca-123209165aba.png)

도커가 종료되었네요.
![image](https://user-images.githubusercontent.com/118237164/208042752-7d4c3d69-3112-42a9-b526-3d77bc847dc0.png)

파이썬으로 실행할때에는 requirements.txt 파일로 라이브러리를 인스톨 했습니다.
도커 컴포즈는 도커 컴포즈를 실행하면 도커파일에 작성된 라이브러리 목록을 설치하도록 했습니다.

성공적으로 영화코드, 영화코드로 폴더 생성, 영화리뷰, 영화코드와 리뷰를 가져온 url의 HTML.pickle까지 저장이 되었습니다.


mcode(현재상영중인 영화목록코드).txt
![image](https://user-images.githubusercontent.com/118237164/208342994-ba976458-6a69-4267-be99-e8c55d56e99d.png)
별점과 리뷰 내용 
![image](https://user-images.githubusercontent.com/118237164/208343025-1a078ca6-f6da-43ac-846a-54033cc5d0a5.png)
별점과 리뷰 내용을 가져온 URL의 HTML (pickle)
![image](https://user-images.githubusercontent.com/118237164/208343039-405d54f9-988c-4f28-8d8e-5a4abffc94d8.png)





