from flask_restful import Resource, reqparse
from models import User


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Users(Resource):
    def get(self):
        users = User.objects()
        return [{'cpf': user.cpf, 'email': user.email} for user in users]


class UserResource(Resource):
    def get(self, cpf):
        user = User.objects(cpf=cpf).first()
        if user:
            return {
                'cpf': user.cpf,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'birth_date': str(user.birth_date)
            }
        return {'message': 'User not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cpf', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('birth_date', required=True)
        args = parser.parse_args()

        if User.objects(cpf=args['cpf']).first():
            return {'message': 'CPF already exists'}, 400

        user = User(**args)
        user.save()
        return {'message': 'User created successfully'}, 201
