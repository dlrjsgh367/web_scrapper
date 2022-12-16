from utils.scrapper import parsing_mcode_list, parsing_reviews 

def main():
    # 현재 시점에서 최신 영화 리스트를 받아서 저장하고 가져오기
    print("네이버 최근영화목록을 가져오고 있습니다.")
    mcode_list = parsing_mcode_list()
    # 최신 영화 리스트에서 영화마다 리뷰를 받아서 저장하기
    for mcode in mcode_list:
        print(f"{mcode}을 파싱하고 있습니다.")
        parsing_reviews(mcode)

if __name__ == "__main__": #국룰.
    main()