class SecondSong():
    """
    Klass som skapar artistobjekt
    """

    def __init__(self, artistid, artist, songtitle, tracklength, year):
        self.artistid = artistid
        self.artist = artist
        self.songtitle = songtitle
        self.tracklength = float(tracklength)
        self.year = year

    def uniqueTrack(self):
        """
        Returnerar 'artist + songtitle'
        """
        return self.artist + ' ' + self.songtitle

    def __lt__(self, other):
        """
        Returnerar True om self är mindre än other i hänsyn till artistnamn,
        annars False
        """
        return self.tracklength < other.tracklength

    def __le__(self, other):
        """
        Returnerar True om self är mindre än eller lika med other i hänsyn till
        artistnamn
        """
        return self.tracklength <= other.tracklength

    def __gt__(self, other):
        """
        Returnerar True om self är större än other i hänsyn till artistnamn
        """
        return self.tracklength > other.tracklength

    def __ge__(self, other):
        """
        Returnerar True om self är större än eller lika med other i hänsyn till
        artistnamn
        """
        return self.tracklength >= other.tracklength
