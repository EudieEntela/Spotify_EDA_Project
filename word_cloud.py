import streamlit as st
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('spotify_api_data.csv')


def show_wordcloud_page():
    # List of stopwords for preprocessing_lyrics
    stopwords = {
        "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", 
        "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with", "you", "your"
    }

    st.title("Word Cloud Generator for Songs")

    song_selection = st.selectbox("Select a song to generate a Word Cloud:",options=sorted(df['track'].unique())) #Select a song (displayed alphabetically)

    #"Generate Word Cloud" button
    if st.button('Generate Word Cloud'):

        selected_lyrics = df.loc[df['track'] == song_selection, 'lyrics'].values[0] #GEt song lyrics

        lyrics = re.sub(r'[\W_]+', ' ', selected_lyrics.lower())  # Remove special characters and convert to lowercase
        words = [word for word in lyrics.split() if word not in stopwords]  # Remove stopwords
        processed_lyrics = ' '.join(words)

        # Generate and display the word cloud
        if processed_lyrics.strip():  # Ensure lyrics are not empty

            # Create the WordCloud
            wordcloud = WordCloud(width=800, height=400, background_color='black').generate(processed_lyrics)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')

            st.header(f"Word Cloud for '{song_selection}'")
            st.pyplot(fig)
        else:
            st.warning(f"No lyrics available for the selected song: {song_selection}")
