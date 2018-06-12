#http test

from urllib.request import  Request, urlopen # 모듈 , request: url을 요청, urlopen: 서버에서 데이터를 받아옴.
from datetime import *
'''
url = 'http://www.naver.com'
request = Request(url) # url요청
resp = urlopen(request) #url열기
resp_body = resp.read().decode("utf-8") #utf-8로 인코딩
print(resp_body)#body출력
'''
#에러
try:#예외처리
    url = 'http://www.naver.com'
    request = Request(url) # url요청
    resp = urlopen(request) #url열기
    resp_body = resp.read().decode("utf-8") #utf-8로 인코딩
    print(resp_body)#body출력
except Exception as e:
    print('%s %s' % (e, datetime.now())) # 2개를 문자열로 출력하게따 exception 내용, 날짜시간, stdout=출력

'''
System.out.println('hell world'); #stdout

'''
