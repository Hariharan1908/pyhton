# class founder():
#     def naveen(Jack_Daniels):
#         print("Founder of Wishky")
# class CEO():
#     def sharan(Corona_extra):
#         print("Founder of actor_MGR")

# class Manager(founder,CEO):
#     def ram(priya):
#         print("managed by whole sale alcohol")

# child1 = Manager()
# child1.naveen()
# child1.sharan()
# child1.ram()


# class vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def moves(self):
#         print('moves along')    

#     def get_makes_model(self):
#         print(f"i am {self.name} {self.model}") 


# class airplane(vehicle):

#     def moves(self):
#         print('flies along')

# class Truck(vehicle):

#     def moves(self):
#         print("drives along")

# class bike(vehicle):

#     def moves(self):
#         print("rides along")


# my_plane = airplane('sharan', 'skyscapper', 42)
# my_plane.get_makes_model()
# my_plane.moves()


# my_truck = airplane('Truck1', 'model1')
# my_truck.get_makes_model()
# my_truck.moves()


# my_bike = airplane('Hero', 'honda')
# my_bike.get_makes_model()
# my_bike.moves()





class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(5), Circle(2)]
for shape in shapes:
    print(f"Area of shape: {shape.area()}")









# Parent class
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print(f"{self.name} is making a sound")

# # Child class inheriting from Animal
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)  # Calling the superclass constructor
#         self.breed = breed
    
#     def speak(self):  # Method overriding
#         print(f"{self.name} is barking")

# # Creating objects of the classes 
# animal = Animal("Generic Animal", 5)
# dog = Dog("Buddy", 3, "Labrador")

# # Accessing methods of the classes
# animal.speak()  # Output: Generic Animal is making a sound
# dog.speak()  # Output: Buddy is barking
