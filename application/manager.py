from flask import render_template, request, redirect, url_for

from application import app
from application.db_controller import get_all_songs, get_song_by_id, add_song_bd


@app.route('/')
@app.route("/index")
def index():
    """ Render the main page """
    return render_template("index.html")


@app.route('/songs')
def songs():
    """ Render the page with the song list """
    song_list = get_all_songs()
    return render_template("songs.html", songs=song_list)


@app.route("/song/<id_song>")
def incomplete_song(id_song):
    """Render the song page of the given id"""
    song = get_song_by_id(id_song)
    return render_template("song.html", song=song)


@app.route("/video/<id_song>")
def video_popup(id_song):
    """ Render only the video of the given id"""
    song = get_song_by_id(id_song)
    return render_template("video.html", video_url=song.url)


@app.route("/add-song")
def add_song():
    """ Render the form to add a song """
    return render_template("add-song.html")


@app.route("/adding-song", methods=["POST"])
def adding_song():
    """ Manage the POST request of the /add-song """
    if request.method == "POST":
        add_song_bd(request.form["title"], request.form["author"],
                    request.form["url"], request.form["lyrics"])
    return redirect(url_for("index"))


@app.route("/eval-song", methods=["POST"])
def eval_song():
    """ Render the evaluation page """
    if request.method == "POST":
        return render_template("eval.html", tries=request.form["tries"])
