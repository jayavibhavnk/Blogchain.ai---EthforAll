
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import datetime

from main import blog_to_ipfs

app = Flask(__name__)
CORS(app)
employees = []

@app.route("/")
def hello():
    return {"server":"active"}

@app.route('/blog',methods=['POST'])
@cross_origin()
def blogify():
    blog_json = request.get_json()
    #print(blog_json)
    statement = blog_to_ipfs(blog_json)
    return {"response" : statement}

#falsk because of nikhil 