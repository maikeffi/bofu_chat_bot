import requests
import json
from lib.FBFormat import FBFormat
host = "https://price-api.datayuge.com"
apiv1 = "/api/v1/compare"
api_key = "FbJf8qvu0pOQoRyK4pnCPB33hArX8eS4VVd"

class DataYuge(object):


    def getSuggestionList(string):
        path = "/search/suggest?product={string}&api_key={secretkey}"
        url = host + apiv1 + path.replace("{string}",string).replace("{secretkey}",api_key)
        res = DataYuge.processUrl(url)
        res = FBFormat.getQuickRepliesSuggestions(res)
        return res

    def getSearchProductList(string):
        path = "/search?product={string}&api_key={secretkey}"
        url = host + apiv1 + path.replace("{string}", string).replace("{secretkey}", api_key)
        #print(url)
        b = string.split()[0]
        res = DataYuge.processUrl(url)["data"]
        res = FBFormat.getHorCarouselSearch(res,b,"search")
        return res

    def getProductComparisonDetails(prodId):
        path = "/detail?id={productID}&api_key={secretkey}"
        url = host + apiv1 + path.replace("{productID}",prodId).replace("{secretkey}", api_key)
        res = DataYuge.processUrl(url)["data"]
        res = FBFormat.getHorCarouselSearch(res, prodId, "compare")
        return res
    def processUrl(url):
        r = requests.get(url)
        data = json.loads(r.text)
        return data