from csv import DictWriter, writer

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
        self.movies.append(film)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name.lower() != name.lower(), self.movies))

    def checking_for_duplicates(self):
        for movie in self.movies:
            if self.movies.count(movie) > 1:
                return self.movies.remove(movie)
        return False

    def saving_to_file(self, name):
        with open(name, 'w', encoding='utf8')as file:
            csv_writer = writer(file)
            csv_writer.writerow(['NAME', 'GENRE', 'STATUS'])
            for movie in self.movies:
                csv_writer.writerow([movie.name, movie.genre, movie.watched])

