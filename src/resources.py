from flask_restful import Resource, reqparse
from .models import User
import re


def is_valid_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(cpf_slice, factor):
        total = sum(int(digit) * (factor - i)
                    for i, digit in enumerate(cpf_slice))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)

    digit1 = calculate_digit(cpf[:9], 10)
    digit2 = calculate_digit(cpf[:10], 11)

    return cpf[-2:] == digit1 + digit2


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

        if not is_valid_cpf(args['cpf']):
            return {'message': 'Invalid CPF'}, 400

        if User.objects(cpf=args['cpf']).first():
            return {'message': 'CPF already exists'}, 400

        user = User(**args)
        user.save()
        return {'message': 'User created successfully'}, 201
