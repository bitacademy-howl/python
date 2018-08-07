from analysis_fb.collect.api import api_fb

# url = api_fb.fb_gen_url(node='jtbcnews',
#                   a=10,
#                   b=20,
#                   s="kasgsadfg",
#                   kasd='aoosoodod')
# print(url)

# get 방식의 url 생성 및 post 방식의 url token 받아오기
# id = api_fb.fb_name_to_id("jtbcnews")
# print(id)

api_fb.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-12-31')
api_fb.fb_fetch_get('jtbcnews', '2017-01-01', '2017-12-31')