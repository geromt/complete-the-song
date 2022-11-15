import flask

import db_controller
from song import Song

app = flask.Flask(__name__)


@app.route('/')
@app.route("/index")
def index():
    db_controller.create_db()
    return flask.render_template("index.html")


@app.route('/songs')
def songs():
    song_list = db_controller.get_all_songs()
    return flask.render_template("songs.html", songs=song_list)


@app.route("/song/<id_song>")
def incomplete_song(id_song):
    song = db_controller.get_song_by_id(id_song)
    return flask.render_template("song.html", song=song)


@app.route("/add-song")
def add_song():
    return flask.render_template("add-song.html")


@app.route("/adding-song", methods=["POST"])
def adding_song():
    print("hola")
    if flask.request.method == "POST":
        print("entro")
        db_controller.add_song(flask.request.form["title"],
                               flask.request.form["author"],
                               flask.request.form["url"],
                               flask.request.form["lyrics"])
    return flask.redirect(flask.url_for("index"))


@app.route("/eval-song", methods=["POST"])
def eval_song():
    print("holi")
    if flask.request.method == "POST":
        print(flask.request.form["correct-words"])
        correct_words = flask.request.form["correct-words"].split(" ")
        wrong_answers = []
        wrong = 0
        for i in range(len(correct_words)):
            input_word = flask.request.form[str(i)]
            if input_word != correct_words[i]:
                wrong += 1
                wrong_answers.append([correct_words[i], input_word])
        return flask.render_template("eval.html",
                                     total=len(correct_words),
                                     wrong=wrong,
                                     wrong_answers=wrong_answers)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
