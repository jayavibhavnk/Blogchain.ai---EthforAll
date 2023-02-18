
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import requests
import json

#false express server

url = "https://data.mongodb-api.com/app/data-stoly/endpoint/data/v1/action/find"

headers = {
    "Content-Type": "application/json",
    "apiKey": "V2jAj0WKRWitf1Tzw0UdTg5cCcWckSZLErF4AAOcVEJavrOO65MY6Ia65uOQDazQ"
}

payload = {
    "dataSource": "Cluster0",
    "database": "Ethforall_blogs",
    "collection": "blogs"
}

def mongo_resp():
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.text
    data = json.loads(data)
    return data

app = Flask(__name__)
CORS(app)
employees = []

@app.route("/")
def hello():
    return {"server":"active"}

@app.route('/json',methods=['GET'])
@cross_origin()
def blogify():
    return mongo_resp()


@app.route('/array',methods=['GET'])
@cross_origin()
def blogify1():
    k = mongo_resp()
    l = k['documents']
    l.reverse()
    return l

if __name__ == '__main__':
    app.run(debug = True, port=8080)