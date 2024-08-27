from flask import Flask, render_template, request
import pandas as pd
from movie_recommender import MovieRecommender
app = Flask(__name__)

# Load movie data
movie_data = pd.read_csv('Tamil_movies_dataset.csv')

# Create an instance of MovieRecommender
recommender = MovieRecommender(movie_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        favorite_movie = request.form['favorite_movie']
        favorite_director = request.form.get('favorite_director', '')
        favorite_genre = request.form.get('favorite_genre', '')
        favorite_actor = request.form.get('favorite_actor', '')
        
        user_input = f"{favorite_movie} {favorite_director} {favorite_genre} {favorite_actor}"
        recommended_movies = recommender.recommend(user_input)
        
        # Get the movie names and links
        recommended_movies_with_links = [
            {"title": movie, "link": movie_data[movie_data['MovieName'] == movie]['link'].values[0]}
            for movie in recommended_movies
        ]

        return render_template('index.html', 
                               recommended_movies=recommended_movies_with_links,
                               movies=movie_data['MovieName'].unique(), 
                               directors=movie_data['Director'].unique(),
                               genres=movie_data['Genre'].unique(), 
                               actors=movie_data['Actor'].unique())

    return render_template('index.html', 
                           movies=movie_data['MovieName'].unique(), 
                           directors=movie_data['Director'].unique(),
                           genres=movie_data['Genre'].unique(), 
                           actors=movie_data['Actor'].unique())
    
    
@app.route('/reviews')
def reviews():
    posts = [
        {'title': 'Movie Review 1', 'content': 'This is a review of movie 1.', 'author': 'John Doe', 'date': '2023-02-20'},
        {'title': 'Movie Review 2', 'content': 'This is a review of movie 2.', 'author': 'Jane Doe', 'date': '2023-02-21'},
        {'title': 'Movie Review 3', 'content': 'This is a review of movie 3.', 'author': 'Bob Smith', 'date': '2023-02-22'}
    ]
    return render_template('reviews.html', posts=posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
