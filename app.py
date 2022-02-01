from flask import Flask, jsonify, request
from flask_cors import CORS

IMAGES_PATH = "/static/img"
POSTER_FORMAT_NAME = "{}_Poster.jpg"

def getImageSrc(image):
    return IMAGES_PATH+"/"+image

def filterMovie(movie):
    if "poster" in movie.keys():
        movie["poster"] = getImageSrc(movie["poster"])
    if "director_avatar" in movie.keys():
        movie["director_avatar"] = getImageSrc(movie["director_avatar"])
    return movie

def filterMovies(movies):
    return [ filterMovie(m.copy()) for m in movies]


app = Flask(__name__)
CORS(app)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "director": "Frank Darabont",
        "director_avatar": "Frank-Darabont_avatar.jpeg",
        "genres": ["Drama"],
        "poster": "Shawshank-Redemption_Poster.jpg",
        "release_date": "September 10, 1994",
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "director": "Francis Ford Coppola",
       "director_avatar": "Francis-Ford-Coppola_avatar.jpg",
       "genres": ["Crime", "Drama"],
       "poster": "The-Godfather_Poster.jpg",
       "release_date": "March 14, 1972",
    }
]

@app.route("/movies")
def show_movies():
    return jsonify(filterMovies(movies))


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movie = movies[index]
    movies.pop(index)
    return jsonify(movie), 200

app.run()