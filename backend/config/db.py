from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

cluster = os.getenv('MONGODB_CONNECTION')

client = MongoClient(cluster)