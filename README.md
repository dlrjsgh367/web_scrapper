# Web scrapper
## web_scrapper는 어떤 동작을 하나요?
  > ㅁㄴㅇㅁㄴㅇㅁ


## 사용법 2가지  
### 파이썬  
### 도커  


## 파이썬
### 파이썬으로 web_scrapper를 실행해봅시다.
올려둔 파일중에 requirements.txt 가 있는데요. 이 파일은
web_scrapper를 실행할때 요구되는 라이브러리들을 안에 담아 두고있습니다. 
```
pip install -r requirements.txt
```
위에 커맨드를 입력하면 requirements.txt 안에 있는 라이브러리들이 설치됩니다.

라이브러리를 설치했다면 남은건 실행밖에 없겠네요
```
python main.py
```





## 도커  
### 도커 컴포즈 이용하기
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

성공적으로 영화코드, 영화리뷰, 영화코드와 리뷰를 가져온 url의 HTML까지 저장이 되었습니다.




