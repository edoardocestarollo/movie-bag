from email.mime import image
from flask import Flask, jsonify, request
from flask_cors import CORS

def getImageSrc(image):
    return IMAGES_PATH + "/" + image

def filterMovie(movie):
    if "poster" in movies.keys():
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
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@app.route('/movies')
def show_movies():
    return jsonify(movies)

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