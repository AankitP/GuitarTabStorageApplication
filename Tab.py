debug = False

class GuitarTab:
    def __init__(self, Title = "Title", Artist = "Artist", Location = "Location"):
        self.Title = Title
        self.Artist = Artist
        self.Location = Location
    
    def __str__(self):
        return(f"Song Title: {self.Title}\nArtist: {self.Artist}")

    def getTitle(self):
        return self.Title
    
    def getArtist(self):
        return self.Artist
    
    def getLocation(self):
        return self.Location
    
    def setTitle(self, title):
        self.Title = title
    
    def setArtist(self, artist):
        self.Artist = artist

    def setLocation(self, location):
        self.Location = location

    # this is so that I can store the object to a json
    def to_dict(self):
        return {
            "Title": self.Title,
            "Artist": self.Artist,
            "Location": self.Location
        }

if(debug):
    newSong = GuitarTab()

    print(newSong)

    newSong.setTitle("Song1")
    newSong.setArtist("Artist1")
    newSong.setLocation("Location1")

    print(newSong)