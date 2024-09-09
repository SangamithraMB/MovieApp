import csv
from istorage import IStorage
import pandas as pd


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        # Ensure the file exists or create it with a header if it doesn't
        try:
            with open(self.file_path, 'r', newline='') as file:
                csv.reader(file)  # Try reading to ensure file existence
        except (FileNotFoundError, IOError):
            # If the file doesn't exist, create it with a header
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Year', 'Rating', 'Poster', 'imdb_url', 'notes'])

    def list_movies(self):
        """List all movies as a dictionary."""
        movies = {}
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Use get() with default values to avoid KeyError
                    movies[row.get('Title', '')] = {
                        'year': row.get('Year', 'Unknown'),
                        'rating': row.get('Rating', 'Not rated'),
                        'poster': row.get('Poster', 'No poster available'),
                        'imdb_url': row.get('imdb_url', 'URL not available'),
                        'notes': row.get('notes', '')
                    }
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading movies: {e}")
        return movies

    def add_movie(self, title, year, rating, poster, imdb_url, note):
        """Add a new movie to the CSV file."""
        movies = self.list_movies()
        if title in movies:
            print(f"Movie '{title}' already exists.")
            return
        try:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title, year, rating, poster, imdb_url, note])
            print(f"Movie '{title}' added successfully.")
        except IOError as e:
            print(f"Error adding movie: {e}")

    def delete_movie(self, title):
        """Delete a movie from the CSV file by title."""
        movies = self.list_movies()
        if title not in movies:
            print(f"Movie '{title}' not found.")
            return
        updated_movies = {k: v for k, v in movies.items() if k != title}
        self._save_movies(updated_movies)
        print(f"Movie '{title}' deleted successfully.")

    def update_movie(self, title, rating):
        """Update the rating of an existing movie."""
        movies = self.list_movies()
        if title not in movies:
            print(f"Movie '{title}' not found.")
            return
        movies[title]['rating'] = rating
        self._save_movies(movies)
        print(f"Movie '{title}' updated with new rating: {rating}.")

    def update_movie_notes(self, title, notes):
        """Update notes for a movie in the CSV storage."""
        movies = pd.read_csv(self.file_path)
        if title in movies['Title'].values:
            movies.loc[movies['Title'] == title, 'notes'] = notes
            movies.to_csv(self.file_path, index=False)
        else:
            raise ValueError("Movie not found.")

    def _save_movies(self, movies):
        """Save the movies dictionary back to the CSV file."""
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Year', 'Rating', 'Poster', 'imdb_url', 'notes'])  # Write header
                for title, details in movies.items():
                    writer.writerow(
                        [title, details['year'], details['rating'], details['poster'], details.get('imdb_url', ''),
                         details.get('notes', '')])
            print(f"Movies saved successfully to {self.file_path}")
        except IOError as e:
            print(f"Error saving movies: {e}")
