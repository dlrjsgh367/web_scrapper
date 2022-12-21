# Web scrapper

## 목차
web_scrapper  
* 개요
* 사용법 2가지
   * [파이썬](#파이썬)
   * [도커](#도커)



## 개요
  > 1. 네이버 영화 사이트에 현재상영중인 영화목록에 영화코드를 모두 가져옵니다.
  > 2. ./data/오늘날짜/영화코드/HTML폴더를 생성합니다.   
  > ./data/오늘날짜 폴더를 생성하고 1번에서 가져온 영화코드를 이름으로 폴더를 생성한 뒤 영화코드폴더에 HTML 폴더를 생성합니다.
  > 3. 리뷰 시작페이지 ~ 종료페이지 의 html을 .pickle 로 저장한뒤 HTML 폴더에 저장합니다. 리뷰는 pickle 저장이 끝나면 영화코드 폴더에 저장됩니다.  
  > 4. request, response strategy
    - 10초동안 응답이 없을 경우 다음 작업으로 넘어갑니다. 로그 파일에서 확인할 수 있습니다.
    - 
 


## 사용법 2가지
---
### 파이썬
#### 파이썬으로 web_scrapper를 실행해봅시다.
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

```
├── dir1
│   ├── file11.ext
│   └── file12.ext
├── dir2
│   ├── file21.ext
│   ├── file22.ext
│   └── file23.ext
├── dir3

web_scrapper
├── main.py
└── data
    └── 오늘날짜
          ├── 
          └── mcode.txt
        
```

성공적으로 영화코드, 영화코드로 폴더 생성, 영화리뷰, 영화코드와 리뷰를 가져온 url의 HTML.pickle까지 저장이 되었습니다.


mcode(현재상영중인 영화목록코드).txt
![image](https://user-images.githubusercontent.com/118237164/208342994-ba976458-6a69-4267-be99-e8c55d56e99d.png)
별점과 리뷰 내용 
![image](https://user-images.githubusercontent.com/118237164/208343025-1a078ca6-f6da-43ac-846a-54033cc5d0a5.png)
별점과 리뷰 내용을 가져온 URL의 HTML (pickle)
![image](https://user-images.githubusercontent.com/118237164/208343039-405d54f9-988c-4f28-8d8e-5a4abffc94d8.png)





### 도커  
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

#### 도커 컴포즈 이용하기
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

프로젝트 시작일 : 2022-11-15

- [Web scrapper](#web-scrapper)
  * [목차](#--)
  * [web_scrapper는 어떤 동작을 하나요?](#web-scrapper-------------)
  * [사용법 2가지](#----2--)
    + [1. 파이썬](#1----)
      - [파이썬으로 web_scrapper를 실행해봅시다.](#------web-scrapper--------)
    + [2. 도커](#2---)
      - [도커 파일](#-----)
      - [도커 컴포즈 이용하기](#-----------)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



