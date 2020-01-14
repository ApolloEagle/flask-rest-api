from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from .ocr import read_file
import werkzeug

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

class ProcessFile(Resource):
    def post(self):
        data = parser.parse_args()
        photo = data['file']
        return photo

api.add_resource(ProcessFile, '/')