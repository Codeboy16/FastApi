from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)

# Use YOUR existing database name or Create New Automatically
database = client["yourDatabaseName"]

# Use YOUR existing collection name or Create New Automatically
collection = database["yourCollectionName"]


# pip install motor pymongo python-dotenv (Install The Package for Use MongoDb Atlas)