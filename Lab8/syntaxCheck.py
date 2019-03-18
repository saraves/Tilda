from linkedQFile import LinkedQ

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

class SyntaxError(Exception):
    ''' User defined exception class'''
    pass

def readMolekyler(q):
    '''
    <molekyl>|<molekyl><molekyler>
    '''
    readMolekyl(q)
    if q.peek():
        readMolekyler(q)


def readMolekyl(q):
    '''
    <atom>|<atom><num>
    '''
    readAtom(q)
    if q.peek() != None and q.peek().isdigit():
        readnum(q)


def readAtom(q):
    '''
    <LETTER>|<LETTER><letter>
    '''
    readLETTER(q)
    # Kolla om <LETTER> följs av <letter>
    if q.peek() != None and q.peek() in alphabet:
        readletter(q)


def readLETTER(q):
    '''
    A|B|C|...|Z
    '''
    letter = q.dequeue()
    if letter in ALPHABET:
        return
    raise SyntaxError('Fel stor bokstav: ' + letter)


def readletter(q):
    '''
    a|b|c|...|z
    '''
    letter = q.dequeue()
    if letter in alphabet:
        return
    raise SyntaxError('Fel liten bokstav: ' + letter) # Det här kommer ALDRIG hända

def readnum(q):
    '''
    2|3|4|...
    '''
    number = q.dequeue()
    if number.isdigit():
        # Tal större än 0
        if int(number) > 0:
            # Specialfall om första talet = 1
            if int(number) == 1:
                # Ettan följs av fler siffror är okej
                if q.peek() == None:
                    raise SyntaxError('"1" följt av None')
                elif not q.peek().isdigit():
                    raise SyntaxError('"1" följt av bokstav')

            # Vid en följd av siffror
            while q.peek() != None and q.peek().isdigit():
                q.dequeue()
            return
    raise SyntaxError('Fel nummer: ' + number)


def printQueue(q):
    '''
    Skriver ut kön
    '''
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = ' ')
    print(' ')


def storeSentance(molekyler):
    '''
    Lagrar alla molekyler i en kö
    '''
    q = LinkedQ()
    for character in molekyler:
        q.enqueue(character)
    return q


def kollaSyntaxen(molekyler):
    '''
    Kollar syntaxen och hanterar syntaxfel
    '''
    q = storeSentance(molekyler)

    try:
        readMolekyler(q)
        return 'Följer syntaxen!'
    except SyntaxError as fel:
        return str(fel)


def main():
    '''
    Program som tar in en följd av molekyler och kontrollerar syntaxen
    '''
    q = LinkedQ()
    molekyler = input('Skriv en följd av atomer: ')
    resultat = kollaSyntaxen(molekyler)
    print(resultat)

if __name__ == '__main__':
    main()


# Felmeddelande vid:
# 1. Molekyl som börjar på liten bokstav
# 2. Molekyl som har siffra mindre än 0
