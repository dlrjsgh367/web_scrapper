import requests 

from bs4 import BeautifulSoup

import xml
import xml.etree.ElementTree as ET

def sort(a, b, c, d, e, f, g, h, i, j, k):

    a_fix = '<root>{}</root>'.format(a)
    a_content = ET.fromstring(a_fix).text

    b_fix = '<root>{}</root>'.format(b)
    b_content = ET.fromstring(b_fix).text
    
    c_fix = '<root>{}</root>'.format(c)
    c_content = ET.fromstring(c_fix).text

    d_fix = '<root>{}</root>'.format(d)
    d_content = ET.fromstring(d_fix).text

    e_fix = '<root>{}</root>'.format(e)
    e_content = ET.fromstring(e_fix).text

    f_fix = '<root>{}</root>'.format(f)
    f_content = ET.fromstring(f_fix).text

    g_fix = '<root>{}</root>'.format(g)
    g_content = ET.fromstring(g_fix).text

    h_fix = '<root>{}</root>'.format(h)
    h_content = ET.fromstring(h_fix).text

    i_fix = '<root>{}</root>'.format(i)
    i_content = ET.fromstring(i_fix).text

    j_fix = '<root>{}</root>'.format(j)
    j_content = ET.fromstring(j_fix).text

    k_fix = '<root>{}</root>'.format(k)
    k_content = ET.fromstring(k_fix).text
    
    result = f"특허명 : {a_content}", f"IPC : {b_content}", f"출원인 : {c_content}", f"출원번호 : {d_content}", f"출원일자 : {e_content}", f"등록번호 : {f_content}", f"등록일자 : {g_content}", f"공개번호 : {h_content}", f"공개일자 : {i_content}", f"대리인 : {j_content}", f"발명자 : {k_content}", "\n"
    return result


# category : 검색유형
# row : row개의 검색결과를 가져옴
# Keyword : 검색어 입력(검색어 + 검색어 도 됨)
def search_result(category, row, Keyword):
    # 결과값을 담아놓는 리스트
    result_list = []
    
    # url 
    url = "http://kportal.kipris.or.kr/kportal/resulta.do"

    # header
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
    
    # data 
    data = {
    "next": f"{category}",
    # patentList
    # designList
    # trademarkList
    # frnUSList
    # frnEUList
    # frnJPList
    "FROM": "SEARCH",
    "searchInTransKorToEng": "N",
    "searchInTransEngToKor": "N",
    "row": f"{row}",
    "page": "1",
    "queryText": f"{Keyword}",
    "expression": f"{Keyword}",
    }

    # response
    res = requests.post(url, headers=headers, data=data)
    
    soup = BeautifulSoup(res.text, "lxml")
    
    result = soup.find_all("article")

    with open("search_result.xml", "w", encoding='utf8') as f:
        f.write(str(result))

    for item in result:
        tlv = item.find('tlv').text # 특허명
        ipv = item.select_one('a').text # IPC
        apv = item.find('apv').text # 출원인
        vdkvgwkey = item.find('vdkvgwkey').text # 출원번호
        adv = item.find('adv').text # 출원일자
        gnv = item.find('gnv').text # 등록번호
        gdv = item.find('gdv').text # 등록일자
        onv = item.find('onv').text # 공개번호
        odv = item.find('odv').text # 공개일자
        agv = item.find('agv').text # 대리인
        inv = item.find('inv').text # 발명자
        abv = item.find('abv').text # 상세 설명
        result_list.append(sort(tlv,ipv,apv,vdkvgwkey,adv,gnv,gdv,onv,odv,agv,inv))

    Real_result_list  = []
    for i in result_list[:row]:
        i = "\n".join(i)
        Real_result_list.append(str(i))
    # 결과 값 txt 파일 저장
    with open("search_result.txt", "w", encoding='utf8') as f:
        f.writelines(Real_result_list)
    
if __name__ == "__main__":
    search_result(category="patentList", row=30, Keyword="안경")
    
    


