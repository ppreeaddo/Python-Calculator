first_number = input("First: ")
second_number = input("Second: ")
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = float(first_number) + float(second_number)
    print(result)
elif operation =="-":
    result = float(first_number) - float(second_number)
    print(result)
elif operation == "*":
    result = float(first_number) * float(second_number)
    print(result)
elif operation == "/":
    result = float(first_number) / float(second_number)
    print(result) 