import pandas as pd
import seaborn as sns
from pymongo import MongoClient
import matplotlib.pyplot as plt  

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

def heatmap1():
    # Convert 'Date' field to datetime format 
    data['Date'] = pd.to_datetime([d for d in data['Date']])  # List comprehension for conversion

    # Extract year from the 'Date' column
    data['Year'] = data['Date'].dt.year

    # Reshape the data for heatmap (pivot table by year and state)
    data_pivoted = data.pivot_table(values='AQI', index='Year', columns='State Name', aggfunc='mean')

    # Generate heatmap using seaborn
    sns.heatmap(data_pivoted)
    plt.show()

def heat_map_by_county():
    # Preprocess data for Heatmap
    # Extract year from the Date column
    data['Year'] = pd.to_datetime(data['Date']).dt.year

    # Calculate average AQI every year for each county
    data_pivot = data.pivot_table(values='AQI', index='County Name', columns='Year', aggfunc='mean')

    # Create the Heatmap
    sns.heatmap(data_pivot, cmap="YlGnBu")  # Adjust the colormap as desired
    plt.xlabel("Year")
    plt.ylabel("County Name")
    plt.title("Heatmap of Average AQI by County and Year")
    plt.show()

heat_map_by_county