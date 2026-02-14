import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 🔑 Replace with your OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY_HERE"

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌦 Real-Time Weather Data Analytics Dashboard")

city = st.text_input("Enter City Name", "Chennai")

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

if st.button("Get Weather Data"):
    data = get_weather_data(city)

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        description = data["weather"][0]["description"]

        st.subheader(f"Weather in {city}")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🌡 Temperature (°C)", temperature)
        col2.metric("💧 Humidity (%)", humidity)
        col3.metric("🌬 Wind Speed (m/s)", wind_speed)
        col4.metric("🔵 Pressure (hPa)", pressure)

        st.write("### 🌥 Weather Condition:", description.capitalize())

        # Create DataFrame for visualization
        weather_df = pd.DataFrame({
            "Parameter": ["Temperature", "Humidity", "Wind Speed", "Pressure"],
            "Value": [temperature, humidity, wind_speed, pressure]
        })

        st.write("### 📊 Weather Data Visualization")

        fig, ax = plt.subplots()
        ax.bar(weather_df["Parameter"], weather_df["Value"])
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.success("Data Loaded Successfully ✅")

    else:
        st.error("City not found or API issue ❌")
