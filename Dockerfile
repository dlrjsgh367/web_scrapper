FROM bs4/beautifulsoup4:4.11

WORKDIR /usr/src


COPY requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["test.py"]

ENTRYPOINT ["python3"]