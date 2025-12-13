#hashtags are used to perform comments
#this tells the computer to ignore part of the program
#this helps others understand the code better

#this code will be used to print my name and a welcome message
name = "Alexis"
print("welcome " + name)

#in python print is used to tell the computer what to say
#the message printed will be surrounded by quotes
print("")

#a string is blocks of text
#they can be surrounded by single or double quotes
print("Alexis")
print('Alexis')
#these will both yield the same result

#variables store a value
message = "Hello"
#in this case the variable is message and it stores the value Hello

#too common errors are SyntaxError and NameError
#SyntaxError is an error with the program
#NameError is when python interpreter sees a word it does not recognize
#TypeError is when an operation is applied to an object of an innappropriate type

#python stores number data as integers (int)- whole numbers and floating-point number (float)- decimels
#python can perform arithmetic operations: addition, subtraction, multiplication, division

#python can perform exponentation

#2 to the 10th power
print(2 ** 10)
1024

#python can perform modulo
#prints 4 because 29/5 is 5 with remainder 4
print(29 % 5)
4

#the + operation can add two strings
#this process is called concatenation
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + "" + question_text
print(full_text)
#prints Hey there! How are you doing?"

#to concatenate a number with strings requires making the number into a string
birthday_string = "I am "
age = 10
birthday_string_2 = " years old"
full_birthday_string = birthday_string_1 + str(age) + birthday_string_2
print(full_birthday_string)

#python has shorthand for updating variables
#plus-equals operator
number_of_miles_hiked = 12
number_of_miles_hiked += 2
print(number_of_miles_hiked)
#prints 14

#plus-equals operator can be used for string concatenation
hike_caption = "What an amazing time to walk through nature"
hike_caption += "#nofilter"
hike_caption += "#blessed"

#when printing multi-line strings use (''') or (""")
leaves_of_grass) = """leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.

print(leaves_of_grass)

#bugs in python are denoted with ^

#in lists [] are used. You can append (add), remove (subtract), add two lists using +, or denote an item using negative. Lists are numbered starting at 0
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = (shopping_list[-1])
index5_element = (shopping_list[5])
print(last_element + index5_element)
#-1 will print cereal, 4 will print juice

#2D lists
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
#"Noelle"	heights[0][0]
#61	heights[0][1]
#"Ali"	heights[1][0]
#70	heights[1][1]
#"Sam"	heights[2][0]
#67	heights[2][1]

