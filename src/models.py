from .db import db
from datetime import datetime

class User(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow)

    def to_json(self):
        return {
            'cpf': self.cpf,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
