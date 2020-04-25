from werkzeug.security import safe_str_cmp
from models.user import UserModel# importing from user



def authenticate(username, password): # to authenticate by taking username and password as arguments
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        print("This is username and password authentication: location UserModel/User")
        print("find_by_username")

        return user # return the user

def identity(payload):
    user_id = payload['identity']
    print("UserModel/User find_by_id")
    return UserModel.find_by_id(user_id)
