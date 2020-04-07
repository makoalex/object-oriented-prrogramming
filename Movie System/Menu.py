import os
import json
from Users import User


def find_file():
    name = input('Please enter name:\n')
    filename = '{}.json'.format(name).lower()
    if is_file(filename):
       with open(filename) as f:
           data = json.load(f)
           user = User.load_file(data)
    else:
        user = User(name)

    keep_running = True
    while keep_running:
        selection = input("\nEnter 'a' to add a film, 'd' to delete a film \n"
                          "Enter 's' to see the films, 'w' to set a film as watched \n"
                          "Enter 'c' to see the list of watched movies\n"
                          "Enter 'q to save and quit'\n")

        if selection == 'a':
            film_name = input('enter the film name').capitalize().strip()
            film_genre = input(' enter the film genre').capitalize().strip()
            print(user.add_movies(film_name, film_genre))

        elif selection == 'd':
            movie_inp = input('enter a movie to delete from the list')
            print(user.delete_movie(movie_inp))
        elif selection == 's':
            for movie in user.movies:
                print("'Name:' {} 'Genre:' {}, 'Watched:' {} ".format(movie.name, movie.genre,movie.watched))
        elif selection == 'w':
            movie_name = input(' the film you ar e looking for?')
            print(user.change_status(movie_name))
        elif selection == 'c':
            for movie in user.watched_movies():
                print("'Name:' {} 'Genre:' {}, 'Watched:' {} ".format(movie.name, movie.genre,movie.watched))
        elif selection == 'q':
            with open(filename, 'w') as json_file:
                json.dump(user.data_to_json(), json_file)
            keep_running = False






def is_file(filename):
    return os.path.isfile(filename)


find_file()
