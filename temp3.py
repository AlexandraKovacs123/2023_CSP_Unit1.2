# write a method called addSubtract()
# this method should take a parameter called operation
# when method is called, ask the user for two numbers
# do the operation of the parameter to the inputs

def addSubtract(operation):
    num1 = [2, 5, 6, 98, 32, 123]
    num2 = [5, 67, 89, 34, 1, 4]
    index = 0
    for nums in num1:
        if operation == "add":
            print(num1[index] + num2[index])
            index += 1
        else:
            print(num1[index] - num2[index])
            index += 1


addSubtract("add")
addSubtract("subtract")
