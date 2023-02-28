import requests 

import xml
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup



def reject_status_remove(status_check, title):
    """
    status가 '거절'인 것을 제거해주는 함수 입니다.
    """ 
    for status in status_check:
        s = status.find("status").text
        if s == "<![CDATA[거절]]>":
            pass
        else:
            with open(f'./xml/{title}.xml', "a", encoding="utf8") as f:
                f.write(str(status))
            

def remove_tag(x, y, z):
    """
    xml 태그를 제거해주는 함수입니다.
    """

    x_fix = f'<root>{x}</root>'
    x_content = ET.fromstring(x_fix).text

    y_fix = f'<root>{y}</root>'
    y_content = ET.fromstring(y_fix).text

    z_fix = f'<root>{z}</root>'
    z_content = ET.fromstring(z_fix).text
    
    result =  f"출원번호 : {x_content}", f"특허명 : {y_content}", f"요약 : {z_content}", "\n"
    return result


def status_remove(Keyword, row):
    """
    Arguments
    row : row개의 검색결과를 가져옴
    Keyword : 검색어 입력(검색어 + 검색어 도 됨)  
    """

    # url 
    url = "http://kportal.kipris.or.kr/kportal/resulta.do"

    # header
    headers = {
                "Referer": "http://kportal.kipris.or.kr/kportal/search/total_search.do",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                }
    # data 
    data = {
            "next": "patentList",
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
    
    # reject_status_remove arguments
    status_check = soup.find_all("article")

    # '거절' status 제거 후 xml 파일 저장
    reject_status_remove(status_check=status_check, title=Keyword)

    # reject_status_remove로 저장한 파일 open
    result_file = open(f'./xml/{Keyword}.xml', 'r', encoding="utf8")

    soup = BeautifulSoup(result_file, 'lxml')

    # 중간 결과값을 담아놓는 리스트
    result_list = []

    # find article
    result = soup.find_all("article")
    for item in result:
        
        # 특허명
        tlv = item.find('tlv').text 
        
        # 출원번호
        vdkvgwkey = item.find('vdkvgwkey').text 
        
        # 요약
        abv = item.find('abv').text 

        # xml 태그 제거 후 중간 결과 리스트에 추가
        result_list.append(remove_tag(tlv,vdkvgwkey,abv))

    # 최종 결과값을 담을 리스트
    Real_result_list  = []
    for i in result_list[:row]: # 0부터 row 만큼 반복
        i = "\n".join(i)
        Real_result_list.append(str(i))

    # 최종 결과 리스트 저장
    with open("./search_result/search_result.txt", "w", encoding='utf8') as f:
        f.writelines(Real_result_list)

if __name__ == "__main__":
    status_remove(Keyword="AI+그림", row=30)
    
    


