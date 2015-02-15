# -*- coding:utf-8 -*-

import requests
import json

class Request_Response:
	def __init__(self):
		self._url = ''
		self._data = ''

	

url = 'http://ware.m.jd.com/client.action?functionId=skuDyInfo&clientVersion=4.0.0&client=android&osVersion=4.0.3&screen=960*540&networkType=wifi&pin=ljzh347'
#post_data = {'skuId':'1457441393'}

str = '1457441393'

post_data = "body={'skuId':'" + str + "'}"

print post_data

headers = {"Content-Type": "application/x-www-form-urlencoded"}

r = requests.post(url, data=post_data, headers=headers)

print r.json()
