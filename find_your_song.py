import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv('spotify_api_data.csv')

def show_findsong_page():
    # Main Content: Filters
    st.header("Filters")

    # Playlist Filter (Multiselect, allowing multiple selections)
    playlist_filter = st.multiselect(
        "Select Playlist(s):",
        options=df['playlist_name'].unique(),
        default=df['playlist_name'].unique()
    )
    # Artist Filter (Selectbox, allowing single selection)
    artist_filter = st.selectbox(
        "Select Artist:",
        options=["All"] + list(df['artist'].unique())  # Adding "All" option to allow all artists
    )
    # Explicit Content Filter
    explicit_filter = st.selectbox(
        "Explicit Content:",
        options=["All", True, False]
    )
    # Popularity Range Slider
    popularity_range = st.slider(
        "Popularity Range:",
        min_value=int(df['popularity'].min()),
        max_value=int(df['popularity'].max()),
        value=(int(df['popularity'].min()), int(df['popularity'].max()))
    )
    # Duration Range Slider
    duration_range = st.slider(
        "Duration (ms):",
        min_value=int(df['duration_ms'].min()),
        max_value=int(df['duration_ms'].max()),
        value=(int(df['duration_ms'].min()), int(df['duration_ms'].max()))
    )
    # Apply Filters
    filtered_df = df[
        (df['playlist_name'].isin(playlist_filter)) &
        ((df['artist'] == artist_filter) if artist_filter != "All" else True) &  # If "All" is selected, no filter on artist
        ((df['explicit'] == explicit_filter) if explicit_filter != "All" else True) &
        (df['popularity'].between(*popularity_range)) &
        (df['duration_ms'].between(*duration_range))
    ]
    # Display filtered data
    st.write(f"Filtered Data: {len(filtered_df)} tracks")
    st.dataframe(filtered_df)