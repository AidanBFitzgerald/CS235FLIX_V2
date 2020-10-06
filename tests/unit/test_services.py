import pytest

from flix.domain.model import make_review, User
from flix.movies import services as movies_services


def test_can_add_review(in_memory_repo):
    movie_id = 1
    review_text = "Wasn't a fan"
    rating = 4
    username = 'shaun'

    movies_services.add_review(movie_id, review_text, rating, username, in_memory_repo)
    comments_as_dict = movies_services.get_reviews_for_movie(movie_id, in_memory_repo)

    assert next(
        (dictionary['review_text'] for dictionary in comments_as_dict if dictionary["review_text"] == review_text),
        None) is not None


def test_cannot_add_review_for_non_existent_movie(in_memory_repo):
    movie_id = 12
    review_text = 'Favourite Movie!'
    rating = 10
    user = 'shaun'

    with pytest.raises(movies_services.NonExistentMovieException):
        movies_services.add_review(movie_id, review_text, rating, user, in_memory_repo)


def test_cannot_add_review_for_non_existent_user(in_memory_repo):
    movie_id = 2
    review_text = 'Favourite Movie!'
    rating = 10
    user = 'dave'

    with pytest.raises(movies_services.UnknownUserException):
        movies_services.add_review(movie_id, review_text, rating, user, in_memory_repo)


def test_can_get_movie(in_memory_repo):
    movie_id = 2
    movie_as_dict = movies_services.get_movie(movie_id, in_memory_repo)
    assert movie_as_dict['id'] == movie_id
    assert movie_as_dict[
               'description'] == "Following clues to the origin of mankind, a team finds a structure on a distant moon, but they soon realize they are not alone."
    assert movie_as_dict['title'] == "Prometheus"
    assert movie_as_dict['director'] == "Ridley Scott"
    assert movie_as_dict['actors'] == ["Noomi Rapace", "Logan Marshall-Green", "Michael Fassbender", "Charlize Theron"]
    assert movie_as_dict['genres'][0]["genre"] == "Adventure"
    assert movie_as_dict['runtime'] == 124
    assert len(movie_as_dict['reviews']) == 0
    assert movie_as_dict['year'] == 2012


def test_cannot_get_non_existent_movie(in_memory_repo):
    movie_id = 27
    with pytest.raises(movies_services.NonExistentMovieException):
        movies_services.get_movie(movie_id, in_memory_repo)


def test_can_get_first_movie(in_memory_repo):
    movie = movies_services.get_first_movie(in_memory_repo)
    assert movie['id'] == 1


def test_can_get_last_movie(in_memory_repo):
    movie = movies_services.get_last_movie(in_memory_repo)
    assert movie['id'] == 5


def test_can_get_all_letters(in_memory_repo):
    letters = movies_services.get_all_letters(in_memory_repo)
    assert len(letters) == 3
    assert letters[0] == 'G'


def test_can_get_movies_by_letter(in_memory_repo):
    letter = 'P'
    movies, prev_letter, next_letter = movies_services.get_movies_by_letter(letter, in_memory_repo)
    assert movies[0]['id'] == 2
    assert prev_letter == 'G'
    assert next_letter == 'S'


def test_can_get_movies_from_genre(in_memory_repo):
    genre = "Action"
    movies = movies_services.get_movies_from_genre(genre, in_memory_repo)
    assert movies[0]['id'] == 1
    assert movies[1]['id'] == 5


def test_can_get_reviews_for_movie(in_memory_repo):
    movie_id = 1

    # adding review to repo
    user = User("shaun", '12345')
    review = make_review("Wow", user, in_memory_repo.get_movie(1), 10)
    in_memory_repo.add_review(review)

    # testing retrieval of review
    reviews = movies_services.get_reviews_for_movie(movie_id, in_memory_repo)
    assert len(reviews) == 1
    assert reviews[0]["review_text"] == "Wow"


def test_cannot_get_reviews_for_non_existent_movie(in_memory_repo):
    with pytest.raises(movies_services.NonExistentMovieException):
        reviews = movies_services.get_reviews_for_movie(12, in_memory_repo)


def test_can_get_reviews_for_movie_without_reviews(in_memory_repo):
    reviews = movies_services.get_reviews_for_movie(2, in_memory_repo)
    assert len(reviews) == 0