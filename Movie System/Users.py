import json

from Movie import Movie


class User:
    user_list = []

    def __init__(self, name):
        self.name = name
        self.movies = []
        User.user_list.append(self)

    def __repr__(self):
        return " <User {}>".format(self.name)

    def watched_movies(self):
        watched_films_list = []
        [watched_films_list.append(movie) for movie in self.movies if movie.watched]
        return watched_films_list  # return list(filter(lambda movie: movie.watched, self.movies)) another version

    def add_movies(self, name, genre):
        film = Movie(name, genre, False)
        self.movies.append(film)

    def change_status(self, name):
        for movie in self.movies:
            if movie.name.lower() == name.lower():
                movie.watched = True

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name.lower() != name.lower(), self.movies))

    def checking_for_duplicates(self):
        for movie in self.movies:
            if self.movies.count(movie) > 1:
                return self.movies.remove(movie)
        return False

    def data_to_json(self):
        return {
            'name': self.name,
            'movies': [movie.json() for movie in self.movies]
        }

    def file(self, name):
        with open(name, 'w') as file:
            json.dump(self.data_to_json(), file)

    @classmethod
    def load_file(cls, data):
        user = User(data['name'])
        movies = []
        for d in data['movies']:
            movie_data = Movie(d['name'], d['genre'], d['watched'])
            movies.append(movie_data)
            print("'Name:' {} 'Genre:' {}, 'Watched:' {} ".format(d['name'], d['genre'], d['watched']))
        user.movies = movies
        return user

