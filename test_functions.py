import pytest
import math
#this py file contains the pytest functions and the uncorrected original functions


## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points

# tests for a correct division by numbers
def test_numbers():
    assert numbers(10, 2) == 5

#tests for a failed division by numbers
def test_numbers_fail():
    assert numbers(10, 2) == 6

#should throw a zero division error
def test_numbers_zero():
    assert numbers(10,0) == 0

# tests the function using an integer and a float, should return an integer
def test_numbers_1flt():
    assert numbers(5,5.0) == 1.0

def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)
    return dist

#testing dist, should pass and return a long decimal using only integers
def test_dist_1():
    assert dist(1,2,3,4) == 2.8284271247461903
#testing dist to ensure it can return a distance of zero
def test_dist_2():
    assert dist(4,2,4,2) == 0.0
#testing dist, should return a float with a decimal of zero
def test_dist_3():
    assert (dist(1, 4, 2, 4)) == 1.0
#testing dist to ensure it can handle a mix of floats and integers
def test_dist_4():
    assert (dist(1.,2.0,3.0,4.)) == 2.8284271247461903
#testing dist with only floats
def test_dist_4():
    assert (dist(1.,2.0,3.0,4.)) == 2.8284271247461903
#testing dist with a number stored as a string, this test should fail
def test_dist_5():
    assert (dist("1",2,3,4)) == 2.8284271247461903
## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])

# comment
