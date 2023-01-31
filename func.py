# def welcome():
#     print("this is python")
# welcome()    


# def welcome(name, addresh): #parameters
#     print("welcome", name,  )
#     print( "addresh", addresh)
     
# name = input("enter  your name")
# addresh = input("enter your addresh")

# welcome(name, addresh) #arguments



# a = 10
# b = 20
# total = a+b
# # print("the sum of {} and {} is {}".format(a, b, total))
# print(f"the sum of {a} and {b} is {total}.")



# def profile(name, addresh, contact):
#     print(f"Name:{name}")
#     print(f"Addresh:{addresh}")
#     print(f"Contact:{contact}")

# profile("sonu", "ktm", "456541232322") #positional arguments
# # profile("ram", "987452123", "ktm")
# # profile(contact="9562323", name="sonu", addrsh="ktm")



# def addition(num1, num2=1):
#     print(num1+num2)

# addition(10,)




# def addition(num1,num2):
#     print(num1+num2)

# def product(num1, num2):
#     return num1 * num2

# a = addition(10, 20)
# print(f"Addition: {a}")
# res = product (10, 5)
# print(f"product:{res}")



# def multiple_arguments(*a):
#     print(a)

# multiple_arguments(1,2, 3, 4, 5, 6, "python", "Ram")



main = []
even = []
odd = []
duplicate = []
abc = 0
for i in range(4):
    val = input("enter your nuber")

    main.append(val)
for j in main:
  if (j%2==0):
    even.append(j)
  else:
    odd.append(j)
print(main)
print(even)
print(odd)


# students = []
# for i in range(5):
#     name= input("plese enter student name")
#     students.append(name.capitalize())

# print(students)
