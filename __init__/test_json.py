# test json

import sys
from urllib.request import  Request, urlopen # 모듈
from datetime import *
import json
'''
url = 'http://www.naver.com'
request = Request(url) # url요청
resp = urlopen(request) #url열기
resp_body = resp.read().decode("utf-8") #utf-8로 인코딩
print(resp_body)#body출력
'''
#에러
try:#예외처리
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url) # url요청
    resp = urlopen(request) #url열기
    resp_body = resp.read().decode("utf-8") #utf-8로 인코딩해서 읽어오기
    print(type(resp_body), ":" ,resp_body)# python방식으로 출력 str타입


    json_result=json.loads(resp_body)
    print(type(json_result),":",json_result) #json 방식으로 출력 dict타입

    data = json_result['data'];
    print(type(data),data) #json_result[data] 키값 안에 있는 데이터출력 ,타입 list 방식
except Exception as e:
    print('%s %s' % (e, datetime.now()),file=sys.stdout) # 2개를 문자열로 출력하게따 exception 내용, 날짜시간, stdout=출력
