import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("spotify_api_data.csv")

def show_edasection_page():

    # Track Popularity Trends Over Time
    st.header("Track Popularity Trends Over Time")
    avg_popularity = (df.groupby('release_year')['popularity'].mean().reset_index().sort_values('release_year')) # Calculate average popularity by release year

    fig = px.line(avg_popularity,x='release_year',y='popularity',title="Average Track Popularity by Release Year",
                    labels={'release_year': 'Release Year', 'popularity': 'Avg Popularity'},markers=True )

    fig.update_layout(xaxis=dict(title='Release Year', showgrid=True),yaxis=dict(title='Average Popularity', showgrid=True),template='plotly_white')
    st.plotly_chart(fig)
    st.write('This graph hows the average popularity of tracks throughout the years. Each point shows the release year and the average popularity of the tracks release that same year. The database may not be too big considering it is just about 1000 songs, but the trend with these playlists and tracks show large variance in popularity with the the years before and after, regardless if it is an older track or newer.')

    st.markdown("---")

    # Explicit Songs Over Time
    st.header('Explicit Songs Over Time')
    explicit_group = df.groupby('release_year')['explicit'].mean().reset_index()
    fig2 = px.bar(explicit_group, x='release_year', y='explicit', title="Explicit Songs Over Time", 
              labels={'explicit': 'Explicit Songs'}, color_discrete_sequence=['green'])
    st.plotly_chart(fig2)
    st.write('The bar chart above visualizes the proportion of explicit songs over the years. Based on the data collected, it shows a larger amount of explicit songs in the later years starting in the 2000s as opposed to the earlier years (1990s and below) that have none.')

    st.markdown("---")

    # Top Artists Analysis
    st.header('Top 10 Most Common Artist')
    top_artists = df['artist'].value_counts().head(10).reset_index()
    top_artists.columns = ['artist', 'track_count']  # Rename columns for clarity
    top_artists = top_artists.sort_values(by='track_count', ascending=True)

    fig3 = px.bar(top_artists, x='track_count', y='artist', orientation='h', title="Top Artists by Track (Count)",
                  labels={'track_count': 'Track Count', 'artist': 'Artist'}, color='track_count', color_continuous_scale='viridis')
    st.plotly_chart(fig3)
    st.write('This graph displays the top 10 most common artists in the database. It seems like, at least in this dataframe, most artist are well-known artists that come from all different genres of music. This could be because of the specific playlist we took the tracks from on Spotify.')

    st.markdown("---")

    # Sentiment Distribution
    st.header("Sentiment Analysis")
    sentiment_counts = df['sentiment'].value_counts() #Count for each category

    fig4 = px.pie(sentiment_counts, values=sentiment_counts.values, names=sentiment_counts.index, 
              title="Distribution of Sentiment Categories")
    st.plotly_chart(fig4)
    st.write('This pie chart represents the distribution of sentiment categories. It is split into three slices: Negative, Neutral and Positive depending on the song lyrics. It illustrates the quantity of songs that fall under each category given the lyrical tone.')

    st.markdown("---")

    # Song Duration Distribution
    fig5 = px.histogram(df, x='duration_ms', nbins=20, title="Song Duration Distribution (in seconds)",
                    labels={'duration_ms': 'Duration (seconds)'}, color_discrete_sequence=['orange'])
    st.plotly_chart(fig5)
    st.write('This histogram shows the distribution of song durations (in milliseconds). As it appears, most songs have a similar duration at about the 3min-4min make aside from a couple of anomalies that up to 7-10mins.')

    st.markdown("---")

    # Top 10 Most Popular Songs
    top_songs = df.nlargest(10, 'popularity')
    top_songs = top_songs.sort_values(by='popularity', ascending=True)
    fig6 = px.bar(top_songs, x='popularity', y='track', orientation='h', title="Top 10 Most Popular Songs",
              color='artist', labels={'popularity': 'Popularity', 'track': 'Track'})
    st.plotly_chart(fig6)
    st.write('This bar showcases the 10 most popular songs in this dataset. In this graph, the bar shows the popularity score and the respective artist of the track. The artists in the top 10 all seem to be very popular artists and most of them in the "pop" genre.')

    st.markdown("---")

    # Popularity of Explicit vs Non-Explicit Songs
    fig7 = px.violin(df, x='explicit', y='popularity', color='explicit', box=True, points='all',title='Popularity of Explicit vs Non-Explicit Songs', 
                  labels={'explicit': 'Explicit', 'popularity': 'Popularity'}, color_discrete_sequence=['#FFC1CC', '#ADD8E6'])
    st.plotly_chart(fig7)
    st.write('This violin plot compares the distribution of popularity scores between explicit and non-explicit songs. The width of the violins represents the density of songs at each popularity level, while the overlayed boxplots provide additional summary statistics like the median. In the visualization above, we are able to see whether explicit songs are more or less popular than the non-explicit ones.')