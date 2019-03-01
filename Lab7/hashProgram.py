from dictHashFile import DictHash
from hashfil import Hashtabell
from songFile import Song
import timeit

def main():
    '''
    Kallar på rätt program
    '''

    choose = int(input('Vilken del vill du köra? Välj 1 eller 2: '))

    while choose != 1 and choose != 2:
        choose = int(input('Välj 1 eller 2: '))
        print(choose)

    if choose == 1:
        partOne()
    elif choose == 2:
        partTwo()

def partOne():
    '''
    Del 1. Hashtabell som bygger på pythons inbyggda dictionary.
    '''
    lines = int(input('Hur många rader vill du läsa in, max 281:'))
    songHash = DictHash()
    songHash = readFile(lines, songHash)

    item = 'Kristian Meurman'

    # Slår upp element i dictionary - O(1) (97 rader tog 0.287 s i labb 6)
    dictTime = timeit.timeit(stmt = lambda: dictSearch(songHash, item))
    print('Uppslagning i dictionary tog', round(dictTime, 4), 'sekunder')

def partTwo():
    '''
    Del 2. Egen hashtabell.
    '''
    lines = int(input('Hur många rader vill du läsa in, max 281:'))
    songHash = Hashtabell(281)
    songHash = readFile(lines, songHash)

    print('Vi fick', songHash.collisions, 'kollisioner')

def readFile(lines, songHash):
    """
    Läser in fil.
    songHash är hashtabell implementerad med metod från del 1 eller del 2.
    """

    linenumber = 0

    with open('unique_tracks.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            if linenumber == lines:
                break
            info = line.split("<SEP>")           # Gör varje rad till en lista
            for i in range(len(info)):
                info[i] = info[i].strip()        # Ta bort '\n'
            newSong = Song(info[0], info[1], info[2], info[3])

            key = newSong.artist
            data = newSong.songtitle

            songHash.put(key, data)  # Lägg till i dict under 'artistnamn'
            linenumber = linenumber + 1

    return songHash

def dictSearch(songdict, item):
    """
    Returnerar True om item finns i songdict
    """
    if item in songdict:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
