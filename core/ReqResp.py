# -*- coding:utf-8 -*-

import requests
import json

class Request_Response:
    def __init__(self, url, data, headers):
        self._url = url
        self._data = data
        self._headers = headers

    def postResponse(self):
        r = requests.post(self._url, data = self._data, headers = self._headers)
        return r

if __name__ == "__main__":
    u = 'http://ware.m.jd.com/client.action?functionId=skuDyInfo&clientVersion=4.0.0&client=android&osVersion=4.0.3&screen=960*540&networkType=wifi&pin=ljzh347'
    d = 'body={"skuId":"1457441393"}'
    h = {"Content-Type": "application/x-www-form-urlencoded"}
    rr = Request_Response(u, d, h)
    r = rr.postResponse()
    print r.text
