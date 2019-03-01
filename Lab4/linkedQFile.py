class Node():

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedQ():

    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, item):
        newNode = Node(item)

        if self.isEmpty():                  # Om listan är tom
            self.__first = newNode
        else:                               # Om listan inte är tom
            self.__last.next = newNode      # Flytta pekaren för näst sista noden
        self.__last = newNode               # Flytta last pekaren

    def dequeue(self):
        item = self.__first.data
        self.__first = self.__first.next    # Flytta first pekaren
        return item

    def isEmpty(self):
        return self.__first == None

if '__name__' == '__main__':
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)
