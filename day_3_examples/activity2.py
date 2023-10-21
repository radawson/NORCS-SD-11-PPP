class Person:
    def __init__(self, in_name, in_age):
        self.name = in_name
        self.age = in_age

    def get_name(self):
        return self.name

class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.has_ticket = False
        self.in_zoo = False

    def buy_ticket(self):
        self.has_ticket = True
        if self.age < 18:
            print(f"{self.name} has purchased a child ticket.")
        else:
            print(f"{self.name} has purchased an adult ticket.")

    def enter_zoo(self, zoo):
        if self.has_ticket:
            self.has_ticket = False
            zoo.add_customer(self)
            self.in_zoo = True
        else:
            print("Please purchase a ticket before attempting to enter the zoo.")

    def exit_zoo(self, zoo):
        if self.in_zoo:
            zoo.remove_customer(self)
            self.in_zoo = False
        else:
            print("You are not in the zoo.")

class Zoo:
    def __init__(self, name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"{customer.name} has entered {self.name}")

    def remove_customer(self, customer):
        self.customers.remove(customer)
        print(f"{customer.name} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

class Animal:
    def __init__(self, name):
        self.name = name
        self.noise = "nothing"

    def get_name(self):
        return self.name

    def make_noise(self):
        print(f'{self.name} says "{self.noise}".')

    def eat_food(self):
        print("All creatures need sustenance")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f'{self.name} goes "Blub blub".')

    def eat_food(self):
        print(f"A {self.name} eats seafood.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.noise = "chirp chirp"

    def eat_food(self):
        print(f"A {self.name} eats seeds, nuts and berries.")

class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.noise = 'Ooo eee ooo ahh ahh'

    def eat_food(self):
        print(f"A {self.name} eats seeds, fruit, leaves, and bark.")

if __name__ == "__main__":
    nyc_zoo = Zoo("NYC Zoo")

    salmon = Fish("salmon")
    robin = Bird("robin")
    bonobo = Chimp("bonobo")
    nyc_zoo.add_animals([salmon, robin, bonobo])

    alice = Customer("Alice", 25)
    bob = Customer("Bob", 20)
    charlie = Customer("Charlie", 10)
    dave = Customer("Dave", 30)
    for c in [alice, bob, charlie, dave]:
        c.buy_ticket()
        c.enter_zoo(nyc_zoo)
    nyc_zoo.visit_animals()
    for c in [alice, bob, charlie, dave]:
        c.exit_zoo(nyc_zoo)
