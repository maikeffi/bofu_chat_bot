import requests
import json
host = "https://price-api.datayuge.com"
apiv1 = "/api/v1/compare"
api_key = "FbJf8qvu0pOQoRyK4pnCPB33hArX8eS4VVd"

class DataYuge(object):


    def getSuggestionList(self,string):
        path = "/search/suggest?product={string}&api_key={secretkey}"
        url = host + apiv1 + path.replace("{string}",string).replace("{secretkey}",api_key)
        res = self.processUrl(url)
        return res


    def processUrl(self,url):
        r = requests.get(url)
        data = json.loads(r.text)
        return data["keywords"]