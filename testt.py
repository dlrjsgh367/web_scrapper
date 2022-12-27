# import argparse

# parser = argparse.ArgumentParser()

# ##1. Position type: 필수 입력
# # ex) test.py "이건호" 19 81
# parser.add_argument('name')# 1번째 위치 # a
# parser.add_argument('age', type=int)# 2번째 위치 # a
# parser.add_argument('weight', type=float)# 3번째 위치 # a


# ## 2. Keyword type: 옵션
# # ex) test.py --bouns 1200
# parser.add_argument('-b','--bouns', type=int) # a


# ## 3. Choice type
# # ex) test.py --animal [펭귄|원숭이|지렁이]
# parser.add_argument('-a', '--animal', choices=['펭귄', '원숭이', '지렁이']) # a 
# # parser.add_argument('-f', '--food', choices=['스테이크', '햄버거', '양상추'])


# # ## 4. Indicater type
# # parser.add_argument('-m', '--male', action='store_true')
# # parser.add_argument('-f', '--female', action='store_true')


# # 5. Mutually exclusive type
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-m', '--male', action='store_true') # a 
# group.add_argument('-ff', '--female', action='store_true') # a 

# args = parser.parse_args() # a


# print(f'name={args.name}')
# print(f'age={args.age}')
# print(f'weight={args.weight}')
# print(f'bouns={args.bouns}')

# if args.bouns:
#     print(f'bouns={args.bouns}')
# else:
#     print("보너스 안받았어요")

# if args.animal:
#     print(f'animal={args.animal}')
# else:
#     print("동물 선택을 안했어요.")

# if args.male:
#     print(f"Hi, Mr. {args.name}")

# if args.female:
#     print(f"Hi, Miss {args.name}")


#키워드 타입은 --를 붙여서 구분한다. --가 없으면 포지션 타입
#포지션 타입은 필수로 입력해야하는 값이지만, 키워드 타입은 옵션의 개념이므로 꼭 입력할 필요는 없다.

#주의 사항 - 표시는 사용자전용이고, 프로그램이 인식가능한 변수는 -- 이다.
#사용자는 -, -- 둘다 사용가능하지만 프로그램은 --만 인식한다.

#모든것은 명시를 안해주면 str type이다. 기호에 따라 type 을 바꿔라

#초이스 타입은 n개중 1개만 골라야 할경우 사용한다. 
#초이스 타입에 인자를 넣지않으면 None 값이 들어가고, 
#정의된 초이스 값(예 : 펭귄, 원숭이,지렁이)이 아닌 다른 인자가 들어온다면 error가 발생한다.

#인디케이터 타입은 어떤 값들이 필요한게 아닌, 상태를 알려주고 싶을때 사용한다. (store_true)
#위에서 정의한 인디케이터는 --male, --female 로 성별을 구분하는것이다. 
#그런데 우리가 인디케이터 타입을 정의한 이유는 성별을 구분하기 위함인데,
# test.py "이건호" 19 81 -b 1000 -a 펭귄 --male --female  처럼 마지막에 남성, 여성을 입력하면
# male, female arg에 설정한 print가 2개 다 나온다.

#간단 요약
#성별 구분하려고 인디케이터 썼는데 인자를 남성, 여성 둘다 넣으면 성별 구분이 안되니까
# 남성, 여성 인자 2개를 같이 입력했을때 에러를 발생시킬수 있게 Mutually exclusive type으로
# 남성 여성을 group화 시켜서 인자에 1개 이상의 값이 들어오면 에러를 발생시킬것이다

# Mutually exclusive 으로 인디케이터 값을 그룹화 하는것이기 때문에 
# 인티케이터 값을 Mutually exclusive 으로 그대로 넘겨서 인디케이터 값은 없어도 된다.

import os

# path = "C:/Users/HAMA/code/web_scrapper/data"            
# file_list = os.listdir(path)
# # print(file_list)

# for file in file_list:
#     filepath = path + '/' + file
#     print(filepath)

# if filepath:
    

# path = "C:/Users/HAMA/code/web_scrapper/data/2022-12-27"
# file_list = os.listdir(path)
# file_list_py = [file for file in file_list if file.endswith('.pickle')]
# print(file_list_py)

# print(os.getcwd())

# for currentdir, dirs, files in os.walk(r"C:\Users\HAMA\codeweb_scrapper"):

#     for file in files:
#         print(currentdir+r"\\"+file)
        

import os.path
from utils.util import get_today
today = get_today()
 
def print_file(dir):
 
    files = os.listdir(dir)
    
    for item in files :
    
        if os.path.isdir(dir+r"\\"+item) == True :
        
            print_file(dir+r"\\"+item)
            
        else:
        
            print(dir+r"\\"+item)
 
if __name__ == '__main__':
 
    dir = rf"C:\Users\HAMA\code\web_scrapper\data\{today}"
    # dir = r".\data"
    
    print_file(dir)
