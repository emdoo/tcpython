from urllib import request, response, error, parse
import json

class client:
    def __init__(self, key:str):
        self.key = key

    def call(self, endpoint:str, selections:str="", id:str=""):
        req_url = "https://api.torn.com/%s/%s?%s" % (endpoint,id,parse.urlencode({"comment":"tcpython","key":self.key,"selections":selections}),)
        req = request.Request(req_url, headers={"User-Agent": "Chrome/126.0.0.0"}, method="GET")
        with request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))


