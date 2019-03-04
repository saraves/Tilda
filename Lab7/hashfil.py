class Hashtabell():
    '''
    Egen implementering av en hashtabell
    '''

    def __init__(self, size):
        self.size = 2000003       # Anpassar tabellens storlek för att minska kollisioner
        self.hashtable = [None] * self.size
        self.collisions = 0

    def __getitem__(self, key):
        '''
        Gör det möjligt att skriva d[key] istället för d.get(key)
        '''
        return self.get(key)

    def __setitem__(self, key, data):
        '''
        Gör det möjligt att skriva d[key] = data istället för d.put(key, data)
        '''
        self.put(key, data)

    def __contains__(self, key):
        '''
        Gör det möjligt att skriva 'if key in d'
        Returnerar True om key finns i hashtabellen. False annars
        '''
        found = False
        if self.get(key):
            found = True
        return found

    def hashfunction(self, astring, tablesize):
        '''
        Beräkna hashvärdet för strängen. Returnera slot-värdet
        Delar från boken och föreläsning 5
        '''
        sum = 0
        for pos in range(len(astring)):
            sum = sum * 32 + ord(astring[pos])
        return sum % tablesize

    def put(self, key, data):
        '''
        Lagrar data i hashvärdet key
        Från boken
        '''

        # Ta fram hashvärde för nyckeln
        hashvalue = self.hashfunction(key, len(self.hashtable))


        # Ny nyckel
        if self.hashtable[hashvalue] == None:
            self.hashtable[hashvalue] = HashNode(key, data)
        else:
            # Ersätt befintligt värde
            if self.hashtable[hashvalue].key == key:
                self.hashtable[hashvalue].data = data
            else:
                # Kollisionsupplösning med 'Plus 3'
                nextslot = self.rehash(hashvalue, len(self.hashtable))
                self.collisions = self.collisions + 1
                while self.hashtable[nextslot] != None and self.hashtable[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.hashtable))

                # Hittat ledigt hashvalue
                if self.hashtable[nextslot] == None:
                    self.hashtable[nextslot] = HashNode(key, data)
                # Ersätter befintligt värde
                else:
                    self.hashtable[nexslot].data = data

    def get(self, key):
        '''
        Returnerar datat som är lagrat i hashvärdet key
        Från boken
        '''
        startslot = self.hashfunction(key, len(self.hashtable))

        data = None
        stop = False            # Gått igenom hela hashtabellen
        found = False           # Hittat nyckeln
        position = startslot

        while self.hashtable[position] != None and not found and not stop:
            # Hittat nyckeln
            if self.hashtable[position].key == key:
                found = True
                data = self.hashtable[position].data
            else:
                position = self.rehash(position, len(self.hashtable))
                # Gått igenom hela hashtabellen
                if position == startslot:
                    stop = True

        if data == None:
            raise KeyError
        else:
            return data

    def rehash(self, oldhash, size):
        '''
        Kollisionsupplösning med Linear probing - 'Plus 3'
        Från boken
        '''
        return (oldhash + 3) % size

class HashNode():
    '''
    Klass för noderna som lagras i hashtabellen
    '''

    def __init__(self, key, data):
        self.key = key
        self.data = data

if __name__ == '__main__':
    alist = {'1':'ett', '2':'två', '3':'tre'}
    hashtabell = Hashtabell(len(alist))

    print('hashtabell["2"]=', hashtabell['2'])
    print('Vi fick', hashtabell.collisions, 'kollisioner')


# "Redovisa hur många krockar det är som mest vid insättning"
# Betyder det vid en insättning? Eller vid insättning av hela atomtabellen?
# Ska tabellen ha en konstant storlek? Eller det primtal som är närmst
# t.ex. (2 * size)
# primtal - 281
# primtal - 2000003
