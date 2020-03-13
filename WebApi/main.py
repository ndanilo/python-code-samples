from datetime import datetime, date
from Models.item import Item
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
import json

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

item = Item()
item.Id = 123
item.Description = 'Some Description'
item.Date = datetime.now()      

#encoder sample: https://docs.python.org/3/library/json.html

properties = [ p for p in dir(item) if not p.startswith('_') ]
print(properties)

print(type(item))

x={}
for p in properties:
    x[p]=getattr(item,p)

print(x)

x=DatetimeEncoder().encode(item.__dict__)
print(f'x={x}')

class Notes(Resource):
    __items = []

    def get(self):
        item = Item()
        item.Id = 123
        item.Description = 'Some Description'
        item.Date = datetime.now()
        self.__items.append(item)

        response = app.response_class(response=json.dumps([ j.__dict__() for j in self.__items ]),status=200,mimetype='application/json')
        return response

app = Flask(__name__)
api = Api(app)

api.add_resource(Notes, '/notes')

if __name__ == '__main__':
    app.run(debug=True)