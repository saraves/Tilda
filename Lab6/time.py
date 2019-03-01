from songFile import Song
import timeit

def main():
    """
    Program som utför några uppgifter och tar tid på dem
    """

    # Skapar Song-objekt
    lines = int(input('Hur många rader vill du läsa in? '))
    songlist, songdict = readFile(lines)
    elements = len(songlist)

    last = songlist[elements-1]
    item = last.artist
    #item = 'Kristian Meurman'

    # Söker efter ett element med linjärsökning i osorterade listor - O(n)
    seqTime = timeit.timeit(stmt = lambda: seqSearch(songlist, item))
    print('Linjärsökning tog', round(seqTime, 4), 'sekunder')

    # Sorterar listor med Quick Sort - O(nlog(n))
    quickTime = timeit.timeit(stmt = lambda: quickSort(songlist), number = 1)
    print('The Quick Sort tog', round(quickTime, 4), 'sekunder')

    # Söker med binärsökning i sorterade listor - O(log(n))
    binaryTime = timeit.timeit(stmt = lambda: binarySearch(songlist, item))
    print('The Binary Search tog', round(binaryTime, 4), 'sekunder')

    # Slår upp element i dictionary - O(1)
    dictTime = timeit.timeit(stmt = lambda: dictSearch(songdict, item))
    print('Uppslagning i dictionary tog', round(dictTime, 4), 'sekunder')

def dictSearch(songdict, item):
    """
    Returnerar True om item finns i songdict
    """
    if item in songdict:
        return True
    else:
        return False

def binarySearch(songlist, item):
    """
    Rekursiv implementation av binärsökning (från boken)
    """
    if len(songlist) == 0:
        return False
    else:
        midpoint = len(songlist)//2
        if songlist[midpoint] == item:
            return True
        else:
            if item.__lt__(songlist[midpoint]):
                return binarySearch(songlist[:midpoint], item)
            else:
                return binarySearch(songlist[midpoint+1:], item)

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

def seqSearch(songlist, item):
    """
    Returns True if testartist exists in songlist, false annars (från boken)
    """
    pos = 0
    found = False

    while pos < len(songlist) and not found:
        if songlist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def readFile(lines):
    """
    Läser in fil
    """

    songlist = []
    songdict = {}
    linenumber = 0

    with open('unique_tracks.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            if linenumber == lines:
                break
            info = line.split("<SEP>")           # Gör varje rad till en lista
            for i in range(len(info)):
                info[i] = info[i].strip()        # Ta bort '\n'
            newSong = Song(info[0], info[1], info[2], info[3])

            songlist.append(newSong)             # Lägg till i lista
            songdict[newSong.artist] = newSong   # Lägg till i dict under 'artistnamn'
            linenumber = linenumber + 1

    return songlist, songdict


if __name__ == '__main__':
    main()

# timeit - svar på frågorna
# stmt: statement I want to measure, defaults to 'pass'
# number: number of executions you want to run the stmt
# vad är det timeit tar tid på? Hur lång tid det tar att utföra
# det statement som ska mätas.
# vad skrivs ut av ett anrop på timeit? Tiden det tar att
# utföra stmt
