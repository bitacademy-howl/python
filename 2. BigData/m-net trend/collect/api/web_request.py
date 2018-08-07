from datetime import datetime
import sys
from urllib.request import Request, urlopen

def html_request(
        url='',
        encoding='utf-8',
        success=None):

    try:
        request = Request(url)
        resp = urlopen(request)
        print(resp)
        # print(resp.read())

        try:
            html_response = resp.read()
            html = html_response.decode(encoding)
        except UnicodeDecodeError:
            html = html_response.decode(encoding, 'replace')

        # html = resp.read()
        print(html)
        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return html
        else:
            success(html)

    except Exception as e:
        print('%s %s' % (e, datetime.now()), file=sys.stderr)

def json_request():
