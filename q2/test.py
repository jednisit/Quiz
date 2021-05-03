import json
from flask import Flask,jsonify
import readjson

app = Flask(__name__)



@app.route('/')
def hello_world():
    return jsonify(readjson.read())

@app.route('/1')
def hello_world1():
    return jsonify(readjson.up())

@app.route('/2')
def hello_world2():
    return jsonify(readjson.dele())

@app.route('/3')
def hello_world3():
    return jsonify(readjson.add())

