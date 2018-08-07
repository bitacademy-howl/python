import json
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import sys

def crawling(url = None,
             encoding = 'utf-8',
             by_json = False,
             pre_processing = lambda result : result,
             store_function = lambda result : result,
             err=lambda e: e.print('%s : %s' % (e, datetime.now()), file=sys.stderr)
             ):
    # 크롤링 함수 설명 : 크롤링 함수는 url을 전달받아 html 및 json response를 받고,
    #                    전처리 및 저장을 할지 여부를 판단하며, 리턴값이 무조건 있는 함수로 정의한다.
    #                    리턴값은 html 및 json 응답과 이에대한 전처리 까지의 내용을 정의한다.

    try:
        request = Request(url)
        response = urlopen()

        if by_json == True:
            json.loads(response)

        try:
            receive = response.read()

            # 아래는 외부에서 함수를 인자로 전달받아 수행하도록 구현
            pre_processed = pre_processing(receive)
            stored = store_function(pre_processing)

            result = receive.decode(encoding)

        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

    # 이 아래는 다양한 http request 에 대한 예외를 포함한다.
    # 지속적으로 업데이트 해볼 것
    except Exception as e:
        err(e)

    return result

# goal
# 크롤링 하고자 하는 웹의 구성방식에 구애받지 않고 외부에서 모든인자를 전달받아 url을 만드는 함수를 작성
# 단, 함수 자체가 재사용 가능하다는 말이지 웹에대한 정보 없이 사용가능하다는 말은 아니다.
def mk_url(
        end_point = None,
        node = None,
        method = 'get',
        **params):

    if method = None:

    elif method == 'get':
        url = '%s/%s/?%s' % (end_point, node, urlencode(params))
    elif method == 'post':
        print('포스트 방식은 지원하지 않음')
        sys.exit(9)
    else:
        pass
    return url

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)