from sqlite3 import connect, Error

from application.song import Song

DB_PATH = "application/db/songs.db"


def get_connection():
    try:
        connection = connect(DB_PATH)
        return connection
    except Error:
        print(Error)


def create_db():
    con = get_connection()
    cursor = con.cursor()

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS song(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL UNIQUE,
            author TEXT NOT NULL,
            url TEXT NOT NULL,
            lyrics TEXT NOT NULL);""")
    except Error:
        print(Error)
    finally:
        con.close()


def add_song_bd(title, author, url, lyrics):
    con = get_connection()
    cursor = con.cursor()

    try:
        cursor.execute("INSERT INTO song(title, author, url, lyrics) VALUES (?, ?, ?, ?);",
                       (title, author, url, lyrics))
        con.commit()
    except Error:
        print(Error)
    finally:
        con.close()


def get_song_by_id(id_song):
    con = get_connection()
    cursor = con.cursor()

    try:
        res = cursor.execute("SELECT * FROM song WHERE id=?;", id_song)

        return Song(*res.fetchone())
    except Error:
        print(Error)
    finally:
        con.close()


def get_all_songs():
    con = get_connection()
    cursor = con.cursor()

    try:
        res = cursor.execute("SELECT * FROM song;")
        songs = [Song(*row) for row in res.fetchall()]

        return songs
    except Error:
        print(Error)
    finally:
        con.close()
