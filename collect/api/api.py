#FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN='EAACEdEose0cBAC9YZCZAxb7rtAnG7BDa3suFlZAH0ZAUtRsjLR2ns7S5CWkIAexKo36ZALgkLJUx36QmU5wN4F9xKfYzWMYSZAfZAZB6SBY53OoxZAqpubek5cwTAlNzpgiI51CzWRqWZBX0LT5yzBDdYCg4JTgU2XiD8b819TfuZBtXL1MQR4eRchNAeo0b4Xqijc9gHRR869EcAZDZD'
BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'


def fb_gen_url(
        base=BASE_URL_FB_API,
        node='',
        **params):
        url = '%s/%s/?%s' % (base, node, urlencode(params))
        return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result =json_request(url=url)
    return json_result.get('id')

 #모듈화
def fb_fetch_posts(pagename, since, until):
        url = fb_gen_url(node=fb_name_to_id(pagename) + '/posts',
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN)
        json_result = json_request(url=url)
        #print(json_result)


        #6/12
        #results = []
        isnext = True #이게 true면 루프를 돔
        while isnext is True: #탈출조건필요

            json_result = json_request(url=url)

            paging =None if json_result is None else json_result.get('paging')  #페이징 정보를빼옴. python 3항 연산자
            posts = None if json_result is None else json_result.get('data')

            #results+=posts #50개씩 리스트로
            url =  None if paging is None else paging.get('next')  #마지막데이터는 Null
            isnext = url is not None  #None이 아니면 True 반환 None이면 루프탈출

            yield posts #값을 계속전달
        #return results



