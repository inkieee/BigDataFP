
from pymongo import MongoClient
import support

#run:
#   pip3 install -r requirements.txt 
#   to setup environment in terminal first

#Load credentials from .env file
import os
from dotenv import load_dotenv
load_dotenv()
mongo_db_pw=os.getenv("MONGO_DB_PW")

# Connect to MongoDB
with MongoClient(f"mongodb+srv://cheerio:{mongo_db_pw}@cluster0.so7kree.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") as client:
    db = client["air_quality"]
    collection = db["air_quality"]


    # Fetch data as DataFrame from MongoDB
    cursor = collection.find({})
    data = pd.DataFrame(list(cursor))

support.heat_map_by_county(data)
