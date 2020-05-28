# import the functions built out in the functions.py
import functions

# Displays a menu option, Runs the script in a loop.

while True:
    print ("What would you like to do?")
    print ("Select 1 for addition")
    print ("Select 2 for subtraction")
    print ("Select 3 for multiplication")
    print ("Select 4 for division")
    #"conditional" or the escape
    print ("Enter Q to Exit")


# Runs the script in a loop.
    choice = input("Enter your choice: ")
    if choice == 'q' or choice =='Q':
        break

    num1 = float(input("Enter the number 1: "))
    num2 = float(input("Enter the number 2: "))
    num3 = float(input("Enter the number 3: "))
    num4 = float(input("Enter the number 4: "))

#peforming the operations

    if choice == '1':
        addition(num1,num2,num3,num4)
    elif choice =='2':
        subtraction(num1,num2,num3,num4)
    elif choice =='3':
        multiplication(num1,num2,num3,num4)
    elif choice =='3':
        division(num1,num2,num3,num4)

    else:
        print("Invalid Choice")
        
  #seperates multipe lines
        print("\n")
