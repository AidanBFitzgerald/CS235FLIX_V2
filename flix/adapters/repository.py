import abc
from typing import List

from flix.domain.model import User, Movie, Genre, Review, Actor, Director

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        """Adds a User to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """Returns the User named username from the repository.

        If there is no User with the given username, this method returns None."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """Adds a Movie to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title, year) -> Movie:
        """Returns Movie with title and year from the repository

        If there is no Movie with the given title and year, this method returns None."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_letter(self, target_letter) -> List[Movie]:
        """Returns a list of Movies that start with the letter, from the repository

        If there are no Movies that start with the given letter, this method returns an empty list."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """Returns the number of Movies in the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """Returns the first Movie, ordered by alphabet, from the repository.

        Returns None if the repository is empty"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """Returns the last Movie, ordered by alphabet, from the repository.

        Returns None if the repository is empty"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_year(self, year: int) -> List[Movie]:
        """Returns a list of Movies that are in a certain year, from the repository.

        If there are no Movies in the specified year, this method returns an empty list."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_from_genre(self, genre: Genre):
        """Returns a list of Movies that are in a certain genre, from the repository.

        If there are no Movies in the specified genre, this method returns an empty list."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self):
        """Adds a Genre to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """Returns the Genres stored in the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """Adds a Review to the repository.

        If the Review doesn't have bidirectional links with a Movie and a User, this method raises a
        RepositoryException and doesn't update the repository"""
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException("Review not correctly attached to a User")
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException("Review not correctly attached to a Movie")

    @abc.abstractmethod
    def get_reviews(self):
        """Returns the Reviews stored in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """Adds an Actor to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        """Returns the Actors sotred in the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """Adds a Director to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """Returns the Directors stored in the repository"""
        raise NotImplementedError