##util package
from .models import AuthUser
import hashlib

class newUser:

    def __init__(self,data):
        self.username   = data['email']
        self.password   = data['password']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']

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
        return hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                password.encode('utf-8'), # Convert the password to bytes
                100000, # It is recommended to use at least 100,000 iterations of SHA-256 
                dklen=128 # Get a 128 byte key
            )