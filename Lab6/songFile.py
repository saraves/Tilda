class Song():
    """
    Klass som representerar en låt
    """

    def __init__(self, trackid, songid, artist, songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.songtitle = songtitle

    def __lt__(self, other):
        """
        Returnerar True om self är mindre än other i hänsyn till artistnamn,
        annars False
        """
        return self.artist < other.artist

    def __le__(self, other):
        """
        Returnerar True om self är mindre än eller lika med other i hänsyn till 
        artistnamn
        """
        return self.artist <= other.artist

    def __gt__(self, other):
        """
        Returnerar True om self är större än other i hänsyn till artistnamn
        """
        return self.artist > other.artist

    def __ge__(self, other):
        """
        Returnerar True om self är större än eller lika med other i hänsyn till
        artistnamn
        """
        return self.artist >= other.artist
