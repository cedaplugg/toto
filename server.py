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
        parser = reqparse.RequestParser()
        parser.add_argument('code', type = str, required = True)
        args = parser.parse_args()
        if collection.distinct(args)[0]['balance']:
            return collection.distinct(args['code'])[0]['balance']
        return {'msg':'wrong code'}
        
class history(Resource):
    def get(self):
        return collection.distinct("code")[0]['history']

class bet2(Resource):#genius
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', type = str, required = True)
        parser.add_argument("bet", type = str, required = True)
        parser.add_argument("quan", type = int, required = True)
        parser.add_argument("odds", type = float, required = True)
        parser.add_argument("predict", type = int, reqired = True)
        args = parser.parse_args()
        if collection
        collection.insert()


api.add_resource(bet2, '/')
app.run(port=5000)