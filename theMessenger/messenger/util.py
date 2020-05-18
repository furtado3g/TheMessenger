##util package
from .models import AuthUser

class newUser:

    def __init__(self,data):
        self.username   = data['email']
        self.email      = data['email']
        self.password   = data['password']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
       