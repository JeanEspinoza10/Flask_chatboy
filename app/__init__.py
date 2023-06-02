from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import environment
from os import getenv



app = Flask(__name__)


app.config.from_object(environment[getenv('ENVIRONMENT')])
CORS(app)

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Chatbot',
    version='0.1',
    description='Endpoints',
    authorizations=authorizations,
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)