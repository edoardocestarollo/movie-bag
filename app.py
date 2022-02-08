from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

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

+app.config['MONGODB_SETTINGS'] = {
+    'host': 'mongodb://localhost/movie-bag'
+}
+
+initialize_db(app)

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