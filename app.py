from flask import Flask , jsonify
import torrent

app = Flask(__name__)

@app.route("/" , methods=["GET"])
def home():
    return "<h2>Hello World</h2>"

@app.route("/get_movie=<string:query>" , methods=["GET"])
def movie(query):
    tor = torrent.Tor1377x()
    movie_details = tor.get_json(query)
    return jsonify(movie_details)

if __name__ == "__main__":
    app.run()