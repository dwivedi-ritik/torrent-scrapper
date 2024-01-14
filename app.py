from flask import Flask


from models import Torrent
from routes.torrent_routes import torr_blueprint
from routes.torrent_provider_route import torrent_provider_blueprint

# import torrent

# from torrs import piratebay

from models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/torrlord"
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(blueprint=torr_blueprint, url_prefix="/api/torrent")
app.register_blueprint(blueprint=torrent_provider_blueprint, url_prefix="/api/provider")

# @app.route("/" , methods=["GET" , "POST"])
# def home():
#     if request.method == 'POST':
#         inp = request.form['query']
#         msg = ""
#         check_lists = request.form.getlist("cb")
#         if "tpb" in check_lists:
#             movie_details  = piratebay.pirate( query = inp , top=False)

#         else:
#             try:
#                 tor = torrent.Tor1377x()
#                 movie_details = tor.get_json(inp)
#             except Exception:
#                 tor = torrent.Tor1377x()
#                 movie_details = tor.get_json(inp)


#         if len(movie_details["movie_info"]) == 0:
#             msg = "No Result Found"
#         else:
#             msg = ""

#         return render_template("index.html" , res=movie_details["movie_info"] , msg=msg)
#     else:
#         movie_details  = piratebay.pirate(query=None , top=True)
#         msg = ""
#         return render_template("index.html" , res=movie_details["movie_info"] , msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
