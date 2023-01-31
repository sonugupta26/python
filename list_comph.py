# a = [i for i in range(5)]
# print(a)

# b = [{i:i**2} for i in range(1, 15, 2)]
# print(b)

# email = ["1@gmail.com", "2@hotmail.com", "3@gmail.com", "4tahoo.com", "5@gmail.com"]
# gmail_list = [i for i in email if i.endswith("@gmail.com")]
# print(gmail_list)


def multiple_keyboard_argument(**k):
    print(k)

multiple_keyboard_argument(name="ram", contact="9816122", addresh="ktm")


