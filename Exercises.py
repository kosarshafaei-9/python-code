# #kosar shafaei_ yazdahom_ nicandishan##

# #Exeercise (page 15)
# price = float(input("Enter product price: "))
# tax = price * 0.09
# total = price + tax
# print("total price: " + str(total))

# # Exercise (page 15)
# Manager = input("pleas enter manager name:")
# year = str(input("Please enter the year of establishment: "))
# print("welcome Lady/Gentleman", Manager, "in thins market. we've started this market since:", year)

# #Exercise (page 18)
# # First
# things = ["book", "phone", "mouse", "book", "headset"]
# print(things)
# things[3] = "External HDD"
# print(things)
# #Second
# number = [30,50,70,90]
# print(number[1])
# #Third
# Cars =["BMW M5", "Porsche 911", "Audi R8", "Mercedis", "Aston Martin", "Rolls Royce"]
# print(Cars)
# Cars.insert(1, "1984")
# Cars.insert(3, "1964")
# Cars.insert(5, "2007")
# Cars.insert(7, "1921")
# Cars.insert(9, "1951")
# Cars.insert(11, "1925")
# print(Cars)

# #Exercise (page 21)
# tasks = ["study", "sleep", "exercise", "rest"]
# print(tasks)
# tasks.pop()
# print(tasks)

# #Exercise (page 25-1)
# math_score = int(input("please enter your math score:"))
# English_score = int(input("please enter your English score:"))
# if math_score and English_score >= 17 :
#     print("congratulation, you can study in computer major.")
# else:
#     print("sorry, you can't study in computer major.")

# #Exercise (page 25-2)
# Age = int(input("please enter your age:"))
# if Age >= 18:
#     print("Access allowed")
# else:
#     print("Access denied")

# #Exercise (page 27)
# user_name = input("please enter your user name:")
# code = input("please enter your password:")

# if user_name == "manager" and code == "9876":
#     print("welcome, you logged in successfully")
# else:
#     ("Error!! your user name or password is uncorrect!")

# #Exercise (page 29)
# nationality = input("please enter your country:")
# age = int(input("please enter your age:"))
# if nationality == "Iran" and age >= 18:
#     print("congratulation, you can log in.")
# else: 
#     print("sorry. you don't allow to log in.")

# #Exercise (page 31-1)
# fruit = input("Which fruit did you choose to buy? apple/orange/banana:")
# count = int(input("How much fruit did you choose? "))
# if fruit == "apple" and count <= 5 :
#     print("Discount applied")
# else:
#     print("No discount")

# #Exercise (page 31-2)
# age = int(input("please neter your age:"))
# if age >= 18 and age <= 25:
#     print("Welcome, young adult.")
# elif age >= 26:
#     print("Welcom, adult.")
# else:
#     print("you are underage.")

# #Exercise (page 31-3)
# status = input("What is the situation? Deliverd/Sent/Registered:")
# if status == "Delivered":
#     print("Your oreder has been successfully delivered.")
# elif status == "Sent":
#     print("your order is in the way."),
# elif status == "Registered":
#     print("your order is being processed.")
# else:
#     ("Status unknown.")

# #Exercise (page 31-4)
# score = int(input("please enter your score:"))
# if score >= 90:
#     print("Exelent")
# elif score >= 69 and score < 90:
#     print("Good"),
# elif score < 68 and score >= 50:
#     print("Pass")
# else:
#     print("Fail")

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

#  #Exercise (page 54 - 2)
# user = {}

# user["username"] = input("please enter your name: ")
# user["age"] = input("please enter your age: ")
# user["password"] = input("please enter your passwprd: ")

# print(user)

# #Exercise (page 56)
# invenroty = {
#     "bag" : 5,
#     "ball" : 8,
#     "laptop" : 3,
#     "mouse" : 10, 
#     "flash memory" :14
# }
# if "bag" in invenroty:
#     print("there is bag in items.")
#     invenroty_value = invenroty.pop("bag")
#     print("item removed: ", invenroty_value)
# else:
#     print("there is no bag.")
# print(invenroty)
 
# # exercise (page 66 - 1)
# def sum_numbers(num1, num2):
#     print("sum:", num1 + num2)

# sum_numbers(20, 15)

# # exercise (page 66 - 2)
# def names(name1, name2, name3):
#     print("name 1:", name1)
#     print("name 2:", name2)
#     print("name 3:", name3)

# name1 = input("Enter first number: ")
# name2 = input("Enter second number: ")
# name3 = input("Enter third number: ")

# names(name1, name2, name3)

# #Exercise (page69 - 1)
# def string_length(text):
#     count = 0
#     for char in text:
#         count += 1
#     return count
# user_text = input("Enter your number: ")
# Length = string_length(user_text)
# print("Length: ", Length)

# #Exercise (page69 - 2)
# def max_number(numbers):
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# numbers = [10, 5, 3, 6, 19, 48, 23]
# print("Max:", max_number(numbers))

# #Exercise (page 70
# def num_diff(score1, score2):
#     diff = score1 - score2
#     if diff < 0:
#         diff = - diff
#     return diff

# score1 = int(input("Enter score 1:"))
# score2 = int(input("Enter score 2:"))
# print(num_diff(score1, score2))

#Exercise (page 73)
cities = ["Mashhad", "Tehran", "Shiraz", "Esfahan"]
sorted(cities, reverse=True)
print(sorted(cities))