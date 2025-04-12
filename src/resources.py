from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Users(Resource):
    def get(self):
        return {'user': 'André'}

class User(Resource):
    def get(self):
        return {'message': 'Teste'}

    def get(self, cpf):
        return {'message': cpf}
