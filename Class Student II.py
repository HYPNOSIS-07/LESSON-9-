class student:
   grade = 9
   name = "Dev"
   def introduction(self):
      print("Hi, I am a student")
   def details(self):
      print("My name is", self.name)
      print("I am in grade", self.grade)

ob = student()
ob.introduction()
ob.details()