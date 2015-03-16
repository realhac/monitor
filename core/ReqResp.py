# -*- coding:utf-8 -*-

import requests
import json

class Request_Response:
    def __init__(self, url, data):
        self._url = url
        self._data = data
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def postResponse(self):
        r = requests.post(self._url, data = self._data, headers = self._headers)
        return r

    #r.cookies['example_cookie_name']
    #cookies = dict(cookies_are='working')
    def postCookieResponse(self, cookies):
        r = requests.post(self._url, data = self._data, headers = self._headers, cookies=cookies)
        return r

if __name__ == "__main__":
    u = 'http://ware.m.jd.com/client.action?functionId=skuDyInfo&clientVersion=4.0.0&client=android&osVersion=4.0.3&screen=960*540&networkType=wifi&pin=ljzh347'
    d = 'body={"skuId":"782200"}'
    rr = Request_Response(u, d)
    r = rr.postResponse()
    print r.text
