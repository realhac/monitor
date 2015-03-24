# -*- coding:utf-8 -*-

import sys

sys.path.append('..')

from core.TestCases import Test_Cases
from core.ReqRespCurl import Request_Response_Curl
from core.JsonAnalyze import Json_Analyze

class Demo_Test_Case(Test_Cases):
    def __init__(self):
        Test_Cases.__init__(self)

        #Init parameter in url
        self._reqProtocol = "http://"
        self._rhost = "ware.m.jd.com"
        self._bhost = "bware.m.jd.com"
        self._rreqAPI = "/client.action?functionId=skuDyInfo&"
        self._breqAPI = "/client.action?functionId=skuDyInfo&"
        self._client = "android"
        self._clientVersion = "4.1.0"
        self._osVersion = "4.2.2"
        self._area = ["28_3080_4004_0", "5_274_49707_0"]
        self._skuId = ["782200", "1356751968"]
        
    def setUp(self):
        Test_Cases.setUp(self)
        
        self._rurl = []
        self._burl = []
        self._data = []
        
        #make url string, live url and beta url
        for _area in self._area:
            self._rurl.append(self._reqProtocol + self._rhost + self._rreqAPI + "clientVersion=" + self._clientVersion + \
                "&client=" + self._client + "&osVersion=" + self._osVersion + "&screen=960*540&networkType=wifi&area=" + _area)
            self._burl.append(self._reqProtocol + self._bhost + self._breqAPI + "clientVersion=" + self._clientVersion + \
                "&client=" + self._client + "&osVersion=" + self._osVersion + "&screen=960*540&networkType=wifi&area=" + _area)

        #make body string
        for _skuId in self._skuId:
            self._data.append('body={"skuId":"' + _skuId + '"}')
        
    def testRun(self):
        Test_Cases.testRun(self)
        
        for _d in self._data:
            for i in range(0, len(self._rurl)):
                r_rrc = Request_Response_Curl(self._rurl[i], _d)
                (rc, rr) = r_rrc.postResponse()

                b_rrc = Request_Response_Curl(self._burl[i], _d)
                (bc, br) = b_rrc.postResponse()

                #print json.loads(r)
                print rc
                print br

    def tearDown(self):
        Test_Cases.tearDown(self)

    def main(self):
        self.setUp()
        self.testRun()
        self.tearDown()

if __name__ == "__main__":
    dtc = Demo_Test_Case()
    dtc.main()
