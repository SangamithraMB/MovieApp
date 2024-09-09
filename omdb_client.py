import os

import requests
from dotenv import load_dotenv

load_dotenv()


class OMDbAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def fetch_movie_data(self, title):
        params = {
            'apikey': self.api_key,
            't': title
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                return data
            else:
                print(f"Error: {data['Error']}")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


# Example usage:
if __name__ == "__main__":
    api_key = os.getenv('OMDB_API_KEY')

    client = OMDbAPIClient(api_key)

    movie_data = client.fetch_movie_data('Titanic')
    if movie_data:
        print(f"Title: {movie_data['Title']}")
        print(f"Year: {movie_data['Year']}")
        print(f"IMDB Rating: {movie_data['imdbRating']}")
        print(f"Actors: {movie_data['Actors']}")
