import streamlit as st
import pandas as pd

df = pd.read_csv("spotify_api_data.csv")

def show_top10_page():

    # Page Title
    st.title("Top Songs by Year")
    st.write("Select a year in order view the top 10 most popular songs and the top 10 longest songs of that year.")

    selected_year = st.selectbox("Select Year", df['release_year'].unique())

    # Filter data for the selected year
    selected_year_data = df[df['release_year'] == selected_year]

    top_pop = selected_year_data[['track', 'artist', 'popularity']].sort_values(by='popularity', ascending=False).head(10) #Sort by popularity ascending and display top 10
    top_long = selected_year_data[['track', 'artist', 'duration_ms']].sort_values(by='duration_ms', ascending=False).head(10) #Sort by duration asecnding and display top 10

    # Display the results
    st.subheader(f"Top 10 Popular Songs of {selected_year}")
    st.dataframe(top_pop)

    st.subheader(f"Top 10 Longest Songs of {selected_year}")

    duration_min = []

    #Convert duration to minutes
    for duration_ms in top_long['duration_ms']:
        minutes = duration_ms // 60000 #Get minutes
        seconds = (duration_ms%60000) // 1000 #Get seconds
        duration_min.append(f"{minutes}:{seconds}min")

    top_long['duration_min'] = duration_min

    top_long = top_long[['track', 'artist', 'duration_min']]
    st.dataframe(top_long)
