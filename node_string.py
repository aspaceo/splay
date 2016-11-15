class album:
    def __init__(self, artist, name, year, rating):
        self.artist = artist
        self.name = name
        self.year = year
        self.rating = rating

        ## album is always instigated without preceded by, succeded by  -------
        self.preceded = None
        self.succeded = None

    def new_album(self, album):
        album.preceded = self
        self.succeded = album


class discography:
    def __init__(self):
        self.debut = None


    def insert(self, album):
        ## will search discography and insert the album in the correct place  -
        if self.debut == None:
            self.debut = album
        else:
            ## already a disc in string, find end of list and insert
            self.debut.new_album(album)

one = album(artist = 'The National', name = 'The National', year = 2001, rating = 5)
two = album(artist = 'The National', name = 'Sad Songs For Dirty Lovers', year = 2001, rating = 6)

the_national_disc = discography()
the_national_disc.insert(one)
the_national_disc.insert(two)


the_national_disc.debut.preceded
the_national_disc.debut.succeded.name






