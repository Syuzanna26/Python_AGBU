# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
# Create a function to display the entire attribute and their values in Student class.
class Student():
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None
    def reading_attributes(self):
        print(f"Student's ID number is: {self.student_id}")
        print(f"His/Her name is: {self.student_name} ")
        print(f"His/her class number is: {self.student_class}")


student1 = Student(4, "Aram")
student1.student_class = 2
student1.reading_attributes()


# 2. Create a Vehicle class without any variables and methods

class Vehicle():
    pass


# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

newvehicle = Vehicle(240, 20)
print(f"My new vehicle`s max speed is {newvehicle.max_speed} and its mileage is {newvehicle.mileage}.")



# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle():
    def __init__(self, model, max_speed, mileage):
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def __init__(self, model, max_speed, mileage):
        super().__init__(model, max_speed, mileage)


schoolbus = Bus("minibus T50", 260, 100)
print(f"The schoolbus model is: {schoolbus.model}. Its max speed is {schoolbus.max_speed}. Its mileage is: {schoolbus.mileage}.")



# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle():
    def __init__(self, model, max_speed, mileage):
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def __init__(self, model, max_speed, mileage):
        super().__init__(model, max_speed, mileage)
    def seating_capacity(self):
        self.seating_capacity = 50
        print(f"The seating capacity of this minibus is: {self.seating_capacity}")


schoolbus = Bus("minibus T50", 260, 100)
print(f"The schoolbus model is: {schoolbus.model}. Its max speed is {schoolbus.max_speed}. Its mileage is: {schoolbus.mileage}.")
schoolbus.seating_capacity


