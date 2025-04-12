from .app import api
from .resources import HelloWorld

api.add_resource(HelloWorld, '/')
