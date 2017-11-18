from lib.JsonUtils import JsonUtils


class FBFormat(object):
    def getQuickRepliesSuggestions(res):

        return {
            "speech": "",
            "messages": [
                {"type": 2,
                 "platform": "facebook",
                 "title": "Below are the List of Suggestions?",
                 "replies": res["keywords"]
                 }
            ]
        }

    def getQuickRepliesSearch(res, string):
        print(string)
        titles = []
        for prod in res:
            title = prod["product_title"]
            if title not in titles:
                if string.lower() in title.lower():
                    titles.append(title)

        return {
            "speech": "",
            "messages": [
                {"type": 2,
                 "platform": "facebook",
                 "title": "Below are the List of Suggestions?",
                 "replies": titles
                 }
            ]
        }
    def getQuickReplyWhenEmptySearch(self):
        return {
            "speech": "",
            "messages": [
                {"type": 2,
                 "platform": "facebook",
                 "title": "Could not find what you are looking for?",
                 "replies": [
                         "New Request",
                         "More Suggestions"
                 ]
                 }
            ]
        }
    def getHorCarouselSearch(res, string, type):

        if type == "search":
            templates = FBFormat.getCarouselTemplateForSearch(res,string)

        if type == "compare":
            templates = FBFormat.getCarouselTemplateForCompare(res)

        if len(templates)<1:
            return FBFormat.getQuickReplyWhenEmptySearch(FBFormat)

        return {
            "speech": "",
            "source": "",
            "displayText": "Here you go: ",
            "data": {
                "facebook": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "image_aspect_ratio":"square",
                            "elements":
                                templates

                        }
                    }
                }
            }
        }

    def getCarouselTemplateForSearch(res,string):
        elements = []
        for prod in res:
            title = prod["product_title"]
            if string.lower() in title.lower():
                price = "Rs " + str(prod["product_lowest_price"])
                imgurl = str(prod["product_image"]).replace("/image/", "/image/thumb-")
                produrl = prod["product_link"]
                element = {
                    "title": title,
                    "subtitle": price,
                    "image_url": imgurl,
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Compare Product",
                            "webview_height_ratio": "tall",
                            "payload": "Compare Product " + str(produrl).replace(
                                "https://price-api.datayuge.com/api/v1/compare/detail?id=", "")
                        }
                    ]
                }

                if len(elements) < 10:
                    elements.append(element)
        return elements

    def getCarouselTemplateForCompare(res):
        elements = []
        title = res["product_name"]
        imgurl = res["product_images"][0]
        rating = res["product_ratings"]
        stores = res["stores"]
        print(title +" "+imgurl)
        for store in stores:
            for key in store.keys():

                try:
                    if str(key) in ("amazon","flipkart","snapdeal"):
                        print(key)
                        price = store[str(key)]["product_price"]
                        prod_url = store[str(key)]["product_store_url"]
                        prod_offer = store[str(key)]["product_offer"]
                        if prod_offer == "":
                            prod_offer = "No Offer"
                        prod_delivery = store[str(key)]["product_delivery"]
                        subtitle = "Rating %s stars \n%s price : Rs %s \n Delivery time : %s days"%(rating,str(key).title(),price,prod_delivery)
                        element = {
                            "title": title,
                            "subtitle": subtitle,
                            "image_url": imgurl,
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy From " +str(key).title(),
                                    "webview_height_ratio": "tall",
                                    "url": prod_url
                                },{
                               "type": "postback",
                                "title": "New Request",
                                "webview_height_ratio": "tall",
                                "payload": "Lets try again ?"
                                }
                            ]
                        }
                        elements.append(element)
                except(IndexError):
                    print("Index Error " + str(key))
                except(TypeError):
                    print("Type Error " + str(key))
        return elements
