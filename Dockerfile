FROM python:3.10.8

# COPY utils/request.py /usr/src/request.py
# COPY utils/scrapper.py /usr/src/scrapper.py
# COPY utils/util.py /usr/src/util.py
# COPY test.py /usr/src/test.py
# WORKDIR /usr/src/app
# COPY . .
# COPY requirements.txt /usr/src/app/requirements.txt
# RUN python3 -m pip install -r /usr/src/app/requirements.txt

# RUN apt-get update -y
# COPY requirements.txt /usr/src/requirements.txt
# RUN python3 -m pip install -r /usr/src/requirements.txt

# COPY utils/request.py /usr/src/request.py
# COPY utils/scrapper.py /usr/src/scrapper.py
# COPY utils/util.py /usr/src/util.py
# WORKDIR /usr/src
# COPY . .
#되는거

RUN apt-get update -y
COPY requirements.txt /usr/src/requirements.txt
RUN python3 -m pip install -r /usr/src/requirements.txt

COPY utils/request.py /usr/src/utils/request.py
COPY utils/scrapper.py /usr/src/utils/scrapper.py
COPY utils/util.py /usr/src/utils/util.py
COPY test.py /usr/src/test.py
WORKDIR /usr/src

ENTRYPOINT ["python3"]

CMD [ "test.py"]