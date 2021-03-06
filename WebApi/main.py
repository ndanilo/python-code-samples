from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from resources2.notes import NotesList, NotesItem
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://root:root@localhost:1433/python_db1?driver=SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
'''

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
import tables
definitions = tables.defineDb(db)

'''
api.add_resource(NotesList, '/notes')
api.add_resource(NotesItem, '/notes/<int:item_id>')
'''

if __name__ == '__main__':
    manager.run()
    #app.run(debug=True)