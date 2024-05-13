from utils import class_inheritance as animals,\
    converters as cv, guess_number as puzzle


# From converters module
# It's a separated py file that contains useful code
# Modules are very useful 
# because with them you can keep your project organized

# unit converters
print(f"My dog weights 10kg. In pounds it's {cv.kg_to_lbs(10)}lbs")
print(f"My cat is 28 inches long. In centimeters it's {cv.in_to_cm(28)}cm")

# emoji dict
# ./utils/converters.py file line 43
print(f"{cv.emoji_converter("It's a very good example of the usefulnes of dictionaries :), like this >:( :( :D")}")

example_cat = animals.Cat("Max")
example_dog = animals.Dog("Charlie")

# inherited methods and attributes
print(f"{"*"*5} Inherited methods and atributes {"*"*5}")
print(f"example_dog's name is: {example_dog.name}")
print(f"example_cat's name is: {example_cat.name}")
example_dog.walk()
example_cat.walk()

# individual methods and attributes
print(f"\n{"*"*5} Unique methods and atributes {"*"*5}")
print(f"example_dog's species is: {example_dog.species}")
print(f"example_cat's species is: {example_cat.species}")
example_dog.speak()
example_cat.speak()
example_dog.sit_down()
example_cat.play()

# Small puzzle ./utils/guess_number
success, answer = puzzle.guess_random_number(10, 3)
if success:
    print(f"Congratulations, you guessed right. It was: {answer}")

