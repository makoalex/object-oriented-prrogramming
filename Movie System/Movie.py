class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self. genre = genre
        self.watched = watched

    def __repr__(self):
        return " Film {} genre {}.".format(self.name, self.genre)
    def __eq__(self, other):
        return self.name == other.name and self.genre == other.genre


