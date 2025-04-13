from .app import api
from .resources import HelloWorld, Users, UserResource

def register_routes():
    api.add_resource(HelloWorld, '/')
    api.add_resource(Users, '/users')
    api.add_resource(UserResource, '/user', '/user/<string:cpf>')
