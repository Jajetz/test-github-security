#!/usr/bin/env python3

from flask import Flask, request, render_template
import pickle
import yaml
import ruamel.yaml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    parameter = request.values.get('parameter')

    parameter1 = eval(parameter)
    parameter2 = pickle.loads(parameter)
    parameter3 = yaml.load(parameter)
    parameter4 = ruamel.yaml.load(parameter)
    parameter5 = eval(parameter)

    res = render_template('index.html', parameter=parameter)

    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
