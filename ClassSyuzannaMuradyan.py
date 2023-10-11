# # 1. Create a class using a type of animal.
class Animal():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def get_personal_information(self):
        print(f"A am a {self.name}")
        print(f"I am {self.sex}")

class DomesticAnimals(Animal):
    def __init__(self, name, sex, legs):
        super().__init__(name, sex)
        self.legs = legs
    def get_personal_information(self):
        super().get_personal_information()
        print(f"I have {self.legs} legs")
    def voicing(self):
        print("I am meowling.")

class WildAnimals(Animal):
    def __init__(self, name, sex, color):
        super().__init__(name, sex)
        self.color = color
        print(f"A am {self.color}")
    def _huntable(self):
        print("I am huntable")
    def _eat(self):
        print("I eat meat.")


dom1 = DomesticAnimals("cat", "female", 4)
dom1.get_personal_information()
dom1.voicing()

wild1 = WildAnimals("lion", "male", "brown")
wild1.get_personal_information()
wild1._eat()
wild1._huntable()







#
#
# # 2. Create a student class.

class Student():
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def learn(self):
        print("Middle grade is 88.")
    def read(self):
        print("The level of reading is higher.")
    def speak(self):
        print(self.get_information())
    def get_information(self):
        return "Personal number is:0165845"

person1 = Student("Aram", 23)
print(f"The student`s name is: {person1.name}")
print(f"His age is: {person1.age}")
person1.learn()
person1.read()
person1.speak()

#
# # 3. Create a class for triangular.
#
# class Geometrical_shape():
    side1 = None
    side2 = None
    side3 = None
    base = None
    hight = None
    def __init__(self, side1, side2, side3, base, hight):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.hight = hight
    def calculate_area(self):
        return (self.base * self.hight) / 2
    def calculates_parimeter(self):
        return self.side1 + self.side2 + self.side3
    def get_some_info(self):
        print("The sum of all types of triangle is equal to 180°")


triangular = Geometrical_shape(4, 5, 3, 5, 4)
print(F"The first side of a triangular is: {triangular.side1}")
print(f"The second sside is: {triangular.side2}")
print(f"The third side is: {triangular.side3}")
print(f"The base is: {triangular.base},"
      f" The height is: {triangular.hight}")
print(f"Area of triangular is: {triangular.calculate_area()}")
print(f"Parimeter of triangilar is: {triangular.calculates_parimeter()}")
triangular.get_some_info()



#
# class Triangular():
    side1 = None
    side2 = None
    side3 = None
    def init (self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def verify_triangular(self, side1, side2, side3):
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            return True
        else:
            return False
triangular1 = Triangular()
side1 = int(input("Please enter the first number: "))
side2 = int(input("Please enter the second number: "))
side3 = int(input("Please enter the third number: "))
print(triangular1.verify_triangular(side1, side2, side3))












