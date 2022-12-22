FROM python:3.10.8
# ENV TZ=Asia/Seoul

RUN python3 -m pip install beautifulsoup4==4.11.1 \
 && python3 -m pip install bs4==0.0.1 \
 && python3 -m pip install certifi==2022.12.7 \
 && python3 -m pip install soupsieve==2.3.2.post1 \
 && python3 -m pip install wincertstore==0.2
