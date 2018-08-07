import sys
from urllib.request import Request, urlopen
from urllib import error
from datetime import *
import json


try:
    url = "http://kickscar.cafe24.com:8080/myapp-api/api/user/list"
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(type(resp_body), resp_body, sep=" : ")

    json_result = json.loads(resp_body)
    print(type(json_result), json_result, sep=" : ")

    data = json_result['data']
    print(type(data), data)

    resultDict = data[0]

    for i in resultDict.items():
        print(i)

except error.URLError as e:
    # print("%s %s" % (e, datetime.now()), file=sys.stderr)
    pass