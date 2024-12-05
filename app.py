import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from top_10_popular_and_longest import show_top10_page
from word_cloud import show_wordcloud_page
from find_your_song import show_findsong_page
from user_analysis_eda import show_useranalysis_page
from eda_section import show_edasection_page

df = pd.read_csv("spotify_api_data.csv")


st.sidebar.image('spotify1_img.jpg',use_container_width=True)
select_box_pages = st.sidebar.selectbox('Select a feature and explore!', ('Home','EDA Section','Top 10','Word Cloud', 'Find Your Song', 'User Data Analysis'))

st.sidebar.write("""
**Explore this EDA Project of Spotify music data through interactive visualizations and analyses!**
- **Home:** A summary on this project and its features. 
- **EDA Section:** A detailed exploratory data analysis.
- **Top 10:** Discover popular and long tracks.
- **Word Cloud:** Visualize lyrical themes and patterns through WordCloud
- **Find Your Song:** Search for a song based on features of your preference.
- **User Data Analysis:**  Explore track popularity, release, trends, lyric sentiments, and search songs by lyrics!
""")

if select_box_pages == 'EDA Section':
        show_edasection_page()
elif select_box_pages == 'Top 10':
        show_top10_page()
elif select_box_pages == 'Word Cloud':
        show_wordcloud_page()
elif select_box_pages == 'Find Your Song':
        show_findsong_page()
elif select_box_pages == 'User Data Analysis':
        show_useranalysis_page()
else:
    st.title('Spotify Music Exploratory Data Analysis Project')
    st.image('spotify_header.png', use_container_width=True)
    st.write("""**Using Spotify's API and Genius' API, this project brings together track features, lyrics, and sentiments to provide insights into popular music trends.**""")

    st.header('About this Project')
    st.write("This project analyzes a musical dataset to uncover patterns in song popularity, track informationm lyrics sentiment and more based on playlists tracks gathered using Spotify's API and Genius' API. You'll gain insight into lyrical themes, factors that play into a songs popularity and more!")

    st.write("Explore Spotify's music data through interactive visualizations. Get started by selecting a feature in the sidebar!")

    st.header('Project Objectives')
    st.write("""
        - Explore Spotify's music data and identify patterns in the tracks and artists
        - Analyze lyrical content and uncover thematic patterns
        - Create an interactive user experience for exploring music, analyzing trends and discovery new tracks
        - Utilize visulization tools to make the experience more engaging.
                """)
    
    st.header('Data Overview')
    st.write("""
        - _track:_ Song Title
        - _artist:_ The creator of the track
        - _playlist_name:_ The playlist where the tracks appear
        - _release_date:_ The date the track was release
        - _popularity:_ A score from 0-100 reflecting the song's popularity
        - _explicit:_ Whether the track contains explicit lyrics or not
        - _duration (ms):_ Track duration in milliseconds
        - _lyrics:_ Lyrical content of the track
        - _release year:_ The year the track was released
        - _sentiment:_ Sentiment analysis of the lyrics
                """)
    
    st.write("Get started by selecting a feature in the sidebar!")
    st.image('footer_image.png', use_container_width=True)