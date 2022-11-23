from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import time
import pickle


def mcode_list(): # 네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?&page=1')
    soup = BeautifulSoup(url, 'html.parser')
    soup = soup.select('#current_movie > option')
    line = []
    for val in soup:
        code = val.get('value')
        if code is not None:
            line.append(code)    
    return line


def asd():   
    review = []
    movie_code = input("영화코드를 입력하세요 : ")
    for page in range(10):
        url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page={page}')
        soup = BeautifulSoup(url, 'html.parser')
        review = soup.find('tbody').text 
        print(review)
        # if review == "":
        #     return False
        time.sleep(0.5)  
        
with open("영화이름.pickle","wb") as fw:
    pickle.dump(asd(), fw)

with open("영화이름.pickle","rb") as fr:
    data1234 = pickle.load(fr)
print(data1234)



# movie_code = '49945'
# url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page=1')
# soup = BeautifulSoup(url, 'html.parser')
# # td_list = soup.find_all("td", class_="title")
# td_list = soup.find_all("td",{"class":"title"})
# print(td_list)

# # for td in td_list:
#     print(td.find_all(class_="report"))
        

# print(soup.select_one('tbody > tr > td.title > a.report'))

#old_content > table > tbody > tr:nth-child(1) > td.title
#old_content > table > tbody > tr > td.title > a.report

# review = []
# for page in range(105):
#     movie_code = '49945'
#     url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page={page}')
#     soup = BeautifulSoup(url, 'html.parser')
#     review = soup.find('tbody').text 
#     if review != "":
#         print False
#     print(review)
#     time.sleep(0.5)  
    


# movie = input("영화 코드를 입력하세요 : ")
# url = urlopen(f'https://movie.naver.com/movie/bi/mi/basic.naver?code={movie}')
# soup = BeautifulSoup(url, 'html.parser')
# print(soup.find_all('td'))

# movie_code = '49945'
# url =  urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page=1')
# soup = BeautifulSoup(url, 'html.parser')
# print(soup.select_one('#old_content > table > tbody'))

# for page in range(1,500):
#     url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
#     soup = BeautifulSoup(url,'html.parser')
#     #find_all : 지정한 태그의 내용을 모두 찾아 리스트로 반환
#     reviews = soup.find_all('div',{'id':'old_content'})
#     time.sleep(1)
#     print(reviews)


# for linebreak in soup.find_all('br'):
#     print(linebreak.extract())

    # print(soup.prettify())
# hi = soup.find('p').find_all(text=True)
# print(hi)

# for linebreak in soup.find_all('br'):
#     linebreak.extract()
#     print(soup.prettify())    


# url = urlopenf'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=49945&target=after&page=1'
# soup = BeautifulSoup(url, 'html.parser')
# print(soup.find('tr'))

