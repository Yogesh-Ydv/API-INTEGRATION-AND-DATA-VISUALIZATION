import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# API key provided by the user
API_KEY = "4477fe3494f0c59d9b1467fd3d364534"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# List of cities to fetch weather data for
cities = ["New York", "London", "Tokyo", "Delhi", "Sydney"]

# Fetch weather data for the cities
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}. Error: {response.status_code}")
        return None

# Store weather data
weather_data = []

for city in cities:
    data = fetch_weather_data(city)
    if data:
        weather_data.append({
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"]
        })

# Create a DataFrame
weather_df = pd.DataFrame(weather_data)

# Visualization
sns.set(style="whitegrid")

# Bar plot for temperatures
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Temperature (°C)", data=weather_df, palette="coolwarm")
plt.title("Temperature in Different Cities", fontsize=16)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xlabel("City", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot for humidity
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Humidity (%)", data=weather_df, palette="Blues")
plt.title("Humidity in Different Cities", fontsize=16)
plt.ylabel("Humidity (%)", fontsize=12)
plt.xlabel("City", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save data to a CSV file
weather_df.to_csv("weather_data.csv", index=False)

print("Task completed! Weather data and visualizations are ready.")