from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import pickle
import sys
sys.setrecursionlimit(10000)

def add(a: int, b: int) -> int: 
    return a+b

result = add(3, 3.4)
# print(result)  # 6.4 출력

def test(a = 'a', b = 1, c = None):
    """
    test 함수입니다.
        Args:
            a ``str``: a value
            b ``int``: b value
            c ``str``: c value
        Retruns:
            None
    """
    pass
test()


def mcode_list():
    """
    네이버 최근영화목록의 영화코드를 리스트로 리턴하는 함수입니다.
    """
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?&page=1')
    soup = BeautifulSoup(url, 'html.parser')
    soup = soup.select('#current_movie > option')
    line = []
    for val in soup:
        code = val.get('value')
        if code is not None:
            line.append(code)    
    return line

def save():
    '''
    지정한 영화의 모든 리뷰페이지의 html을 bs4 객체로 받아서 list.pickle 폴더에 저장하는 함수입니다.
    '''
    url = urlopen('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=49948&target=after')
    soup = BeautifulSoup(url, 'html.parser')

    with open('list.pickle', 'wb') as fw:
        pickle.dump(soup, fw)
    with open('list.pickle', 'rb') as fr:
        res = pickle.load(fr)
    return res

def url_html(url:str) -> BeautifulSoup:
    '''
    url을 입력받으면 html을 출력해주는 함수입니다.
    '''
    url = urlopen(url)
    soup = BeautifulSoup(url, 'html.parser')
    return soup

print(url_html("https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=okkam76&logNo=221609687351"))
# print((url_html('https://stackoverflow.com/questions/32957708/python-pickle-error-unicodedecodeerror')))

# def asd(movie_code):   
#     review = []
#     review_data=[]
#     need_reviews_cnt = 1000
#     for page in range(need_reviews_cnt):
#         url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page={page}')
#         soup = BeautifulSoup(url, 'html.parser')
#         reviews = soup.find_all("td",{"class":"title"})
#         for review in reviews:
#             sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
#             if sentence != "":
#                 movie = review.find("a",{"class":"movie color_b"}).get_text()
#                 review_data.append([movie,sentence])
#                 need_reviews_cnt-= 1
#                 time.sleep(0.5)
#         if need_reviews_cnt < 0:
#             break
#     return review_data

        # with open('list.pickle', 'w', encoding="utf8") as fw:
#     pickle.dump(asd(49945), fw)
# with open("list.pickle","r", encoding="UtF-8") as fr:
#     data = pickle.load(fr)
# print(data)



# movie_code = '49945'
# url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page=1')
# soup = BeautifulSoup(url, 'html.parser')
# # td_list = soup.find_all("td", class_="title")
# td_list = soup.find_all("td",{"class":"title"})

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

# # def test1():
# for page in range(1,11):
#     url = urlopen(f'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=49945&target=after&page={page}')
#     soup = BeautifulSoup(url, 'html.parser')
#     reviews = soup.find_all("tbody")
    
    # for review in reviews:
    #     sentence = review.find("a",{"class":"report"}.get("onclick"))
    #     print(sentence)
# with open("abc.pickle","wb") as fw:
#     pickle.dump(test1(), fw)

# with open("abc.pickle","rb") as fr:
#     data1234 = pickle.load(fr)
# print(data1234)




    #old_content > table > tbody > tr:nth-child(1) > td.title



