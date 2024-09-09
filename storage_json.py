import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        """Initialize the JSON storage with the given file path."""
        self.file_path = file_path
        # If the file doesn't exist, create an empty file
        try:
            with open(self.file_path, 'r') as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.file_path, 'w') as file:
                json.dump({}, file)

    def list_movies(self):
        """Loads and returns all movies as a dictionary."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def add_movie(self, title, year, rating, poster, imdb_url, note):
        """Adds a new movie to the JSON file."""
        movies = self.list_movies()  # Load the current movies
        if title in movies:
            print(f"Movie '{title}' already exists.")
        else:
            movies[title] = {
                'year': year,
                'rating': rating,
                'poster': poster,
                'imdb_url': imdb_url,
                'notes': note
            }
            self._save_movies(movies)
            print(f"Movie '{title}' added.")

    def delete_movie(self, title):
        """Deletes a movie from the JSON file."""
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            print(f"Movie '{title}' deleted.")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, rating):
        """Updates the rating of a movie in the JSON file."""
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)
            print(f"Movie '{title}' updated with new rating: {rating}.")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie_notes(self, title, notes):
        """Update notes for a movie in the JSON storage."""
        movies = self.list_movies()
        if title in movies:
            movies[title]['notes'] = notes
            self._save_movies(movies)  # Ensure you save the updated data
        else:
            raise ValueError("Movie not found.")

    def _save_movies(self, movies):
        """Helper function to save the movies to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)
