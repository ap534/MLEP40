# app.py
import streamlit as st
import requests

# Function to call the API and get recommendations
def get_movie_recommendations(user_id):
    response = requests.get(f"http://flask-api:5001/recommend?user_id={user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return ["Error: Could not retrieve recommendations", response]

# Streamlit UI
st.title('Movie Recommendation System')

user_id = st.text_input("Enter User ID")

if st.button('Get Recommendations'):
    recommendations = get_movie_recommendations(user_id)
    st.write(recommendations)
