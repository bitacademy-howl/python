# import pycurl
#
# class ContentCallback:
#     def __init__(self):
#         self.contents = ''
#
#     def content_callback(self, buf):
#         self.contents = self.contents + buf
#
# if __name__ == '__main__':
#     t = ContentCallback()
#     curlObj = pycurl.Curl()
#     print(curlObj)
#     curlObj.setopt(curlObj.URL, 'http://www.naver.com')
#     curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
#     curlObj.perform()
#     curlObj.close()
#     print
#     t.contents
