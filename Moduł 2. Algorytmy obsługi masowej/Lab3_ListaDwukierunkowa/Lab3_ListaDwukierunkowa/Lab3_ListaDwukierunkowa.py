# 10.03.2020, Kamil Matula gr. D
# Zestaw II, algorytm 5: Lista Dwukierunkowa

class Node(object):
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self): #(poprzedni, aktualny, następny)
        if self.previous == None: prev = "None"
        else: prev = str(self.previous.data)
        if self.next == None: nex = "None"
        else: nex = str(self.next.data)
        return "(" + prev + ", " + str(self.data) + ", " + nex + ")"

class ListaDwukierunkowa(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        tab = []
        currentNode = self.head
        while currentNode != None:
            tab.append(str(currentNode))
            currentNode = currentNode.next
        return str(tab)

    def addToList(self, index, element):
        if index < 0 or index > self.count() or index != int(index):
            print("Nieprawidłowy indeks!")
        elif index == 0:
            self.head = Node(element, self.head)
            if self.head.next != None: self.head.next.previous = self.head
        else:
            currentIndex = 0
            currentNode = self.head
            while currentIndex < index - 1:
                currentNode = currentNode.next
                currentIndex += 1
            currentNode.next = Node(element, currentNode.next, currentNode)

    def removeFromList(self, index):
        if index < 0 or index > self.count() - 1 or index != int(index):
            print("Nieprawidłowy indeks!")
        elif index == 0:
            if self.head.next != None: self.head.next.previous = None
            self.head = self.head.next
        else:
            currentIndex = 0
            currentNode = self.head
            while currentIndex < index - 1:
                currentNode = currentNode.next
                currentIndex += 1
            if currentNode.next.next != None: currentNode.next.next.previous = currentNode
            currentNode.next = currentNode.next.next

    def count(self):
        currentIndex = 0
        currentNode = self.head
        while currentNode != None:
            currentIndex += 1
            currentNode = currentNode.next
        return currentIndex

    def showAt(self, index):
        if index < 0 or index > self.count() or index != int(index):
            print("Nieprawidłowy indeks!")
        else:
            currentIndex = 0
            currentNode = self.head
            while currentIndex < index:
                currentIndex += 1
                currentNode = currentNode.next
            return currentNode.data

    def indexOf(self, element):
        currentIndex = 0
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == element: return currentIndex
            currentIndex += 1
            currentNode = currentNode.next
        return None

Lista = ListaDwukierunkowa()
Lista.addToList(0,213)
Lista.addToList(0,32)
Lista.addToList(1,23)
Lista.addToList(3,81)
Lista.addToList(4,5)
Lista.addToList(2,2)
print(Lista)
Lista.removeFromList(5)
Lista.removeFromList(0)
Lista.removeFromList(1)
print(Lista)
print(Lista.count())
print(Lista.showAt(2))
print(Lista.indexOf(213))
print(Lista.indexOf("A"))