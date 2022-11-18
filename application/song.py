import random


class Song:
    def __init__(self, id_song, title, author, url, lyrics):
        self.id_song = id_song
        self.title = title
        self.author = author
        self.url = url
        self.lyrics = lyrics
        self.last_words = []

    def gen_incomplete(self):
        incomplete = []
        i = 0
        for line in self.lyrics.split('\n'):
            if line.strip() == '':
                incomplete.append('<br/><br/>')
                continue

            words = line.strip().split(" ")
            n = random.randint(0, len(words)-1)

            self.last_words.append(words[n])

            incomplete.append(" ".join(words[:n]))
            incomplete.append(f' <input id="{i}" type="text" name="{i}"> ')
            incomplete.append(" ".join(words[(n+1):]))
            incomplete.append(f' <br/>')
            i += 1

        return "".join(incomplete)

    def get_correct_words(self):
        return " ".join(self.last_words)


