from bintreeFile import Bintree

def main():
# Läser in svensk fil och gör binärträd. Skriver ut dubletter.
    svenska = Bintree()
    with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()         # ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = ' ')
            else:
                svenska.put(ordet)      # in i sv-sökträd
    print('\n')


# läser in engelsk fil och gör binärträd. Kollar om engelska ord finns i sv-träd
    engelska = Bintree()
    with open('engelska.txt', 'r', encoding = 'utf-8') as engelskfil:
        for rad in engelskfil:
            raden = rad.split()             # lista med varje rad
            for ord in raden:
                ord = ord.strip(',."' )     # lista med varje ord
                if ord in engelska:
                    pass                    # sortera bort dubletter
                else:
                    engelska.put(ord)       # in i eng-sökträd
                    if svenska.__contains__(ord):
                        print(ord, end = ' ')

main()
