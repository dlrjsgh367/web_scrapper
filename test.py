import pickle
import logging

from utils.scrapper import parsing_mcode_list, parsing_reviews 

def main():
    # 현재 시점에서 최신 영화 리스트를 받아서 저장하고 가져오기
    print(f"네이버 최근영화목록을 가져오고 있습니다.")
    # logging.info("네이버 최근영화목록을 가져오고 있습니다.")
    mcode_list = parsing_mcode_list()
    # 최신 영화 리스트에서 영화마다 리뷰를 받아서 저장하기
    for mcode in mcode_list:
        print(f"{mcode}을 파싱하고 있습니다.")
        # logging.info(f"{mcode}을 파싱하고 있습니다.")
        parsing_reviews(mcode)
        
def asd():
    with open("./data/2022-12-06/195973/HTML/1.pickle", "rb") as rb:
        asd = pickle.load(rb)
    print(asd)

if __name__ == "__main__": #국룰.
    main()

# url = urlopen('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=154986&target=after&page=14')
# soup = BeautifulSoup(url, 'html.parser')
# print(soup)

