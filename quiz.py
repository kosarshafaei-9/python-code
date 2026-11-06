#kosar shafaei - Quiz 

menu = {
    "1" : "Python Quiz",
    "2" : "Math Quiz", 
    "3" : "Exit"
}

python_quiz = {
    "with which word we can see the output?" : "print",
    "How can we change the input into number form?" : "int",
    "how can we stop the terminal?" : "ctrl+c"
}

math_quiz = {
    "4(5+5)? " : "40",
    "(6-2)(8+3)? " : "44",
    "2**3? " : "8"
}

print("welcome to this quiz.")

while True:

    for key in menu:
        print(key, "-", menu[key])

    choice = input("selcet an option: ")
    score = 0

    if choice == "1":
        print("\nPython Quiz.")
        for question in python_quiz:
            answer = input(question + "")
            if answer == python_quiz[question]:
                print("correct!")
                score += 1
            else:
                print("wrong!")
                print("correct answer is: ", python_quiz[question])
        print("your score:", score, "/", len(python_quiz))

    elif choice == "2":
        print("\nMath Quiz.")
        for question in math_quiz:
            answer = input(question + " ")
            if answer == math_quiz[question]:
                print("correct!")
                score+=1
            else:
                print("wrong!")
                print("correct answer is:", math_quiz[question])  
        print("your score:", score, "/", len(math_quiz))

    elif choice == "3":
        print("Exit the quiz...")
        break

    else:
        print("your choice is invalid.")
