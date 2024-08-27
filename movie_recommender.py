import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, movie_data):
        self.movie_data = movie_data
        self.vectorizer = TfidfVectorizer()

    def recommend(self, user_input, num_recommendations=10):
        # Combine features into a single string
        combined_features = self.movie_data['MovieName'] + " " + self.movie_data['Genre'] + " " + self.movie_data['Actor'] + " " + self.movie_data['Director']
        combined = self.vectorizer.fit_transform(combined_features)

        # Get the user's input and convert it to a vector
        user_vector = self.vectorizer.transform([user_input])

        # Calculate cosine similarity between user's input and movie features
        cos_sim = cosine_similarity(user_vector, combined)

        # Get the top N similar movies
        scores = list(enumerate(cos_sim[0]))
        similar_movies = sorted(scores, key=lambda x: x[1], reverse=True)

        # Return the top N movie recommendations
        return [self.movie_data.at[index, "MovieName"] for index, _ in similar_movies[1:num_recommendations+1]]