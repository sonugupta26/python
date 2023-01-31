# strl = "Geekyshows"
# n = len(strl) 
# for i in range (n):
#     print(strl[i])



# main = []
# even = []
# odd = []
# dublicate = []
# for i in range(1, 5):
#     val = int(input("enter element"))
#     main.append(val)

# print(main)

# for j in main:
#     if(j%2==0):
#         even.append(j)
#     else:
#         odd.append(j)  
# for j in main:
#     if j==main:
#         dublicate.append(j)

# print("dublicate:", dublicate)
  

# print("even:", even)
# print("odd:", odd)




main = []
even = [] 
odd = []
duplicate = []
for i in range(6):
    num = int(input("enter any number:"))
    if num in main:
        duplicate.append(num)
#     else:
#         if num % 2==0:
#             even.append(num)
#         else:
#             odd.append(num)
    main.append(num)
print(main)
print(even)
print(odd)
print(duplicate)



# main = [1, 5, 8, 8, 5, 6, 44, 55, 66, 88,1, 2, 31, 1, 2, 3, 4]
# num = [1, 2, 3, 4, 5, 77, 88]
# aa = []

# if num in main:
#     aa.append(num)
# print(aa)    