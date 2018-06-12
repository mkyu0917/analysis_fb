from analysis_fb.collect.api import api
''' 
url = api.fb_gen_url(
                     node='jtbcnews',
                     a=10, b=20,
                    s='내다')

print(url)
'''

'''
id = api.fb_name_to_id("jtbcnews")
print(id)
'''
#결과 값을 받아옴
for posts in api.fb_fetch_posts('jtbcnews', '2017-01-01','2017-12-31'): #fb_fetch에서 값을 받고 돌려서 계속 프린트
    print(posts)
    print(len(posts))