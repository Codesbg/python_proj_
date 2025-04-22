#loops in python
#while condition:
# Code to execute while the condition is True
'''
n=10
while n==10 :
# print("hello"*10 )
    n=n+1;
#  for variable in iterable:
# Code to execute in each iteration

#for i in range(10):
# print("hello")

# second loop in Python

fruits = [ "mango","banana" ,"lemon", "melon" , "grapes"]
#for fruits in fruits :
#print(fruits)
'''
#**Data Structures**

'''### **Lists in Python (In Detail)**
A **list** is one of Python's most versatile and commonly
 used data structures. It represents a collection 
 of items (called elements) that can be ordered, 
 changed (mutable), and allow duplicates. 
 Lists are defined using square brackets `[]`
  and can contain elements of any data type.
  # Empty list
empty_list = []

# List with integers
numbers = [1, 2, 3, 4, 5]

# List with strings
fruits = ["apple", "banana", "cherry"]

# Mixed-type list
mixed = [1, "hello", 3.14, True]

# Nested list
nested_list = [[1, 2, 3], [4, 5, 6]]


list1=[1,2,3,4,5,6]
print(list1)
nestedlist = [[1,2,3,4,50],[34556,456,453,764,986],[2,4,5,6,7],[6,7,8,9,0]]
print(nestedlist)
mixedlist=[1,"this list can contain all types of data type",3.78,True,5,7,8,False,"hello"]
print(mixedlist)

# Accessing Elements

#indexing

print(list1[5])

#slicing
print(nestedlist[3],[6]) #list 3 ka 6th element
print(mixedlist[2:4])

#### **Modifying Lists**

mixedlist[0]=45
print(mixedlist)
print(mixedlist.pop(3))
mixedlist.append("hey")
mixedlist.insert(3,"hey")
print(mixedlist)


#program for guessing a number if it is correct display you won
number = 67;
guess_count =0;
guess_limit = 5;
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess == number:
        print("You won!")
        break

else:
    print("try agin wrong answer" , number)
    
#loop chalo jab atk command quit na aa jaye
command = ""
while  command.lower() != "quit" :

  command = input (">")
if command == " start":
    print(" start the car")
    
elif command=="step":
    print("step on the car")
    
elif command=="stop":
    print("stop the car")
else:
    print("we dont undeestand !")

# print coordinate till 0 to 2 from 1 to 5
for i in range (2):
    for j in range (6):
        print(f"({i},{j})")
   
numbers = [6,2,6,2,2,2]

for i in range (6):
    print("#"* int(numbers[i]))
    i=i+1


# dupes in list

list_one = [2,5,6,7,8,2,1]
unique_list=[]
for list_one in list_one:
    if list_one not in unique_list:
        unique_list.append(list_one)
        print(unique_list)
        
#toples me () ye use karte hai
# we cannot change the tuple we just check the index and count
# dictionaries

dictionary name = {
key : value ,
key2 : val
}

# key values must be unique


student = {
    " name ": "xyz",
    " age ":19,
    "section" :  "D"
}
print(student)
student["fathers name"]="hjk" # to add more key values
print(student)
student.update({"dob":2004}) # to update whole dictionary
print(student)

# digit to word translator
inputed = input("digit_word :")
digit_to_word = {
  "1":"one",
  "2" :"two",
  "3" : "three",
  "4" :"four",
  "5" :"five",
  "6" :"six",
  "7" :"seven",
  "8" :"eight",
  "9" :"nine",
  "0":"zero"
}
# to input char from the dictionary
# it join the input strings in one line
output = ""
# Loop through each character in the input
for ch in inputed :
    # Convert the digit to word, default to "!" if not found in the dictionary
 output+= digit_to_word.get(ch," ") + " " #  Each character in the input string is looked up in the dictionary using the `get()` method:

print(output
      
# print emoji
# with dictionary

# user enter their message

message = input("enter your message :")
words = message.split( ' ') # this split the string into seperate words
emojis = {
    ":)":"😊",
    ":(": "😒",
}
output = ""
for word in words :
 output += emojis.get(word,word) + " "
 print(output)
'''
#import the file and use in other
# code reusability

from NEW import FindMax
numbers = [23,56,78,90]
max = FindMax(numbers)
print(max)
