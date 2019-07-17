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
    def get(self)
        return {'code': "code"}

