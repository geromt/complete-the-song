from flask import render_template, request, redirect, url_for

from application import app
from application.db_controller import get_all_songs, get_song_by_id, add_song_bd


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/songs')
def songs():
    song_list = get_all_songs()
    return render_template("songs.html", songs=song_list)


@app.route("/song/<id_song>")
def incomplete_song(id_song):
    song = get_song_by_id(id_song)
    return render_template("song.html", song=song)


@app.route("/add-song")
def add_song():
    return render_template("add-song.html")


@app.route("/adding-song", methods=["POST"])
def adding_song():
    if request.method == "POST":
        add_song_bd(request.form["title"], request.form["author"],
                    request.form["url"], request.form["lyrics"])
    return redirect(url_for("index"))


@app.route("/eval-song", methods=["POST"])
def eval_song():
    if request.method == "POST":
        correct_words = request.form["correct-words"].split(" ")
        wrong_answers = []
        wrong = 0
        for i in range(len(correct_words)):
            input_word = request.form[str(i)]
            if input_word != correct_words[i]:
                wrong += 1
                wrong_answers.append([correct_words[i], input_word])
        return render_template("eval.html",
                               total=len(correct_words),
                               wrong=wrong,
                               wrong_answers=wrong_answers)
