from flask import Flask, request
from .ocr import read_file
import base64

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_file():
    if request.method == 'POST':
        file = request.json['base64Data']
        if file:
            output = read_file(file)
            return output
