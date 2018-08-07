
def url_gen(END_POINT='', NODE='', YEAR=0, MONTH=0, DATE=0):
    url = '%s%s%s' % (END_POINT, NODE, '{0:04d}{1:02d}'.format(YEAR, MONTH))
    print('url = ', url)
    return url

