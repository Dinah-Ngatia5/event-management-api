from server import create_app
from server.extensions import db

app = create_app()

if __name__ == '__main__':
    app.run()
