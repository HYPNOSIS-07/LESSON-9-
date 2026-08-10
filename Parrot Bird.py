class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue = parrot("Blue", 10)
woodstock = parrot("Woo", 15)

print ("Blue is a {}".format(blue.species))
print ("Woodstock is also a {}".format(woodstock.species))

print("Blue is a {}".format(blue.species))
print("Woodstock is also a {}".format(woodstock.species))

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(woodstock.name, woodstock.age))