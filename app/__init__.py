from flask import Flask
from flask_restx import Api
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(
    app,
    title='Chatbot',
    version='0.1',
    description='Endpoints',
    doc='/swagger-ui'
)

