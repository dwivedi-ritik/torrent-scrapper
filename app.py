from flask import Flask , jsonify , render_template , url_for , request

import torrent

from torrs import piratebay

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def home():
    if request.method == 'POST':
        inp = request.form['query']
        msg = ""
        check_lists = request.form.getlist("cb")
        if "tpb" in check_lists:
            movie_details  = piratebay.pirate(inp)
        else:
            tor = torrent.Tor1377x()
            movie_details = tor.get_json(inp)
       
        if len(movie_details["movie_info"]) == 0:
            msg = "No Result Found"
        else:
            msg = ""
        return render_template("index.html" , res=movie_details["movie_info"] , msg=msg)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
