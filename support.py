import pandas as pd
import seaborn as sns
from pymongo import MongoClient
import matplotlib.pyplot as plt  

def heat_map_by_county(data):
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

