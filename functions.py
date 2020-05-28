def addition(num1,num2,num3,num4):
        result = num1 + num2 + num3 + num4
        print ("{0} + {1} = {2}".format(num1,num2,num3,num4,result))

def subtraction(num1,num2,num3,num4):
        result = num1 - num2 - num3 - num4
        print ("{0} - {1} = {2}".format(num1,num2,num3,num4,result))

def multiplication(num1,num2,num3,num4):
        result = num1 * num2 * num3 * num4
        print ("{0} * {1} * {2}".format(num1,num2,num3,num4,result))


def division(num1,num2,num3,num4):
    if num2 == 0.0:
        print(" Cannot divide by Zero")
    else:
        result = num1 / num2
        print ("{0} / {1} = {2}".format(num1,num2,num3,num4,result))
