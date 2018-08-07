import config
from collect.api.web_request import html_request
from .url_generator import url_gen
import sys
import urllib

def fetch_data(FETCH='', **conf):
    print(conf)
    if FETCH:
        # print(FETCH)
        url = url_gen(**conf)
        # print(url)
        html = html_request(url)
        print('responsed html : ', html)


    # print(*common.values())
    # print(common['NODE'])
    #
    # print(common, type(common))
    # print(*common)