from flask import Flask, g
import markdown
import os
import shelve
from flask_restful import Resource, Api, reqparse, request
import csv
#creo la instancia de Flask
app = Flask(__name__)

# Create the API
api = Api(app)
'''
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('devices.db')
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
'''

@app.route("/")
def hello():
    """present some documentacion"""
    # open the readme file
    print(os.path.dirname(app.root_path))
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        #convcert to html
        return markdown.markdown(content)

class DeviceList(Resource):
    def get(self):
        return {'message': 'OK', 'ECU': '02,03,04'}, 200
    
    def post(self):

        parser = reqparse.RequestParser()
        print(request.json)
        parser.add_argument('identifier', required=True, help='este dato es obligatorio')
        parser.add_argument('timeStamp', required=True)
        parser.add_argument('ECU')
        parser.add_argument('acelerometer')
        parser.add_argument('GPS')
        
        # Parse the arguments into an object
        args = parser.parse_args()
        # this is in case we use shelves instead of the mighty all power CSV
        '''
        shelf = get_db()
        print(shelf)
        shelf[args['identifier']] = args
        '''
        with open("dump.csv", "a") as pepe:
            w = csv.DictWriter(pepe, args.keys())
            w.writerow(args)
            

        return {'message': 'data Recieve'}, 201

api.add_resource(DeviceList, '/data')
