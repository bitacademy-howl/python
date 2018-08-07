from __test__.test_json import json_result
from analysis_fb.collect.api import web_request as wr


url = "http://kickscar.cafe24.com:8080/myapp-api/api/user/list"

# json_result = wr.json_request(url)
# print(json_result)

def success_fetch_user_list(response):
    print(response)

def error_fetch_user_list(e):
    print(e)

url = "http://kickscar.cafe2.com:8080/myapp-api/api/user/list"

wr.json_request(url=url,
                success=success_fetch_user_list,
                error=error_fetch_user_list)
