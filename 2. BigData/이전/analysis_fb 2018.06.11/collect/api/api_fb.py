# FB API Wrapper Function

# 파이썬은 상수 변수의 개념이 있지 않지만 대문자로 상수임을 명시하는 관례를 따른다.
from urllib.parse import urlencode
from .web_request import json_request

BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'
ACCESS_TOKEN = "EAACEdEose0cBAC9UETLkfD4n5OwjNi4vDOEQ0YDxrOgHVU5ms8AheCDxUd13OUhEk5jtsWMGRKVz5jZBQmoYy9J1ZBc0EKfjfw9iSBOtNsyZACi8JrJ6oFhZA7wGlRYMervbkR3mv7zJkGZBebnCYwZAZCrg6w4oRD6ASDF0ZBItEgVQmg1YUDgLTreiMYHpacj0l1wZABYNnZBVdWmAulJHI5qjzZCNypvMkwZD"

def fb_gen_url(
        base=BASE_URL_FB_API,
        node='', **params
):
    # print("params : ", params)
    url = "%s/%s/?%s" % (base, node, urlencode(params))
    return url


# 실제 URL에 모든 정보가 담겨있지 않기 위해 Post 방식으로 id를 받아와 url에 사용한다..
# 페이스북 api 탐색기에서 액세스 토큰을 받아서 node ID를 가져오는 함수를 지정
def fb_name_to_id(pageName):
    url = fb_gen_url(node=pageName, access_token = ACCESS_TOKEN)
    json_result = json_request(url=url)
    # print(json_result)
    # print(json_result.get("id"))
    return json_result.get("id")


# 실제 포스트방식에 사용될 URL 생성 - with ACCESS_TOKEN
def fb_fetch_posts(pageName, since, until, limit=50):
    # 자세한 URL 생성 fields 는 facebook API 참조
    url = fb_gen_url(node=fb_name_to_id(pageName)+"/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=limit,
                     access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    print("페이스북 dataSet의 url : ", url)
    print("최종 데이터 셋 : ", json_result)