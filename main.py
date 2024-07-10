# se doreste o aplicatie care sa iti sugereze un film random
# dintr-o lista top 250 de filme din lume
import json
import random

import requests
from movie import Movie


def get_all_movies(config: dict):
    try:
        headers = {"User-Agent": config["mimic_browser_header"]}
        response = requests.get(config['imdb_url'], headers=headers)
        if response.status_code == 200:
            text = response.text
            start_index = text.find('"item":')
            end_index = text.find('"ratingCount":')

            while end_index != -1:
                movie_parse = text[start_index:end_index]
                movie_dict = json.loads("{" + movie_parse[:-1] + "}}}")['item']
                movie = Movie(movie_dict["name"], movie_dict["aggregateRating"]["ratingValue"],
                              movie_dict["description"])
                # print(movie.name)
                text = text[(end_index + len("ratingCount")):]
                start_index = text.find('"item":')
                end_index = text.find('"ratingCount":')

            return movie.list_of_movies

        else:
            raise Exception(f"Wrong error code {response.status_code}. {response.text}")
    except Exception as e:
        print("Failed to get movies from movie database", e)


if __name__ == '__main__':

    with open("config.json", "r") as f:
        config = json.loads(f.read())

    movie_list = get_all_movies(config)

    while True:
        response = input("Do you want to see a good movie ? Y/N : ")
        if response.lower() == "y":
            movie = random.choice(movie_list)
            message = f"""
            Movie name: {movie.name}
            Rating: {movie.rating}
            Description: {movie.description}"""
            print(message)
        else:
            break