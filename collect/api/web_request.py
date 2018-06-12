import sys
from urllib.request import  Request, urlopen # 모듈
from datetime import *
import json


def html_request(

        url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list',  #default 파라미터
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)  # 2개를 문자열로 출력하게따 exception 내용, 날짜시간, stdout=출력
 ):

    try:  # 예외처리
        request = Request(url)  # url요청
        resp = urlopen(request)  # url열기
        html = resp.read().decode(encoding)  # utf-8로 인코딩해서 읽어오기

        print('%s: success for request[%s]' %(datetime.now(),url))

        if callable(success) is False:
            return html
        else:
            success(html)

    except Exception as e:
        if callable(error) is True: #함수를 부를 수 있는지 없는지
            error(e)

#제이슨 기본함수
def json_request(
        url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)
        ):
    # test json request에서 호출한 변수를 매개변수가 받아서 try문 실행

    try:
        request = Request(url)
        resp = urlopen(request)
        resp_body = resp.read().decode(encoding)

        json_result = json.loads(resp_body)
        print('%s: success for request[%s]' %(datetime.now(),url))

        if callable(success) is False: #success가 가르키는 함수가 실행가능 하냐 안되냐! 여기서 success는 success_fetch_user_list를 가리킴
            return json_result        #false라서 실행안되고 건너뜀
        else:
            success(json_result) #success함수를 호출하고 json_reusult값을 test_json_request 함수에 전달.

    except Exception as e:
        if callable(error) is True:
                error(e)


