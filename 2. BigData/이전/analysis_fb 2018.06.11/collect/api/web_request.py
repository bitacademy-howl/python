import collections
import sys
from urllib.request import Request, urlopen
from urllib import error
from datetime import *
import json

def print_URLError(e):
    pass

def print_error(e):
    print("%s %s" % (e, datetime.now()), file=sys.stderr)

def html_request(url='',
                 encoding='utf-8',
                 success=None,
                 error = lambda e: print("%s %s" % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)

        # Request 성공 시 URL 및 디코딩 결과를 로그로 남김
        print('%s : SUCCESS FOR REQUEST[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return html
        else:
            success(html)
        # success(html)   # 위와 동일 하나 가독성이 위가 더 익숙하다..ㅠㅠ

    except Exception as e:
        if callable(error) is True:
            error()
        print_URLError()

def json_request(url='',
                 encoding='utf-8',
                 success=None,
                 error = lambda e: print_error(e)):

    try:
        request = Request(url)
        resp = urlopen(request)
        json_body = resp.read().decode(encoding)

        json_result = json.loads(json_body)

        # Request 성공 시 URL 및 디코딩 결과를 로그로 남김
        print('%s : SUCCESS FOR REQUEST[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)
        else:
            print_URLError(e)

# a = json_request(, success=lambda json_result: print(json_result), error=lambda e:print_error())
