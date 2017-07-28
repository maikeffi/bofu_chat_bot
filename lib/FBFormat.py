from lib.JsonUtils import JsonUtils

class FBFormat(object):

    def getQuickRepliesSuggestions(res):



        return {
            "speech": "",
            "messages": [
                {   "type": 2,
                    "platform": "facebook",
                    "title": "Below are the List of Suggestions?",
                    "replies": res["keywords"]
                 }
            ]
        }


