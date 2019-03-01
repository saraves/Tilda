from secondSongFile import SecondSong
import timeit

def main():
    """
    Program som hittar den N:te längsta låten i en osorterad lista
    """

    # Skapar Song-objekt och lägger i songlist
    N = int(input('Vilken N:te längsta låt vill du hitta?'))
    songlist, songdict = readFile()

    seqTime = timeit.timeit(stmt = lambda: searchSong(songlist, N), number = 1)
    print('Linjärsökning i osorterad lista tog', round(seqTime, 4), 'sekunder')

    # Sorterar listor med Quick Sort - O(nlog(n))
    quickTime = timeit.timeit(stmt = lambda: quickSort(songlist), number = 1)
    print('The Quick Sort tog', round(quickTime, 4), 'sekunder')

    print('\nDen', N, ':e längsta låten är:'
    '\nMed linjärsökning', searchSong(songlist, N), 'sekunder\nMed Quick Sort:', wantedSong(songlist, N), 'sekunder')

def wantedSong(songlist, N):
    """
    Returnerar den N:e längsta låten från sorterade listan songlist
    """
    index = len(songlist)-N
    return songlist[index].tracklength

def quickSort(songlist):
    """
    Kallar på quickSortHelper med pivot-värde och rightmark (från boken)
    """
    quickSortHelper(songlist, 0, len(songlist)-1)

def quickSortHelper(songlist, first, last):
    """
    Utför partition rekursivt, vänster del av varje lista först (från boken)
    """
    if first<last:

        splitpoint = partition(songlist, first, last)

        quickSortHelper(songlist, first, splitpoint-1)
        quickSortHelper(songlist, splitpoint+1, last)

def partition(songlist, first, last):
    """
    Utför delningsprocessen (från boken)
    """
    pivotvalue = songlist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and songlist[leftmark] <= pivotvalue:
            leftmark = leftmark+1

        while songlist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark-1

        if rightmark < leftmark:
            done = True
        else:
            temp = songlist[leftmark]
            songlist[leftmark] = songlist[rightmark]
            songlist[rightmark] = temp

    temp = songlist[first]
    songlist[first] = songlist[rightmark]
    songlist[rightmark] = temp

    return rightmark

def searchSong(songlist, N):
    """
    Funktion som givet en osorterad lista söker efter den näst längsta låten
    Linjärsökning - O(n)
    """
    found = {}

    # Iterera tills found är N-1 lång
    for i in range(N):                          # Gå igenom song list N gånger
        longest = 0
        for songobject in songlist:             # Varje songobjekt
            if float(songobject.tracklength) > float(longest) and songobject.uniqueTrack() not in found:
                longestsong = songobject
                longest = songobject.tracklength

        found[longestsong.uniqueTrack()] = longestsong.tracklength

    return longest

def readFile():
    """
    Läser in filen sang-artist-data.txt
    """

    songlist = []
    songdict = {}
    linenumber = 0

    with open('sang-artist-data.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            info = line.split("\t")           # Gör varje rad till en lista
            for i in range(len(info)):
                info[i] = info[i].strip()        # Ta bort '\n'
            newSong = SecondSong(info[0], info[1], info[2], info[3], info[4])

            songlist.append(newSong)             # Lägg till i lista
            songdict[newSong.artist] = newSong   # Lägg till i dict under 'artistnamn'
            linenumber = linenumber + 1

    return songlist, songdict


if __name__ == '__main__':
    main()
