from linkedQFile import LinkedQ
from bintreeFile import Bintree

class ParentNode:
    """ Klass som skapar en länkad lista där barnen pekar på sin förälder """
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self):
        if self.parent:
            self.parent.writechain()            # kalla på writechain med sin parent
            
        print(self.word)







if __name__ == '__main__':
    startord = input('Vad är startordet?\n')
    print('Hej')

    q = LinkedQ()               # skapar en kö
    gamla = Bintree()           # dumbarnen

    node = ParentNode(startord)     # skapa en ParentNode av startord

    q.enqueue(node)             # lägger in startordet i kön
    gamla.put(startord)         # lägger in startordet i gamlabarn-trädet
