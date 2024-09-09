from abc import ABC, abstractmethod


class IStorage(ABC):

    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, imdb_url, note):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass

    def update_movie_notes(self, title, note):
        pass
