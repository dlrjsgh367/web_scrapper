FROM python:3.10.8


# COPY utils/request.py /usr/src/request.py
# COPY utils/scrapper.py /usr/src/scrapper.py
# COPY utils/util.py /usr/src/util.py
# WORKDIR /usr/src
# COPY . .
#되는거

# RUN apt-get update -y
# COPY requirements.txt /usr/src/requirements.txt
# RUN python3 -m pip install -r /usr/src/requirements.txt

# COPY utils/request.py /usr/src/utils/request.py
# COPY utils/scrapper.py /usr/src/utils/scrapper.py
# COPY utils/util.py /usr/src/utils/util.py
# COPY test.py /usr/src/test.py
# WORKDIR /usr/src

# ENTRYPOINT ["python3"]

# CMD ["test.py"]
# 인스트럭션을 적게 사용하라

# COPY requirements.txt /usr/src/requirements.txt
# RUN python3 -m pip install -r /usr/src/requirements.txt \
RUN python3 -m pip install beautifulsoup4==4.11.1 \
 && python3 -m pip install bs4==0.0.1 \
 && python3 -m pip install certifi==2022.12.7 \
 && python3 -m pip install soupsieve==2.3.2.post1 \
 && python3 -m pip install wincertstore==0.2

# COPY utils/request.py /usr/src/utils/request.py
# COPY utils/scrapper.py /usr/src/utils/scrapper.py
# COPY utils/util.py /usr/src/utils/util.py

# COPY ./utils /usr/src/utils
# COPY ./test.py /usr/src/test.py
# WORKDIR /usr/src

# COPY C:/Users/HAMA/code/web_scrapper/utils /usr/src/utils
# COPY C:/Users/HAMA/code/web_scrapper/test.py /usr/src/test.py
# WORKDIR /usr/src

# ENTRYPOINT ["python3"]
# # #Dockerfile 이내에 하나의 CMD만 선언 가능하며, 여러개의 CMD가 존재지 마지막 CMD만 수행된다.
# CMD ["test.py"]


