import flask
from flask import request, jsonify
import bubbleSort
from bubbleSort import *
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the home page of my application</h1> <a href=\"/api/bubbleSort\">Go here to see bubble sort</a>"

@app.route('/api/bubbleSort', methods=['GET', 'POST'])
def api_array():
    content = request.json
    
    result = list(content["array"])

    return str(Sorter.sort(result))


app.run(host='0.0.0.0')