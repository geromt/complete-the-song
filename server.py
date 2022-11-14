import flask


app = flask.Flask(__name__)


@app.route('/')
@app.route("/index")
def index():
    return flask.render_template("index.html")


@app.route('/songs')
def songs():
    songs = [Song("cancion1", "autor1", "cancion1.html"), Song("cancion2", "author2", "cancion2.html")]
    return flask.render_template("songs.html", songs=songs)


class Song:
    def __init__(self, title, author, route):
        self.title = title
        self.author = author
        self.route = route

    def gen_incomplete(self):



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
