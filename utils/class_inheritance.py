# Main class
# Classes are used in the OOP (Object Oriented Programming)
class Animals:
    def __init__(self, name : str) -> None:
        self.name = name
    
    
    def walk(self):
        print(f"({self.species}){self.name}: * walks in")

# Child classes 
# Inherited the "name" attribute 
# and the "walk" method
class Dog(Animals):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.species = "Dog"
        
        
    def speak(self):
        print(f"({self.species}){self.name}: BARK!")
        
        
    def sit_down(self):
        print(f"({self.species}){self.name}: * sits down")
    

class Cat(Animals):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.species = "Cat"
    
    def speak(self):
        print(f"({self.species}){self.name}: * ignores you")
        
        
    def play(self):
        print(f"({self.species}){self.name}: * plays with a toy")

