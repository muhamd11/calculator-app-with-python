num_1 = float(input("please enter your first number: "))
operation = input("please enter your operation ")
num_2 = float(input("please enter your second number:"))

if operation == "+":
    print(float(num_1) + float(num_2))

elif operation == "-":
       print(float(num_1) - float(num_2))

elif operation == "/":
       print(float(num_1) / float(num_2))

elif operation == "*":
       print(float(num_1) * float(num_2))
else:
    print("please check your operation and try again")




