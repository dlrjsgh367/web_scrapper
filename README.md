# web_scrapper  

- web_scrapper는 어떤 동작을 하나요?
  > ㅁㄴㅇㅁㄴㅇㅁ

- 사용법 2가지  
  + 파이썬  
  * 도커
  
# 파이썬
### 파이썬으로 web_scrapper를 실행해봅시다.
올려둔 파일중에 requirements.txt 가 있는데요. 이 파일은
web_scrapper를 실행할때 요구되는 라이브러리들을 안에 담아 두고있습니다. 
```
pip install -r requirements.txt
```
위에 커맨드를 입력하면 requirements.txt 안에 있는 라이브러리들이 설치됩니다.





# 도커
## 도커 이미지 만들기
``` docker
docker build -t test .
```
위에서 생성한 것은 web_scrapper를 실행할때 필요한 라이브러리를 설치해주는 도커 이미지입니다.  
 test는 임의로 지정한 이름이니 다른 이름을 쓰셔도 상관없습니다.


생성이 잘 되었는지 확인해볼까요?
``` docker
docker image ls
```

------------

![image](https://user-images.githubusercontent.com/118237164/208035552-fa170dde-09c3-4d5e-9e0e-364a94eb29df.png)

------------
이렇게 나온다면 성공이에요.


## 도커 컴포즈로 실행 시키기
도커 파일을 이용해서 이미지를 생성하는데 성공했다면  
 이제는 도커 컴포즈를 이용해서 web_scrapper를 실행해보겠습니다.


위에서 생성한 이미지의 이름을 도커 컴포즈 이미지 입력란에 입력하세요.


``` docker
version: "3"
services:
  web_scrapper:
    container_name: naver_movie_scrapper 
    image: test 
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
도커 컴포즈에서 이미지 지정을 끝냈다면

``` docker
docker-compose up -d
```
위에 커맨드를 입력해서 web_scrapper를 실행합니다 !

![image](https://user-images.githubusercontent.com/118237164/208042388-372eeb5c-448a-45ca-a0e0-db7e401ae53c.png)

도커가 실행중인것을 볼수 있는데요.
![image](https://user-images.githubusercontent.com/118237164/208042531-d68abe45-7fa5-4be4-a4ca-123209165aba.png)

도커가 종료되었네요. local pc에 data 폴더가 생겼을거에요.
![image](https://user-images.githubusercontent.com/118237164/208042752-7d4c3d69-3112-42a9-b526-3d77bc847dc0.png)


![image](https://user-images.githubusercontent.com/118237164/208045174-45eaa3f9-7c84-4076-b5d6-c6cdc7985729.png)



