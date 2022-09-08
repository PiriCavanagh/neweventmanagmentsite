from flask import Flask

# create a flask App


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = '128329797'

    from .views import mybp  
    app.register_blueprint(mybp)  # registering the blueprint

    return app
