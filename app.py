import urllib
import json
import os
from lib.DataYuge import DataYuge


from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    if str(req["result"]["action"]) == "getListOFSuggestions":
        try:
            data = req["result"]["parameters"]["BrandNames"]
            cat = req["result"]["contexts"][0]["parameters"]["Category"]
            res = DataYuge.getSearchProductList(data + " " + cat)
        except(IndexError):
            return {"result": "Parameters not found"}
    elif str(req["result"]["action"]) == "getListOfComparedDetails":
        try:
            prodId = req["result"]["parameters"]["any"]
            res = DataYuge.getProductComparisonDetails(prodId)
        except(IndexError):
            return {"result": "Work in progress"}
    else:
        return {"Answer":"Action not found"}



    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')