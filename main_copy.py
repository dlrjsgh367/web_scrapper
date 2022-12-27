import logging
import os
import argparse
import pickle

from utils.scrapper import parsing_mcode_list, parsing_reviews
from utils.util import get_today2


logger = logging.getLogger(__name__)
today = get_today2()
log_dir = "./data/logs"
logging.basicConfig(format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s", level=logging.INFO)

# dir = dir.replace("\\", "/")
#     file_name = dir.split('/')[-1]
#     file_dir = '/'.join(dir.split('/')[:-1])
#     if file_name in os.listdir(file_dir):
#         with open(dir, 'rb') as fr:
#             soup = pickle.load(fr)
# path = "./data/2022-12-27"            
# file_list = os.listdir(path)
# print(file_list) ##
 
def str2bool(v):
    if isinstance(v, bool):
       return v
    
    if v.lower() in ('yes', 'True', 't', 'y', '1'):
        # return True
        folder_dir = os.path.join(asd)
        if not os.path.isdir(folder_dir):
            with open(dir, 'rb') as fr:
                hihi = pickle.load(fr)
            return hihi
    elif v.lower() in ('no', 'False', 'f', 'n', '0'):
        pass

    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def file_parser(input_file, output_file=''):
    print(f'Processing {input_file}')
    print('Finished processing')
    if output_file:
        print(f'Creating {output_file}')

def main():
    '''
    #parsing_reviews는 지정한 영화코드의 모든 리뷰페이지를 파싱해오는것인데
    for문을 이용해 mcode_list 안에있는 모든 영화코드들을 parsing_reviews가 읽을수 있도록
    작성되었습니다.
    '''
    


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
    


if __name__ == "__main__": #국룰.
    
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-b', '--boolean_flag', help='boolean flag', default=False, type=str2bool)
    args = parser.parse_args()
    main()