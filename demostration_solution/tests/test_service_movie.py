from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    genre1 = Genre(id=1, name='genre1')
    genre2 = Genre(id=2, name='genre2')
    genre3 = Genre(id=2, name='genre3')

    director1 = Director(id=1, name='director1')
    director2 = Director(id=2, name='director2')
    director3 = Director(id=2, name='director3')

    movie1 = Movie(id=1, title='test_title1', description='test_description1', trailer='test_trailer1',
                   year=2021, rating=1.1, genre_id=genre1, director_id=director1)
    movie2 = Movie(id=2, title='test_title2', description='test_description2', trailer='test_trailer2',
                   year=2022, rating=2.2, genre_id=genre2, director_id=director2)
    movie3 = Movie(id=3, title='test_title3', description='test_description3', trailer='test_trailer3',
                   year=2023, rating=3.3, genre_id=genre3, director_id=director3)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_by_username = MagicMock(return_value=movie2)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            "title": 'test_title3',
            "description": 'test_description3',
            "trailer": 'test_trailer3',
            "year": 2023,
            "rating": 3.3,
            "genre_id": 3,
            "director_id": 3,
            }

        movie = self.movie_service.create(movie_data)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_data = {
            "id": 3,
            "title": 'test_title3',
            "description": 'test_description3',
            "trailer": 'test_trailer3',
            "year": 2023,
            "rating": 3.3,
            "genre_id": 3,
            "director_id": 3,
        }

        self.movie_service.update(movie_data)
