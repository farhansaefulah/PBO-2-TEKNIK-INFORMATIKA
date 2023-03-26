#Nama : Farhan Saefulah
#NIM : 210511059
#Kelas : R2


class Animal:
    def __init__(self, species):
        self.species = species
    
    def eat(self):
        print("The animal is eating.")

class Pet(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name
    
    def play(self):
        print("The pet is playing.")
    
class cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
    
    def bark(self):
        print("Meow! MeoW!")

my_cat = cat("Ane", "Golden Retriever")
print("Species:", my_cat.species)
print("Name:", my_cat.name)
my_cat.eat()
my_cat.play()
my_cat.bark()
