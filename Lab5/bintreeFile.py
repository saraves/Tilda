class Bintree:
# objekt är binärt sökträd.
# lägger till värde, kollar om värde finns,
# skriver ut träd inorder

    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print('\n')

def putta(p, newvalue):
    # sorterar in newvalue i trädet, p = parent
    if p:
        if newvalue < p.value:                  # går till vänster
            p.left = putta(p.left, newvalue)
            return p
        if newvalue > p.value:                  # går till höger
            p.right = putta(p.right, newvalue)
            return p
        if newvalue == p.value:                 # värdet finns redan
            print('Värdet finns redan')
            return p
    else:
        p = Node(newvalue)                      # skapar en ny nod med newvalue
        return p

def finns(p, value):
    # kollar om ett värde finns i trädet
    letar = True
    while letar:
        if p == None:
            return False
        if p.value == value:
            return True
        if value < p.value:
            return finns(p.left, value)
        if value > p.value:
            return finns(p.right, value)

def skriv(p):
    # Skriver ut trädet inorder
    if p != None:
        skriv(p.left)
        print(str(p.value))
        skriv(p.right)

class Node():
    # Nod-klass. Har ett värde och två pekare, left och right

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    # testkod
    bintree = Bintree()
    bintree.put(50)
    bintree.put(7)
    bintree.put(100)
    bintree.put(25)
    bintree.write()
