# app.py
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_recommendations(user_id, user_movie_similarity_df, ratings_df, k=5):
    recommendations = user_movie_similarity_df.loc[user_id]

    # Get top 5 movie IDs
    top_5_movies = recommendations.nlargest(5).index.tolist()
    movie_names = []
    for movie in top_5_movies:
        movie_names.append(movies_names_map[int(movie)])
    print("generated recommendations", movie_names)
         
    return movie_names

@app.route('/recommend', methods=['GET'])
def recommend_movies():
    user_id_input = request.args.get('user_id')
    
    # Logic to generate recommendations based on user_id
    recommendations = get_recommendations(int(user_id_input), train_user_movie_similarity_df, ratings_df)

    return jsonify(recommendations)

train_user_movie_similarity_df = pd.read_parquet("Cache/train_user_movie_similarity.parquet")
ratings_df = pd.read_csv("Camille G data/ratings.csv")
movies_metadata = pd.read_csv("Camille G data/movies_combined_all_features.csv")
movies_names_map = movies_metadata.set_index("movieId")["title"].to_dict()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

