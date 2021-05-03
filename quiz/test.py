import os
import readJson
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    x = readJson.showitem()
    return jsonify(x)


app.env="development"
app.run(debug=True)
