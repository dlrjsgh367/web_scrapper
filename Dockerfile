FROM python:3.10.8

# COPY utils /tmp
# COPY requirements.txt /tmp
# WORKDIR /tmp
# RUN pip install -r requirements.txt

# COPY utils /usr/src
# WORKDIR /usr/src/app
# COPY . .

# COPY . .

COPY utils/ /usr
COPY requirements.txt /usr
WORKDIR /usr
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD [ "test.py"]