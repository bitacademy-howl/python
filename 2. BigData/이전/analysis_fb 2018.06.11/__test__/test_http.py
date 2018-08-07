# http test
import sys
from urllib.request import Request, urlopen
from urllib import error
from datetime import *

try:

    url = "http://www.naver.com"
    # url = "http://www.nadsfgsdfg.c12e213asom"

    request = Request(url)

    resp = urlopen(request)

    resp_body = resp.read().decode("utf-8")

    print(resp_body)
except error.URLError as e:
    # print("%s %s" % (e, datetime.now()), file=sys.stderr)
    pass
