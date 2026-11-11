import tkinter
#buttons
button_value = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+","="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_value) #5
column_count = len(button_value[0]) #4

#colors
color_orange = "#FC6214"
color_dark_gray = "#414141"
color_light_gray = "#838383"
color_white = "#F2F2F2"
color_black = "#000000"

#windo setup
window = tkinter.Tk()
window.title("calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
lable = tkinter.Label(frame, text="0", font = ("Arial", 45), background=color_black,
                      foreground=color_white, anchor="e", width=column_count)

lable.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_value[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1, column=column)

        
frame.pack()

#a+b, a-b, a*b, a/b
A = "0"
operator = None
B = None


def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = lable["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    lable["text"]  = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    lable["text"]  = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    lable["text"]  = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    lable["text"]  = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = lable["text"]
                lable["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value =="AC":
            clear_all()
            lable["text"] = "0"

        elif value == "+/-":
            result = float(lable["text"]) * -1
            lable["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(lable["text"]) / 100
            lable["text"] = remove_zero_decimal(result)

    else:
        if value == ".":
            if value not in lable["text"]:
                lable["text"] += value
        elif value in "0123456789":
            if lable["text"] == "0":
                lable["text"] = value
            else:
                lable["text"] += value


window.mainloop()