from pymongo import MongoClient
from src.config.main import get_app, get_config

app =get_app()
config = get_config()

def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client[config["DATABASE"]]

    
def shutdown_db_client():
    app.mongodb_client.close()
