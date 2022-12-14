from functions import *
# this py file contains the pytest functions

# TESTS FOR OPENFILE
# tests for successful opening of file
def test_openFile(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "File opened.\n"
# tests for nonexistent file (should return an error and fail the test)
def test_openFile_nonexistentFile(capsys):
    openFile("nonexistent_file.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "File opened.\n"
# tests for invalid file name (should return an error and fail the test)
def test_openFile_notString(capsys):
    openFile(12345)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "File opened.\n"
# TESTS FOR NUMBERS

# tests for a correct division by numbers
def test_numbers():
    assert numbers(10, 2) == 5

#tests for a failed division by numbers
def test_numbers_fail():
    assert numbers(10, 2) == 6

#should throw a zero division error, returning None (undefined)
def test_numbers_zero():
    assert numbers(1,0) == None

# tests the function using an integer and a float, should return an integer
def test_numbers_1flt():
    assert numbers(5,5.0) == 1

# tests i the function using an integer and a numeric string
def test_numbers_str():
    assert numbers(5,"5") == 1

# TESTS FOR DIST
#testing dist, should pass and return a long decimal using only integers
def test_dist_1():
    assert dist(1,2,3,4) == 2.8284271247461903
#testing dist to ensure it can return a distance of zero
def test_dist_2():
    assert dist(4,2,4,2) == 0.0
#testing dist, should return a float with a decimal of zero
def test_dist_3():
    assert (dist(1, 4, 2, 4)) == 1
#testing dist to ensure it can handle a mix of floats and integers
def test_dist_4():
    assert (dist(1,2.0,3,4.0)) == 2.8284271247461903
#testing dist with only floats
def test_dist_5():
    assert (dist(1.0,2.0,3.0,4.0)) == 2.8284271247461903
#testing dist with a number stored as a string, this test should attempt conversion due to a typeError
def test_dist_6():
    assert (dist("1",2,3,4)) == 2.8284271247461903
#testing dist with an input including letters stored in a string
def test_dist_7():
    assert (dist("one",2,3,4)) == "Invalid input."

# TESTS FOR ISPALINDROME
def test_palin_1():
    assert (isPalindrome("racecar")) == True
#tests a palindrome with one capital letter, should fail without converting letters to the same case
def test_palin_2():
    assert(isPalindrome("Racecar")) == True
#tests a palindrome in all uppercase letters
def test_palin_3():
    assert(isPalindrome("RACECAR")) == True
#tests a multiword string that is a palindrome
def test_palin_4():
    assert(isPalindrome("racecar racecar")) == True
#tests an integer that is a palindrome, should fail as it is not iterable
def test_palin_5():
    assert(isPalindrome(616)) == True
#tests a float that is a palindrome, should fail as it is not iterable
def test_palin_6():
    assert (isPalindrome(616.616)) == True

# TESTS FOR DIVIDE

# testing divide using integers
def geninputs():
    inputs = ['6','3']
    for item in inputs:
        yield item
GEN = geninputs()
def test_divide(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    assert divide() == "Your numbers divided is: 2.0\n"


# runs the divide function with float values rather than ints
def geninputs_2():
    inputs = ['6.2','3.1']
    for item in inputs:
        yield item
GEN2 = geninputs_2()
def test_divide_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))
    assert divide() == "Your numbers divided is: 2.0\n"

# testing with strings composed of ASCII characters, intentionally fails
def geninputs_3():
    inputs = ['six','three']
    for item in inputs:
        yield item
GEN3 = geninputs_3()
def test_divide_3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN3))
    assert divide() == "Your numbers divided is: 2.0\n"

# TESTS FOR SQ

# testing for negative values, should fail
def test_sq_negative():
    assert sq(-1) == None

#testing for integer values, should pass
def test_sq():
    assert sq(4) == 2

#testing for float values, should pass
def test_sq_is_float():
    assert sq(4.0) == 2.0

#testing for string values, should pass
def test_sq_string():
    assert sq("4") == 2

# TESTS FOR GREETUSER
# tests for correct output
def test_greetUser(capsys):
    greetUser("John", "Robert", "Doe")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "Hello!\nWelcome to the program John Robert Doe\nGlad to have you!\n"
# this test should fail because last name is other characters
def test_greetUser_failure(capsys):
    greetUser("John", "Robert", "&%$#@")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "this test should fail"
# this test should fail because last name is all numbers
def test_greetUser_isLetters(capsys):
    greetUser("John", "Robert", "12345")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "Hello!\nWelcome to the program John Robert 12345\nGlad to have you!\n"


# TESTS FOR DISPLAYITEM

# tests for correct output
def test_displayItem(capsys):
    displayItem([0, 1, 2, 3], 3)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "Your item at 3 index is 3\n"
# should raise an index error, because tried to get an index that is out of reach of the list
def test_displayItem_indexErr():
    assert displayItem([0, 1, 2], 5) == 2
# should raise a type error, because the index variable must be an integer
def test_displayItem_typeErr():
    assert displayItem([0, 1, 2, 3], "three") == 3
