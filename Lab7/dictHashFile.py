class DictHash():
    '''
    Implementation av hashtabell med pythons inbyggda dictionary
    '''

    def __init__(self):
        self.size = 97
        self.hashtable = {}

    def __getitem__(self, key):
        '''
        Gör det möjligt att skriva d[key] istället för d.search(key)
        '''
        return self.get(key)

    def __contains__(self, key):
        '''
        Gör det möjligt att skriva 'if key in d'.
        Returnerar True om key finns i hashtabellen. False annars.
        '''
        found = False
        if self.get(key):
            found = True
        return found

    def hashfunction(self, astring, tablesize):
        '''
        Beräkna hashvärdet för strängen. Returnera slot-värdet. (Från boken)
        '''
        sum = 0
        for pos in range(len(astring)):
            sum = sum * 32 + ord(astring[pos])
        return sum % tablesize

    def put(self, key, data):
        '''
        Lagrar data i hashvärdet key
        '''
        self.hashtable[key] = data

    def get(self, key):
        '''
        Returnerar datat som är lagrat i hashvärdet key
        '''
        found = False
        if self.hashtable[key]:
            found = self.hashtable[key]
        return found


if __name__ == '__main__':
    d = DictHash()
    d.put('1', 'hej')
    d.put('2', 'på')
    d.put('3', 'dig')

    print(d.hashtable)

    if '3' in d:
        print('i 3 finns', d['3'])
    else:
        print(d)
