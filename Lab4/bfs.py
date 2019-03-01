from bintreeFile import Bintree
from linkedQFile import LinkedQ

def main():
# Skapar binärträd av ordlistan (svenska) och dumbarnen (gamla)
# Frågar efter start- och slutord

    svenska = Bintree()         # ordlistan
    gamla = Bintree()           # dumbarnen
    with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()         # ett trebokstavsord per rad
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)

    startord = input('Vad är startordet?\n')
    slutord = input('Vad är slutordet?\n')

    q = LinkedQ()
    q.enqueue(startord)
    gamla.put(startord)

    foundPath = None

    while not q.isEmpty():              # Gå igenom alla barn, barnbarn, ...
        ord = q.dequeue()
        if ord == slutord:
            foundPath = True
            break
        makechildren(ord, q, svenska, gamla)

    if foundPath:
        print('Det finns en väg från', startord, 'till', slutord)
    else:
        print('Det finns ingen väg från', startord, 'till', slutord)


def makechildren(ord, q, svenska, gamla):
# Skapar alla barn till startord från ordlistan

    alfabet = 'abcdefghijklmnopqrstuvwxyzåäö'

    for i in range(len(ord)):                  # iterera genom startord
        for j in alfabet                   # iterera genom alfabetet
            barn = ord[:i] + j + ord[i+1:]
            if svenska.__contains__(barn) and not gamla.__contains__(barn):
                q.enqueue(barn)
                gamla.put(barn)

main()
