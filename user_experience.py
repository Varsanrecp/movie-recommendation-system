import pandas as pd

class UserExperience:
    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_user_input(self):
        favorite_movie = input("Enter your favorite movie: ")

        # Ask if user wants to see list of directors
        show_directors = input("Do you want to see the list of directors? (yes/no): ")
        if show_directors.lower() == 'yes':
            directors = self.movie_data['Director'].unique()
            print("Select your favorite director:")
            for director in directors:
                print(director)
        favorite_director = input("Enter your favorite director (or type 'no one' if you don't have a favorite): ")
        if favorite_director.lower() == 'no one':
            favorite_director = ''

        # Ask if user wants to see list of genres
        show_genres = input("Do you want to see the list of genres? (yes/no): ")
        if show_genres.lower() == 'yes':
            genres = self.movie_data['Genre'].unique()
            print("Select your favorite genre:")
            for genre in genres:
                print(genre)
        favorite_genre = input("Enter your favorite genre (or type 'no one' if you don't have a favorite): ")
        if favorite_genre.lower() == 'no one':
            favorite_genre = ''

        # Ask if user wants to see list of actors
        show_actors = input("Do you want to see the list of actors? (yes/no): ")
        if show_actors.lower() == 'yes':
            actors = self.movie_data['Actor'].unique()
            print("Select your favorite actor:")
            for actor in actors:
                print(actor)
        favorite_actor = input("Enter your favorite actor (or type 'no one' if you don't have a favorite): ")
        if favorite_actor.lower() == 'no one':
            favorite_actor = ''

        user_input = f"{favorite_movie} {favorite_director} {favorite_genre} {favorite_actor}"
        return user_input