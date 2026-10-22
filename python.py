# #Calculating the price of a product and tax
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

#Exercise (page 31-4)
score = int(input("please enter your score:"))
if score >= 90:
    print("Exelent")
elif score >= 69 and score < 90:
    print("Good"),
elif score < 68 and score >= 50:
    print("Pass")
else:
    print("Fail")