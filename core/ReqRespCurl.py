
import pycurl
import io
import json

class Request_Response_Curl:
    def __init__(self, url, data):
        self._url = url
        self._data = data
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def postResponse(self):
        crl = pycurl.Curl()
        #crl.setopt(pycurl.VERBOSE,1)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.MAXREDIRS, 5)
        #crl.setopt(pycurl.AUTOREFERER,1)
        crl.setopt(pycurl.CONNECTTIMEOUT, 60)
        crl.setopt(pycurl.TIMEOUT, 300)
        #crl.setopt(pycurl.PROXY,proxy)
        #crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
        #crl.setopt(pycurl.NOSIGNAL, 1)
        crl.fp = io.BytesIO()
        crl.setopt(pycurl.USERAGENT, "dhgu hoho")

        # Option -d/--data <data>   HTTP POST data
        crl.setopt(crl.POSTFIELDS,  self._data)
        crl.setopt(pycurl.URL, self._url)
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)

        crl.perform()

        r = crl.fp.getvalue().decode('utf-8')
        crl.fp.close()

        return r

    def postCookieResponse(self, cookies):
        crl = pycurl.Curl()
        #crl.setopt(pycurl.VERBOSE,1)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.MAXREDIRS, 5)
        #crl.setopt(pycurl.AUTOREFERER,1)
        crl.setopt(pycurl.CONNECTTIMEOUT, 60)
        crl.setopt(pycurl.TIMEOUT, 300)
        #crl.setopt(pycurl.PROXY,proxy)
        #crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
        #crl.setopt(pycurl.NOSIGNAL, 1)
        crl.fp = io.BytesIO()
        crl.setopt(pycurl.USERAGENT, "dhgu hoho")

        # Option -d/--data <data>   HTTP POST data
        crl.setopt(crl.POSTFIELDS,  self._data)
        crl.setopt(pycurl.URL, self._url)
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)

        # Option -b/--cookie <name=string/file> Cookie string or file to read cookies from
        # Note: must be a string, not a file object.
        crl.setopt(pycurl.COOKIEFILE, cookies)

        # Option -c/--cookie-jar <file> Write cookies to this file after operation
        # Note: must be a string, not a file object.
        crl.setopt(pycurl.COOKIEJAR, cookies)

        crl.perform()

        r = crl.fp.getvalue().decode('utf-8')
        crl.fp.close()

        return r

if __name__ == "__main__":
    u = 'http://ware.m.jd.com/client.action?functionId=skuDyInfo&clientVersion=4.0.0&client=android&osVersion=4.0.3&screen=960*540&networkType=wifi&pin=ljzh347'
    d = 'body={"skuId":"782200"}'
    rr = Request_Response_Curl(u, d)
    r = rr.postResponse()
    #print json.loads(r)
    print r
