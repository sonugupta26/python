# a = lamda x, y:x*y
# print(a(10,20))


#map(func, iterable_object)
# a = [3 ,9 ,8 , 5, 9, 15]

# def increase_by_one(n):
#     return n+2

# output = list(map(increase_by_one, a))
# print(output)


# name_list = ["ram", "shyam", "site", "meera"]


# abc = list(map(lambda name:name.capitalize(), name_list))
# abc = list(map(str.capitalize, name_list))

# print(abc)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# abc = list(filter(lambda n:n % 2 == 0, a))
# print(abc)



# a = "2,4,6,d,8,9,e,4"
# # print(sum(map(int, filter(str.isdigit,a.split(",")))))
# num_list = a.split(",")
# numbers = filter(str.isdigit,num_list)
# print(sum(map(int, numbers)))


marks_of_students = [
    {"name": "Ram",
    "marks":{"maths": 80, "science": 85, "computer": 90},
    },
    {"name": "Sita",
    "marks": {"maths":87, "science": 79, "computer": 85},
    },
    {"name": "Hari",
    "marks":{"maths": 90, "science":75, "computer": 88},
    },
    
]

for i in marks_of_students:
    print(i.get("name"))
    abc = (sum(i.get("marks").values()))
    print(abc)
    # if  Ram > Sita and Ram > Hari:
    #     print("ram")

    # elif Sita > Ram and Sita > Hari:
    #     print("sita")
    # else :
    #     Hari > Ram and Hari > Sita
    #     print("hari")


































