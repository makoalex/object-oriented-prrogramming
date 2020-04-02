from Movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return " <User {}>".format(self.name)

    def watched_movies(self):
        watched_films_list = []
        [watched_films_list.append(movie) for movie in self.movies if movie.watched]
        return watched_films_list  # return list(filter(lambda movie: movie.watched, self.movies)) another version

    def add_movies(self, name, genre):
        film = Movie(name, genre, False)
        self.movies.append(film) if film not in self.movies else None
        # if film not in self.movies:
        #     self.movies.extend(film)
        #     return self.movies
