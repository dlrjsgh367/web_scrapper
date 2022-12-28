import logging
import os
import argparse
import pickle

from bs4 import BeautifulSoup

from utils.scrapper import parsing_mcode_list, parsing_reviews
from utils.util import get_today2



logger = logging.getLogger(__name__)
today = get_today2()
log_dir = "./data/logs"
logging.basicConfig(format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("-f","--fdname", help="폴더 이름을 정합니다.")
args = parser.parse_args()

foldername_dir = f"./data/{args.fdname}"


def main():
    '''
    #parsing_reviews는 지정한 영화코드의 모든 리뷰페이지를 파싱해오는것인데
    for문을 이용해 mcode_list 안에있는 모든 영화코드들을 parsing_reviews가 읽을수 있도록
    작성되었습니다.
    '''
    # arg_dir = os.path.join(foldername_dir)
    # if args.fdname:
    #     os.makedirs(arg_dir)
        

    folder_dir = os.path.join(log_dir)
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)

    logging.basicConfig(format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s", level=logging.INFO)
    
    f_handler = logging.FileHandler(f"./data/logs/{today}.log", "a", encoding="utf-8")
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s")
    f_handler.setFormatter(f_format)

    root_logger = logging.getLogger()
    root_logger.addHandler(f_handler)

   
    
    
    # 현재 시점에서 최신 영화 리스트를 받아서 저장하고 가져오기
    print("네이버 최근영화목록을 가져오고 있습니다.", flush=True)
    mcode_list = parsing_mcode_list()
    # 최신 영화 리스트에서 영화마다 리뷰를 받아서 저장하기
    for mcode in mcode_list:
        
        print(f"{mcode}을 파싱하고 있습니다.", flush=True)
        parsing_reviews(mcode)  
    
# def asd():
#     with open("C:/Users/HAMA/code/web_scrapper/data/2022-12-28/194841/HTML/2.pickle", "rb") as pp:
#         # pp = BeautifulSoup(pp)
#         data = pickle.load(pp)
#     print(data)
if __name__ == "__main__": #국룰.
    main()

# 기존에는 [ python main.py ] 를 입력해서 실행하면 ./data/오늘날짜/영화코드폴더/HTMl 로 폴더가 생성되었는데, 
# argparse 를 이용해서 인자 [ python main.py -f "폴더명" ] 를 입력하면 ./data/폴더명/영화코드폴더/HTMl 로 폴더가 생성 되게 하는것을 성공하였다.  