
class Movie:

    list_of_movies = []

    def __init__(self, name, rating, description):
        self.name = name
        self.rating = rating
        self.description = description
        self.list_of_movies.append(self)


    @classmethod
    def append_movie(cls):
        pass


