import time

from bs4 import BeautifulSoup

from utils.util import get_today, save
from utils.request import url_request
from utils.scrapper import parsing_mcode_list, parsing_reviews # * 쓰는건 별로 좋은 방법이 아닙니다. 쓸것만 딱 골라쓰세요 가져온 변수가 다른변수와 겹칠수가 있음.


def main():
    # 현재 시점에서 최신 영화 리스트를 받아서 저장하고 가져오기
    mcode_list = parsing_mcode_list()

    # 최신 영화 리스트에서 영화마다 리뷰를 받아서 저장하기
    for mcode in mcode_list:
        parsing_reviews(mcode)


if __name__ == "__main__": #국룰.
    main()