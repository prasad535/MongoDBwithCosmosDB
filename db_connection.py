# Database connection
import pymongo
import certifi
import os

from dotenv import load_dotenv
from constants import MONGODB_URL_KEY, DATABASE_NAME

load_dotenv()

ca = certifi.where()

class MongoDBClient:
    client = None
    
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                print("Connection String:", mongo_db_url)
                
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(
                        mongo_db_url,
                        tlsCAFile=ca
                    )
                    
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            
        except Exception as e:
            raise e

