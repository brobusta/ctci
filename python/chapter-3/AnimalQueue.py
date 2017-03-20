from Queue import Queue

class Animal(object):
    def __init__(self, name = ''):
        self.name = name
        self.order = 0

class Dog(Animal):
    def __init__(self, name = ''):
        Animal.__init__(self, name)

    def __str__(self):
        return "[Dog " + self.name + "," + str(self.order) + "]"

class Cat(Animal):
    def __init__(self, name = ''):
        Animal.__init__(self, name)

    def __str__(self):
        return "[Cat " + self.name + "," + str(self.order) + "]"

class AnimalQueue(object):
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()
        self.time = 0

    def enqueue(self, animal):
        if type(animal) is Dog:
            self.dog_queue.add(animal)
        elif type(animal) is Cat:
            self.cat_queue.add(animal)
        else:
            raise ValueError("invalid type")
        animal.order = self.time
        self.time += 1

    def dequeueDog(self):
        return self.dog_queue.remove()

    def dequeueCat(self):
        return self.cat_queue.remove()

    def dequeueAny(self):
        if self.dog_queue.isEmpty():
            return self.dequeueCat()
        elif self.cat_queue.isEmpty():
            return self.dequeueDog()

        topDog = self.dog_queue.peek()
        topCat = self.cat_queue.peek()
        if topDog.order < topCat.order:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

if __name__ == '__main__':
    queue = AnimalQueue()

    d1 = Dog("Alice")
    c1 = Cat("John")
    d2 = Dog("Bob")
    c2 = Cat("Peter")
    queue.enqueue(d1)
    queue.enqueue(c1)
    queue.enqueue(c2)
    queue.enqueue(d2)

    print queue.dequeueCat()
    print queue.dequeueAny()
    print queue.dequeueDog()

