##util package
from .models import AuthUser
import hashlib

class newUser:

    def __init__(self,data):
        if data['first_name']:
            self.username   = data['email']
            self.password   = data['password']
            self.first_name = data['first_name']
            self.last_name  = data['last_name']
        else:
            self.username   = data['email']
            self.password   = data['password']

    def get_values(self):
        
        return{
            "username" : self.username,
            "email" :self.username,
            "password" : self.crypto(self.password),
            "first_name" : self.first_name,
            "last_name":self.last_name,
            "is_superuser":False,
            "is_staff":False,
            "is_active":True
        }
       
    def crypto(self,password):
        salt = 'homesweethole'
        key  = hashlib.sha256(password.encode()).hexdigest()
        return key

class loginDigest:
    def crypto(self,password):
        salt = 'homesweethole'
        key  = hashlib.sha256(password.encode()).hexdigest()
        return key        



class AddFriend:

    def __init__(self,data):
        self.user_id = data['me']
        self.friend_id = data['friend']
    
    def getValues(self):
        return {
            "me":self.user_id,
            "friend":self.friend_id
        }