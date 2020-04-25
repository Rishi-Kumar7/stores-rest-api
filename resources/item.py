

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel




class Item(Resource):# class for the Item
    parser = reqparse.RequestParser() #using parser
    parser.add_argument('price',  # selecting 'price' as an item content to be updated
            type =float,
            required =True,
            help="This field cannot be left blank!")

    parser.add_argument('store_id',  # selecting 'price' as an item content to be updated
            type =int,
            required =True,
            help="every item needs a store_id")

    @jwt_required()# mentioned above #jwt_required
    def get(self, name):# GET:client request for item name, takes up only name of the item
        item =ItemModel.find_by_name(name)
        print("find_by_name executed")
        if item:
            return item.json()
        return {'message': 'item not found'}, 404





    def post(self, name):#POST: client giving data to the server to save
        if ItemModel.find_by_name(name):

            return{'message':"An item with name '{}' already exists".format(name)}, 400


        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id']) # item name and price


        print("ItemModel created with ar gs name: {} and price: {}".format(name, data['price']))


        try:
            item.save_to_db()
            print("save_to_db executed")
        except:
            return {'message':'An error occured inserting the item'}, 500 # internal sever error
            print("save_to_db not executed")
        print("post executed")
        return item.json(), 201



    def delete(self, name):
        item = ItemModel.find_by_name(name)
        print("find_by_name executed")
        if item:
            item.delete_from_db()
            print("delete_by_name executed")

        return {'message':'Item deleted'}


    def put(self, name):# PUT: updateing the values already in the server

        data =Item.parser.parse_args()

        item = ItemModel.find_by_name(name)


        if item is None:
            item = ItemModel(name, data['price'],data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        print("save_to_db executed")

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items':list(map(lambda x: x.json(), ItemModel.query.all()))}
