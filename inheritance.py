#child class "IS A" parent class
#TEacher "IS A" person => this is  correct
#Dog "IS A" person=> this is incorrect

# class Person:
#     def __init__(self, name, addresh):
#         self.name = name
#         self.addresh = addresh
  
#     def walk(self):
#         print(f"{self.name} is walking")

# class Teacher(Person):
#     def __init__(self, name, addresh, designation):
#         super().__init__(name, addresh)
#         self.designation = designation

#     def teach(self):
#         print(f"{self.name} is teaching")

# class Student(Person):
#     def __init__(self, name, addresh, roll_number):
#         super().__init__(name, addresh)
#         self.roll = roll_number

#     def walk(self):
#         super().walk()
#         print(f"{self.name} is running")
    
# t =Teacher("sonu", "ktm", "prof")
# t.walk()
# t.teach()       
# s=Student("monu", "birgunj", "abc")



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Person(User):
    def __init__(self, username, password, name, addresh):
        super().__init__(username, password)
        self.name = name
        self.addresh = addresh

    def profile(self):
        print(f"Name:{self.name}")
        print(f"addresh:{self.addresh}")
        print(f"Username:{self.username}")

class Student(Person):
    def __init__(self, username, password, name, addresh, rollno):
        super().__init__(username, password, name, addresh)
        self.roll_number = rollno

    def profile(self):
        super().profile()
        print(f"Roll number:{self.roll_number}")

class Teacher(Person):
    def __init__(self, username, password, name, addresh, designation):
        super().__init__(username, password, name, addresh)
        self.desination = designation

    def Profile(self):
        super().profile()
        print(f"Desingnation:{self.designation}")


s = Student("ran@gmail.com", "51562", "Ram", "ktm", 1)
s.profile()

t = Teacher("sonu@gmail.com", "41541", "rohit", "sss", "sikta")
t.profile()


# class ProductPriceError(Exception):
#     pass

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price <= 0:
#             raise ProductPriceError("price can not be less than zero.")
#         self.__price = price

# tshirt = Product("Tshirt", 500)
# try:
#     tshirt.price = -100
#     print(f"Without exception:{tshirt.price}")
# except ProductPriceError as msg:
#     print(msg)
#     print(f"After exception:{tshirt.price}")


























