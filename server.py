#!/usr/bin/env python
# coding: utf-8
# Copyright 2013 Abram Hindle
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You can start this by executing it in python:
# python server.py
#
# remember to:
#     pip install flask


import flask
from flask import Flask, request
import json
app = Flask(__name__)
app.debug = True
import pdb

# An example world
# {
#    'a':{'x':1, 'y':2},
#    'b':{'x':2, 'y':3}
# }

class World:
    def __init__(self):
        self.clear()
        
    def update(self, entity, key, value):
        entry = self.space.get(entity,dict())
        entry[key] = value
        self.space[entity] = entry

    def set(self, entity, data):
        self.space[entity] = data

    def clear(self):
        self.space = dict()

    def get(self, entity):
        return self.space.get(entity,dict())
    
    def world(self):
        return self.space

myWorld = World()          

def flask_post_json():
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data.decode("utf8") != u''):
        return json.loads(request.data.decode("utf8"))
    else:
        return json.loads(request.form.keys()[0])

@app.route("/")
def hello():
    return flask.redirect('static/index.html')

@app.route("/entity/<entity>", methods=['POST','PUT'])
def update(entity):
    pdb.set_trace()
    # try:
    #     data = flask_post_json()
    # except json.decoder.JSONDecodeError as e:
    #     v = request.data.decode("utf8")[1:-1]
    #     new = v.strip('{')
    #     new = new.strip('}')
    #     new = new.split(',')
    #     data = {}
    #     for item in new:
    #         t = item.split(':')
    #         data[t[0]]=t[1]
    #     data = json.dumps(data, indent=4, sort_keys=True)
    # pdb.set_trace()
    # if request.method =="PUT":
    #     myWorld.set(entity, data)
    # elif request.method =="POST":
    #     return
    
    return world()

@app.route("/world", methods=['POST','GET'])    
def world():
    return flask.jsonify(myWorld.world())

@app.route("/entity/<entity>")    
def get_entity(entity):
    e = myWorld.get(entity)
    return flask.jsonify(e)

@app.route("/clear", methods=['POST','GET'])
def clear():
    myWorld.clear()
    return flask.jsonify(dict())

if __name__ == "__main__":
    app.run()
