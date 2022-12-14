import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")
        print("File opened.")
    except FileNotFoundError:
        print("That file doesn't exist.")
    except OSError:
        print("That's not a valid file name.")
    except:
        print("An unknown error occurred.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Unable to divide by zero")
        return None
    except TypeError:
        try:
            num1 = float(num1)
            num2 = float(num2)
            return num1 / num2
        except:
            print("You entered an invalid data type.")
    #return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = 0
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        return dist
    except TypeError:
        try:
            x1 = float(x1)
            x2 = float(x2)
            y1 = float(y1)
            y2 = float(y2)
        except ValueError:
            return ("Invalid input.")
            #return False
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    temp = str(temp)
    temp = temp.upper()
    test = temp[::-1]
    if(test == temp):
        return True
    else:
        return False
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = (input("Enter a number: "))
    num2 = (input("Enter another number: "))
    try:
        num1 = int(num1)
        num2 = int(num2)
        div = num1 / num2
        output = "Your numbers divided is: " + str(div) + "\n"
        print(output)
        return output
    except ValueError:
        try:
            num1 = float(num1)
            num2 = float(num2)
            div = num1 / num2
            output = "Your numbers divided is: " + str(div) + "\n"
            print(output)
            return output
        except ValueError:
            print("Invalid data type.")
            return "Invalid data type."
    except:
        print("Something went wrong, please try again.")
        return "Something went wrong, please try again."

## returns the squareroot of a particular number
def sq(num):

    try:
        x = math.sqrt(num)
        return math.sqrt(num)
    except ValueError:
        print("Cannot have a square root of a negative number")
    except TypeError:
        num = float(num)
        x = math.sqrt(num)
        return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if first.isalpha() and middle.isalpha() and last.isalpha():
        print("Hello!")
        print("Welcome to the program", first, middle, last)
        print("Glad to have you!")
    else:
        print("Your name should be all letters.")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    try:
        print("Your item at", index, "index is", numbers[index])
    except IndexError:
        print("The index argument is out of reach of the list.")
    except TypeError:
        print("The index argument must be an integer.")
