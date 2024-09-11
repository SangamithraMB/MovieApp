from istorage import IStorage
from omdb_client import OMDbAPIClient
import random
import statistics


class MovieApp:
    def __init__(self, storage: IStorage, api_key: str):
        self._storage = storage
        self._omdb_client = OMDbAPIClient(api_key)

    def _command_list_movies(self):
        """List all the movies in the storage."""
        movies = self._storage.list_movies()
        movie_length = len(movies)
        print(f"There are {movie_length} movies in the list.")
        if movies:
            for title, details in movies.items():
                imdb_url = details.get('imdb_url', 'URL not available')
                print(
                    f"{title}: {details.get('year', 'Unknown')} - {details.get('rating', 'Not rated')} stars, "
                    f"IMDb URL: {imdb_url}")
        else:
            print("No movies found.")

    def _command_add_movie(self):
        """Add a new movie to the storage."""
        title = input("Enter movie title: ")
        try:
            # Fetch movie data from OMDb API
            movie_data = self._omdb_client.fetch_movie_data(title)
            if not movie_data:
                print("Movie not found.")
                return

            year = movie_data.get('Year')
            rating = float(movie_data.get('imdbRating', 0))
            poster = movie_data.get('Poster', 'No poster available')
            imdb_url = f"https://www.imdb.com/title/{movie_data.get('imdbID')}/" if movie_data.get('imdbID') else '#'
            note = input("Enter movie notes (optional): ")

            self._storage.add_movie(title, year, rating, poster, imdb_url, note)
            print(f"Movie '{title}' added successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def _command_delete_movie(self):
        """Delete a movie from the storage."""
        title = input("Enter movie title to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        """Update a movie's notes."""
        title = input("Enter movie title to update: ")
        note = input("Enter new note: ")

        movies = self._storage.list_movies()
        if title not in movies:
            print(f"Movie '{title}' not found.")
            return

        self._storage.update_movie_notes(title, note)
        print(f"Movie '{title}' successfully updated.")

    def _command_movie_stats(self):
        """
        Display statistics about the movies:
        - Average rating
        - Median rating
        - Best rated movie
        - Worst rated movie
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available for statistics.")
            return

        ratings = [float(details.get('rating', 0)) for details in movies.values() if details.get('rating') is not None]

        if not ratings:
            print("No ratings available for statistics.")
            return

        avg_rating = sum(ratings) / len(ratings)
        median_rating = statistics.median(ratings)

        best_movie = max(movies.items(), key=lambda x: float(x[1].get('rating', 0)))
        worst_movie = min(movies.items(), key=lambda x: float(x[1].get('rating', 0)))

        print(f"Average rating of all movies: {avg_rating:.2f} stars.")
        print(f"Median rating of all movies: {median_rating:.2f} stars.")
        print(f"Best rated movie: {best_movie[0]} with {best_movie[1].get('rating', 'Not rated')} stars.")
        print(f"Worst rated movie: {worst_movie[0]} with {worst_movie[1].get('rating', 'Not rated')} stars.")

    def _command_generate_website(self):
        """Generate a website from the movie data."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available to generate website.")
            return

        with open('index_template.html', 'r') as file:
            template = file.read()

        movie_grid = ''
        for title, details in movies.items():
            imdb_url = details.get('imdb_url', '#')
            movie_grid += f'<div class="movie-item">\n'
            movie_grid += f'  <h2>{title}</h2>\n'
            movie_grid += f'  <p>Year: {details.get("year", "Unknown")}</p>\n'
            movie_grid += f'  <p>Rating: {details.get("rating", "Not rated")}</p>\n'
            movie_grid += f'  <a href="{imdb_url}" target="_blank">\n'
            movie_grid += (f'    <img src="{details.get("poster", "No poster available")}" '
                           f'alt="{title} poster" title="{details.get("notes", "")}">\n')
            movie_grid += f'  </a>\n'
            movie_grid += f'  <div class="movie-note">{details.get("notes", "")}</div>\n'
            movie_grid += f'</div>\n'

        website_content = template.replace('__TEMPLATE_TITLE__', "Sang's Movie App")
        website_content = website_content.replace('__TEMPLATE_MOVIE_GRID__', movie_grid)

        with open('index.html', 'w') as file:
            file.write(website_content)

        print("Website was generated successfully.")

    def _command_random_movie(self):
        """Selects and prints a random movie from the stored movies."""
        movies = self._storage.list_movies()

        if not movies:
            print("No movies available to pick from.")
            return

        random_movie_title = random.choice(list(movies.keys()))
        print(f"Your movie for tonight is {random_movie_title}.")

    def _command_search_movie(self):
        """Search for movies by title or partial title."""
        query = input("Enter movie title or part of the title to search: ").lower()
        movies = self._storage.list_movies()

        found_movies = {title: details for title, details in movies.items() if query in title.lower()}

        if found_movies:
            for title, details in found_movies.items():
                print(f"{title}: {details.get('year', 'Unknown')} - {details.get('rating', 'Not rated')} stars")
        else:
            print("No movies found.")

    def _command_sort_by_rating(self):
        """Sort and display movies by their rating in descending order."""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: float(x[1].get('rating', 0)), reverse=True)

        if sorted_movies:
            for title, details in sorted_movies:
                print(f"{title}: {details.get('year', 'Unknown')} - {details.get('rating', 'Not rated')} stars")
        else:
            print("No movies found.")

    def run(self):
        """Main loop to run the movie app."""
        while True:
            database_detail = """
            ********** My Movies Database **********

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate website
"""
            print(database_detail)

            choice = input("Choose an option: ")

            if choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_delete_movie()
            elif choice == '4':
                self._command_update_movie()
            elif choice == '5':
                self._command_movie_stats()
            elif choice == '6':
                self._command_random_movie()
            elif choice == '7':
                self._command_search_movie()
            elif choice == '8':
                self._command_sort_by_rating()
            elif choice == '9':
                self._command_generate_website()
            elif choice == '0':
                print("Exiting the Movie App.")
                break
            else:
                print("Invalid choice. Please try again.")
