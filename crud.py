"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def show_all_users():
    """display all users"""
    return User.query.all()

def get_user_by_id(movie_id):
    """return user with input user_id"""
    return User.query.get(movie_id)

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview,
                  release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def show_all_movies():
    """return all movies"""

    return Movie.query.all()

def create_rating(score, movie, user):
    """Create and return a movie rating"""
    rating = Rating(score=score, movie=movie, user=user)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """return movie with the movie id"""
    return Movie.query.get(movie_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
