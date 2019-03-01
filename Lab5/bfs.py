from bintreeFile import Bintree
from linkedQFile import LinkedQ
from parentFile import ParentNode

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

    q = LinkedQ()                       # skapar en kö

    node = ParentNode(startord)         # skapa en ParentNode av startord

    q.enqueue(node)                     # lägger in startordet i kön
    gamla.put(startord)                 # lägger in startordet i gamlabarn-trädet

    foundPath = None

    while not q.isEmpty():              # Gå igenom alla barn, barnbarn, ...
        parent = q.dequeue()
        if parent.word == slutord:
            foundPath = True
            break
        makechildren(parent, q, svenska, gamla)

    if foundPath:
        print('Det finns en väg från', startord, 'till', slutord, '\nVägen är:')
        parent.writechain()          # parent är slutordets ParentNode
    else:
        print('Det finns ingen väg från', startord, 'till', slutord)


def makechildren(parent, q, svenska, gamla):
# Skapar alla barn till startord från ordlistan

    alfabet = 'abcdefghijklmnopqrstuvwxyzåäö'
    ord = parent.word

    for i in range(len(ord)):                  # iterera genom startord
        for j in alfabet:                       # iterera genom alfabetet
            barn = ord[:i] + j + ord[i+1:]

            # om ordet finns i ordlistan och inte redan finns i trädet
            if svenska.__contains__(barn) and not gamla.__contains__(barn):
                barnNod = ParentNode(barn, parent)          # skapa ParentNode av barn som pekar på parent

                q.enqueue(barnNod)                  # lägg till i kön
                gamla.put(barn)                     # lägg till i gamla barn




main()
