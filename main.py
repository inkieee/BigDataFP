import pandas as pd
import seaborn as sns
from pymongo import MongoClient

#run:
#   pip3 install -r requirements.txt 
#   to setup environment in terminal first

#Load credentials from .env file
import os
from dotenv import load_dotenv
load_dotenv()
mongo_db_pw=os.getenv("MONGO_DB_PW")

# Connect to MongoDB
client = MongoClient(f"mongodb+srv://cheerio:{mongo_db_pw}@cluster0.so7kree.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["air_quality"]
collection = db["air_quality"]





# Fetch data as DataFrame from MongoDB
cursor = collection.find({})
data = pd.DataFrame(list(cursor))

# Convert 'Date' field to datetime format (assuming 'Date' stores ISO 8601 format)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data['Date'] = pd.to_datetime(data['Date'].dt.utc.strftime('%Y-%m-%d'), utc=True)

# Extract year from the 'Date' column
data['Year'] = data['Date'].dt.year

# Reshape the data for heatmap (pivot table by year and state)
data_pivoted = data.pivot_table(values='AQI', index='Year', columns='State Name', aggfunc='mean')

# Generate heatmap using seaborn
sns.heatmap(data_pivoted)
plt.show()
