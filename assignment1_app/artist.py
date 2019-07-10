class Artist:
    def __init__(self, id, name, genre, desc, albums, inactive):
        self.id = id
        self.name = name
        self.genre = genre
        self.desc = desc
        self.albums = albums
        self.inactive = inactive

    def __str__(self):
        return str(self.id) + ", " + self.name







 

  