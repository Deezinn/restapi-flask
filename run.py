from src.app import app
from src.routes import register_routes

register_routes()


if __name__ == '__main__':
    app.run(debug=True)
