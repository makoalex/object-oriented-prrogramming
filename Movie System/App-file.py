from Movie import Movie
from Users import User
film = Movie('Predator', 'Action', True)
new_film = Movie('Invisible man', 'Thriller', False)
user = User('Ola')
# user.movies.append(film)
# user.movies.append(new_film)
# print(user.watched_movies())
print(user.add_movies('Titanic', 'Romance'))

user.add_movies('Marley and me', 'Comedy')
print(user.movies)

