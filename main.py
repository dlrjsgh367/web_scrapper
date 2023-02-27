import requests 
from bs4 import BeautifulSoup
import xml

from urllib import parse

def search_result(type, Keyword):
    # result_list = []
    # url 주소
    url = "http://kportal.kipris.or.kr/kportal/resulta.do"

    # header 값
    headers = {
        "Accept": "application/xml, text/xml, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "117",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "JSESSIONID=kcz5bnBNFiaICTuFEgysKs4C6S0OISkmhWjAIoRXV2mFcEpbbmLtgmrz93itoRMa.amV1c19kb21haW4va3BvcnRhbDM=; _ga=GA1.3.953350611.1677154053; TM_CONFIG=G11111111111111111SX11111110011111100; AB_CONFIG=G11001111111111111111111111110S10000111000111100001000; AT_CONFIG=G0000000000000S111110110111; KA_CONFIG=G0000000000000S110111000; K2_CONFIG=G1111111111111111111111S111111111000000000; AD_CONFIG=G11111111111111S1111111111111000; _gid=GA1.3.348414736.1677460475; __utmc=31935460; KPAT_RECENTLY_JOB=1020170090723; KD_CONFIG=G1111111111111111111111S111111111000000000; EC=W4SYY9pLzcuGMoQxSBxdG5HMPvt565cyRG7UUK4ffo8=; NKP_CONFIG=G1111111111111111111111S110001000000000000; NAB_CONFIG=G11001111111111111111111111110S10000010000000010000; KP_CONFIG=G1111111111111111111111S111111111000000000; DG_CONFIG=G11111111111111111SX11100110011011111; JM_CONFIG=G11111111111111SX01101111110010; KPAT_SRCH_HISTORY=421CE58A92E2FB07; KP_TOTAL_HISTRY=AI; __utma=31935460.953350611.1677154053.1677475066.1677477746.11; __utmz=31935460.1677477746.11.8.utmcsr=kipris.or.kr|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; KIPRIS_TODAY_CNT=CHECKED; __utmb=31935460.2.10.1677477746; _gat=1",
        "Host": "kportal.kipris.or.kr",
        "Origin": "http://kportal.kipris.or.kr",
        "Referer": "http://kportal.kipris.or.kr/kportal/search/total_search.do",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # data 값
    data = {
    "next": f"{type}",
    # patentList
    # designList
    # trademarkList
    # frnUSList
    # frnEUList
    # frnJPList
    "FROM": "SEARCH",
    "searchInTransKorToEng": "N",
    "searchInTransEngToKor": "N",
    "row": "5",
    "page": "1",
    "queryText": f"{Keyword}",
    "expression": f"{Keyword}",
    }

    # response
    res = requests.post(url, headers=headers, data=data)

    soup = BeautifulSoup(res.text, "html.parser")
    result = soup.find_all("article")
    for item in result:
        print(f"특허명   : {item.find('tlv').text}")
        print(f"IPC      : {item.find('ipv').text}")
        # print(f"출원인   : {item.find('apv').text}")
        # print(f"출원번호 : {item.find('vdkvgwkey').text}")
        # print(f"출원일자 : {item.find('adv').text}")
        # print(f"등록번호 : {item.find('gnv').text}")
        # print(f"등록일자 : {item.find('gdv').text}")
        # print(f"공개번호 : {item.find('onv').text}")
        # print(f"공개일자 : {item.find('odv').text}")
        # print(f"대리인   : {item.find('agv').text}")
        # print(f"발명자   : {item.find('inv').text}")
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    # with open("search_result.xml", "w", encoding='utf8') as f:
    #     f.write(str(result))
    
if __name__ == "__main__":
    search_result(type="patentList", Keyword="AI+그림")

