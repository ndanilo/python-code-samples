from datetime import datetime, date
from Models.item import Item
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource, inputs
import json
import random

parser = reqparse.RequestParser()
parser.add_argument('description', type=str, required=True, help='description field must to be supplied', location='json')
parser.add_argument('date', type=inputs.datetime.fromisoformat, required=True, help='date field must to be supplied', location='json')

_items=[]
class NotesList(Resource):
    def get(self):
        response =  [ j.to_json() for j in _items ], 200, {'content-type':'application/json','custom':'teste123'}
        return response
    
    def post(self):
        args = parser.parse_args()
        item = Item()
        item.Id = random.randint(1,1001)
        item.Description = args['description']
        item.Date = args['date']
        _items.append(item)

        response = item.to_json(), 201, {'content-type':'application/json','custom':'teste123'}
        return response

class NotesItem(Resource):
    def get(self, item_id):
        item = [ x.to_json() for x in _items if x.Id == item_id ]
        if not item:
            return 'invalid item identifier', 400

        response = item[0], 200, {'content-type':'application/json','custom':'teste123'}
        return response
    def delete(self, item_id):
        item = [ x for x in _items if x.Id == item_id ]
        if not item:
            return 'invalid item identifier', 400
            
        _items.remove(item[0])
        response = {"message":"removed with success"}, 200, {'content-type':'application/json','custom':'teste123'}
        return response