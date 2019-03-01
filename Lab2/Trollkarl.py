from linkedQFile import LinkedQ

def main():
    cards = input('Vilken ordning ligger korten i?')
    cards = cards.split(" ")            # Seperate line into a list

    for x in range(len(cards)):
        cards[x-1] = int(cards[x-1])    # From string to int

    try:
        queue = ArrayQ()                    # Create new queue-object
    except:
        queue = LinkedQ()

    for card in cards:
        queue.enqueue(card)

    print('Det kommer ut i denna ordning:', end=' ')
    while not queue.isEmpty():
        move = queue.dequeue()
        queue.enqueue(move)
        print(str(queue.dequeue()),end=' ')

main()


# 7 1 12 2 8 3 11 4 9 5 13 6 10
