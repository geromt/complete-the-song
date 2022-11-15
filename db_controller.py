import sqlite3

from song import Song


def create_db():
    connection = sqlite3.connect("songs.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS song(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL UNIQUE,
        author TEXT NOT NULL,
        url TEXT NOT NULL,
        lyrics TEXT NOT NULL);""")


def add_song(title, author, url, lyrics):
    connection = sqlite3.connect("songs.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO song(title, author, url, lyrics) VALUES (?, ?, ?, ?);",
                       (title, author, url, lyrics))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def get_song_by_id(id_song):
    connection = sqlite3.connect("songs.db")
    cursor = connection.cursor()

    res = cursor.execute("SELECT * FROM song WHERE id=?;", id_song)
    return Song(*res.fetchone())


def get_all_songs():
    connection = sqlite3.connect("songs.db")
    cursor = connection.cursor()

    res = cursor.execute("SELECT * FROM song;")
    songs = []
    for row in res.fetchall():
        songs.append(Song(*row))

    return songs
