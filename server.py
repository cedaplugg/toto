from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api
import json
import random
import werkzeug
from werkzeug.security import safe_str_cmp
import pymongo
import hashlib
from utils.random_string import random_string


conn = pymongo.MongoClient('mongodb://root:arin4242@localhost:27017')#database connecting
db = conn.toto
collection = db.info
app = Flask(__name__)
api = Api(app)

class signUp(Resource):
    def get(self):
        code = random_string(6)
        return {'code': code}
    

class bet(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("code", type = str, required = True)
        parser.add_argument("bet")
        args = parser.args()

class auth(Resource):
    def post(self):
        pass

class history(Resource):
    def get(self):
        return collection.distinct("code")[0]['history']

class bet2(Resource):#genius
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("bet", required = True)
        args = parser.args()
        return args['bet']

