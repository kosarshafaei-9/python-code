# #Exercise (page37 - 1)
# time= int(input("please enter the time reaminig: "))

# for n in range(time,0, -1):
#     print("time remainig", n)

# print("your food is ready!")

# #Exercise (page37 - 1)
# count = 0

# for n in range(5):
#     height = float(input("please enter your height: "))
#     count+= height
# average = count/5
# print("Average height:", average)

# #Exercise (45-1)



# #Exercise (45-2)
# food = []
# food_name = input("please enter your food name: ")

# while food_name != "done":
#     food.append(food_name)
#     print("your order for", food_name, "has been added")
#     food_name = input("please enter your food name: ")
# print(food)

# #Exwecise (page51 - 1)
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# if 10 in numbers:
#     print("there is number 10.")
# else:
#     print("there is no number 10.")

#  #Exercise (page 51 - 2)
# fruits = {"apple", "banana", "orange", "mango", "berry"}
# f = input("which fruit do you want? ")

# if f in fruits:
#     print("we have", f, "for you")
# else:
#     print("sorry, we don't have", f)
 
#  #Exercise (page 54 - 1)
# product = {
#     "name" : "computer",
#     "price" : "120m"
# }
# product["price"] = "140m"

# print(product)

 #Exercise (page 54 - 2)
user = {}

user["username"] = input("please enter your name: ")
user["age"] = input("please enter your age: ")
user["password"] = input("please enter your passwprd: ")

print(user)