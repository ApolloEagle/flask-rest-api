from flask import Flask, request
from .ocr import read_file

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file submitted'
        file = request.files['file']
        if file:
            output = read_file(file)
            return output
