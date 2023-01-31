# class Projector:
#     def __init__(self, color, year, model = "NEC"):
#         self.color = color
#         self.year = year
#         self.model = model

#     # def visualise(self):
#     #     print(f"Projector of model{self.model} is visualising")

#     def description(self):
#         print(f"Color: {self.color}")
#         print(f"Year: {self.year}")
#         print(f"Mdel: {self.model}")

#     def __str__(self):
#         return self.model

#     def __repr__(self):
#         return self.year, self.model
        
        
        




# p1 = Projector("white", 2022, "MEC")
# p2 = Projector("red", 2025, "xyz")
# # # p1.visualise()
# # # p2.visualise()
# p2.description()
# ## prit(p.color)
# #print(p.year)
# # print(p.model)
# print(p1.__dict__)

# projectors = []
# for i in range(2):
#     color = input("enter color:")
#     year = input("enter year:")
#     model = input("enter model")
#     p = Projector(color, year, model)
#     projectors.append(p)

# print(projectors)



# class Student:
#     def __init__(self, _id, name, contact, addresh):
#         self._id = _id
#         self.name = name
#         self.contact = contact
#         self.addresh = addresh
#         self.total_attendence = 0
    
#     def update_attendence(self):
#         self.total_attendence += 1

#     def view_attendence(self):
#         return self.total_attendence
# s = Student(1, "Ram", "87654", "ktm")
# s2 = Student(2, "syam", "82652", "birgunj")
# s.update_attendence()
# s2.update_attendence()
# print(s2.__dict__)
# s2.update_attendence()
# print(s.view_attendence())
# print(s2.update_attendence)
# print(Student.view_attendence(s))



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price

# tshirt = Product("Tshirt", 5000)
# jacket = Product("Jacket", 2500)
# # print(tshirt._Product_price)
# print(f"Before setting: {tshirt.price}")



# class Calculator:
#     def __init__(self, num1, num2) -> None:
#         self.a = num1
#         self.b = num2
    

#     def add(self):
#         return self.a + self.b

#     def diiferent(self):
#         return self.a - self.b

#     def product(self):
#         return self.a * self.b

#     def division(self):
#         return self.a / self.b

#     @staticmethod
#     def square_root(num):
#         return num**0.5

# c = Calculator(10, 20,)
# print(c.add())
# print(Calculator.square_root(25))


# class Student:
#     collage = "ABC collage" # class or static variable

#     def __init__(self, name, contact):
#         self.name = name
#         self.contct = contact

# print(Student.collage)
# s = Student("Ram", "552205")
# print(s.collage)
# print(s.__dict__)


# class User:
#     def __init__(self, usename, password):
#         self.username = usename 
#         self.password = password

#     @classmethod
#     def create_user_with_random_password(cls, username):
#         return cls(username, "default_password")
    
# u = User("ram@gmail.com", "demo412695")
# print(u.__dict__)


# u2 =User.create_user_with_random_password("hari@gmail.com")
# print(u2.__dict__)















