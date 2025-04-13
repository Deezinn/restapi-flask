from src import create_app
from src.routes import register_routes
from config import DevConfig

app, api = create_app(DevConfig)

register_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
