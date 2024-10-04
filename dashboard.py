import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('main_data.csv')

# Set a custom theme
st.set_page_config(page_title="Bike Rental Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
chart_type = st.sidebar.selectbox("Select a chart to display", 
                                    ("Pengaruh Cuaca terhadap Jumlah Penyewaan", "Hari dan Jam Penyewaan Tertinggi", "Holiday vs Working Day"))

# Set the style for Seaborn
sns.set(style="whitegrid")

# Statistics
st.header("Statistics")
total_rentals = data['cnt'].sum()
average_rentals = data['cnt'].mean()
st.write(f"**Total Rentals:** {total_rentals}")
st.write(f"**Average Rentals:** {average_rentals:.2f}")

# Create a function to plot the weather effect
def plot_weather_effect(data):
    weather_data = data[data['chart_type'] == 'Pengaruh Cuaca terhadap Jumlah Penyewaan']
    plt.figure(figsize=(8, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_data, palette='Blues')
    plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Sewa Sepeda (2011-2012)')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Sewa Sepeda')
    plt.xticks(ticks=[0, 1, 2], labels=['Cuaca Cerah', 'Kabut/Cerah', 'Hujan Ringan'])
    st.pyplot(plt)

# Create a function to plot the hour vs weekday with distinct colors
def plot_hour_weekday(data):
    weekday_data = data[data['chart_type'] == 'Hari dan Jam Penyewaan Tertinggi']
    plt.figure(figsize=(15, 7))
    distinct_palette = sns.color_palette("husl", n_colors=7)
    sns.lineplot(x='hr', y='cnt', hue='weekday', data=weekday_data, palette=distinct_palette, marker='o')
    plt.title('Total Jumlah Penyewaan Sepeda per Jam dan Hari dalam Minggu (2011-2012)')
    plt.xlabel('Jam')
    plt.ylabel('Total Jumlah Penyewaan Sepeda')
    plt.xticks(ticks=range(0, 24), labels=[f"{h}:00" for h in range(24)])
    plt.legend(title='Hari dalam Minggu')
    st.pyplot(plt)

# Create a function to plot the hour vs day type
def plot_hour_day_type(data):
    day_type_data = data[data['chart_type'] == 'Holiday vs Working Day']
    plt.figure(figsize=(15, 6))
    sns.barplot(x='hr', y='cnt', hue='day_type', data=day_type_data, palette='viridis')
    plt.title('Jumlah Penyewaan Sepeda Rata-rata per Jam dan Tipe Hari (2011-2012)')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
    plt.xticks(ticks=range(0, 24), labels=[f"{h}:00" for h in range(24)])
    plt.legend(title='Tipe Hari')
    st.pyplot(plt)

# Dashboard title
st.title('Dashboard Penyewaan Sepeda (2011-2012)')

# Call the plotting functions based on selection
if chart_type == "Pengaruh Cuaca terhadap Jumlah Penyewaan":
    plot_weather_effect(data)
elif chart_type == "Hari dan Jam Penyewaan Tertinggi":
    plot_hour_weekday(data)
else:
    plot_hour_day_type(data)