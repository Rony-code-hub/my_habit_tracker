import os
from flask import Flask
from pymongo import MongoClient
from routes import pages
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    db_name = "habits"

    client = MongoClient(os.environ.get("MONGO_URI"))
    app.db = client[db_name]

    app.register_blueprint(pages)
    return app
