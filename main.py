import requests 
from bs4 import BeautifulSoup



page = requests.get('http://kportal.kipris.or.kr/kportal/search/total_search.do').text
soup = BeautifulSoup(page, 'html.parser')
forms =soup.find_all('form')
for form in forms:
    print(form)


"""
searchTarget=total&
merchandiseString=&
measureString=&
patternString=&
searchType=&
queryText=%EB%B0%B1%EC%8B%A0&
expression=%EB%B0%B1%EC%8B%A0&
sortField=&
sortState=&
sortField1=&
sortState1=&
collectionValues=&
config=&
userId=&
configChange=&
selectedLang=&
lang=&currentTab=&
searchKeyword=%EB%B0%B1%EC%8B%A0&
searchExpression=%EB%B0%B1%EC%8B%A0&
searchInTrans=&
strstat=MID%7CKW&
isResultPageSearch=&
inputQueryText=%EB%B0%B1%EC%8B%A0
"""
