class Config:
    """Configuração base (caso queira herdar para outras configs no futuro)."""
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongodb',
        'username': 'admin',
        'password': 'admin'
    }

class DevConfig(Config):
    """Configuração específica para desenvolvimento."""
    DEBUG = True
