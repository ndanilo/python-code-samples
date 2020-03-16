from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from resources2.notes import NotesList, NotesItem

app = Flask(__name__)
api = Api(app)

api.add_resource(NotesList, '/notes')
api.add_resource(NotesItem, '/notes/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)