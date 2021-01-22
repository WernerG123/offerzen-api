import flask
from flask import request, jsonify
import bubbleSort
from bubbleSort import bubbleSort
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the home page of my application</h1> <a href=\"/api/bubbleSort\">Go here to see bubble sort</a>"

@app.route('/api/bubbleSort', methods=['GET', 'POST'])
def api_array():
    # if 'array' in request.args:
    #     myArray = list(map(int, request.args['array'].split(",")))
    #     result = bubbleSort(myArray)
    # else:
    #     return "Not calling sort: add ?array=5,4,3,2,1 as paramater to test"

    # return str(result)
    content = request.json
    result = list(content["array"])
    return str(bubbleSort(result))


app.run()