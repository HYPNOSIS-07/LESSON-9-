class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is", self.name)


# Creating objects
tom = Robot("Tom")
jerry = Robot("Jerry")

# Introducing the robots
tom.introduce()
jerry.introduce()