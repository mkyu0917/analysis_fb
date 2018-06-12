import os
import json
from datetime import datetime, timedelta #date객체 delta는 함수
from.api import api

RESULT_DIRECTORY='__results__/crawling/'


def preprocess_post(post):
    # 공유수
    if'shares' not in post:
        post['count_shares']=0
    else:
        post['count_shares'] = post['shares']['count'] #공유수
    #리액션수
    if 'reactions' not in post:
        post['count_reactions']=0
    else:
        post['count_reactions'] = post['reaction']['summary']['total_count']
    #코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']

    #kst = utc +9
    kst = datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000') #스트링을 타임객체로 변환
    kst = kst + timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling(pagename, since, until):#크롤링함수
    results = []
    filename= '%s/%s_%s_%s.json' % (
        RESULT_DIRECTORY,
        pagename,
        since,
        until ) #저장할 이름 함수를 불러와서 포멧팅, 저장 확장자는 json



    for posts in api.fb_fetch_posts(pagename, since, until):  # fb_fetch에서 값을 받고 돌려서 계속 프린트
        for post in posts:
            preprocess_post(post)

        results += posts
        print(posts)

     # save results to file(저장, 적재)
    with open(filename, "w", encoding='utf-8') as outfile: #쓰기모드 utf-8로 인코딩해라
        json_string=json.dumps(
            results,
            indent=4,
            sort_keys=True,
            ensure_ascii=False) #제이슨을 만들때 띄어쓰기 4칸해라 indent, 키갑슬 정렬 sort_key,
        outfile.write(json_string)



if os.path.exists(RESULT_DIRECTORY) is False: #처음실행했을때 디렉토리가 없으면 맹그러라
    os.makedirs(RESULT_DIRECTORY)