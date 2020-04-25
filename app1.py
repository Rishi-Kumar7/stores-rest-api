 from flask import Flask# making a flask app, getting the requests
from flask_restful  import  Api # Resource: required data, Api: making api of an flask app, reqparse: parsing the data
from flask_jwt import JWT # JWT: key for authentication, jwt_required: decorator for authentication , in this case above GET
from security import authenticate, identity # security: check security.py
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList


app = Flask(__name__)# Flask app with a unique name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'rishikumar29' # pin for authentication of the app

api = Api(app)# converting app to Api for ease




jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Store,'/store/<string:name>')#route for single Item
print("resource item ADDDED")
api.add_resource(Item,'/item/<string:name>')#route for single Item
print("resource item ADDDED")
api.add_resource(ItemList, '/items')# route for the complete item list
print("resource items ADDED")
api.add_resource(StoreList,'/stores')#route for single Item
print("resource item ADDDED")
api.add_resource(UserRegister, '/register')
print("UserRegister resource ADDED")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
