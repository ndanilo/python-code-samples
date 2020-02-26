from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

class Quotes(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('name', type=str, help='Name to charge for this resource', required=True)

    def get(self):
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }, 200
    def post(self):
        args = self.__parser.parse_args()
        return 'forced error', 500
        return args, 201

app = Flask(__name__)
api = Api(app)

api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)