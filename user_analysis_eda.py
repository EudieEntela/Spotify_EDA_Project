import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("spotify_api_data.csv")

def show_useranalysis_page():
    
    st.title("Artist Analysis EDA")
    st.write("You are free to explore track popularity, release trends, and lyric sentiments!")

    #Users select an artist to filter data on popularity displayed in a bar chart
    st.header("Track Popularity Analysis")
    artist = st.selectbox("Select Artist", options=[''] + sorted(df['artist'].unique().tolist()))
    if artist:
        filtered_artist_df = df[df['artist'] == artist]
        popularity_fig = px.bar(filtered_artist_df, x='track', y='popularity', title=f'Popularity of Tracks by {artist}')
        st.plotly_chart(popularity_fig)


    #User selects specific year to filter and see tracks released over time
    st.header("Release Year Analysis")
    year = st.selectbox("Select Year", options=[None] + sorted(df['release_year'].unique().tolist()))
    if year:
        filtered_year_df = df[df['release_year'] == year]
        release_year_fig = px.line(filtered_year_df, x='release_date', y='track', title=f'Tracks Released in {year} Over Time')
        st.plotly_chart(release_year_fig)


    #User selects a year and it visualizes a pie chart of the sentiment distribution
    st.header("Lyrics Sentiment Analysis")
    sentiment_year = st.selectbox("Select Year for Sentiment Analysis", options=[None] + sorted(df['release_year'].unique().tolist()))
    if sentiment_year:
        filtered_sentiment_df = df[df['release_year'] == sentiment_year]
        sentiment_dist = filtered_sentiment_df['sentiment'].value_counts()
        sentiment_pie_chart = go.Figure(data=[go.Pie(labels=sentiment_dist.index, values=sentiment_dist.values, hole=.3)])
        sentiment_pie_chart.update_layout(title=f"Sentiment Distribution in {sentiment_year}")
        st.plotly_chart(sentiment_pie_chart)


    #User searches for a word in lyrics
    st.header("Search Tracks by Lyrics")
    search_word = st.text_input("Search for a Word in Lyrics", "")
    if search_word:
        filtered_lyrics_df = df[df['lyrics'].str.contains(search_word, case=False, na=False)]
        st.subheader(f"Tracks containing '{search_word}'")
        st.write(filtered_lyrics_df[['track', 'artist', 'release_year']])
