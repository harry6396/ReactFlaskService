## This class is used to hold the values of the Songs
class Songs:
    songName=''
    songCategory=''
    songRating=''
    songArtist=''
    danceability=''
    energy=''
    keys=''
    loudness=''
    modes=''
    speechiness=''
    acousticness=''
    instrumental=''
    liveness=''
    valence=''
    tempo=''
    duration=''
    timesignature=''
    rank=''

    def __init__(self, songName, songCategory, songRating, songArtist, danceability, energy, keys, loudness, modes,
                 speechiness, acousticness, instrumental, liveness, valence, tempo, duration, timesignature, rank):
        self.songName = songName
        self.songArtist = songArtist
        self.songCategory = songCategory
        self.songRating = songRating
        self.danceability = danceability
        self.energy = energy
        self.keys = keys
        self.loudness = loudness
        self.modes = modes
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumental = instrumental
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration = duration
        self.timesignature = timesignature
        self.rank = rank



