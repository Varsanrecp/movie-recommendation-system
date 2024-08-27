import pandas as pd

# Load your dataset
df = pd.read_csv('Tamil_movies_dataset.csv')

# Base URL for IMDb search
base_url = "https://www.imdb.com/find/?q="

# Function to create IMDb search link for a movie
def create_imdb_link(movie_name):
    # Replace spaces with no space in the movie name
    formatted_name = movie_name.replace(' ', '')
    # Create the full IMDb search URL
    link = base_url + formatted_name
    return link

# Apply the function to the 'MovieName' column
df['link'] = df['MovieName'].apply(create_imdb_link)

# Save the updated DataFrame
df.to_csv('updated_dataset.csv', index=False)
