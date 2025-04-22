from sys import get_coroutine_origin_tracking_depth, exception

from dataclasses import replace

from http.cookiejar import uppercase_escaped_char

from calendar import firstweekday

from operator import truediv
import math
'''
# print("hello")
# line by line program execution hota hai ispe
# and har program me from top se execution statrt hota hai
#" ", ' ' form string
#  here sab operators are same as other + , - , * , / and so on
#print("="*10) # it print 10 times = , this is called expression
# variables
price = 34
price = 40

#print ('price :',price)

# op will be 40
# if you nreinitialize it it will again chnage the vlue and old one go to garbage val
# here also int , float , boolean are there
It_happen = True # write t and f capital
It_wont_happen = False

#print ( 'It_wont_happen :', It_wont_happen)

#print('It_happen',It_happen)
cgpa = 9.5;

#print('cgpa :',cgpa)

# how to take input you use input()

#statement = input('enter the price')

#print ('price :' + statement)

#question1 = input("what is your name ?")

#print("person name is ",question1)

#question2 = input("what is your favourite colour ?")

#print( question1,"favourite colour is ",question2)


# conversion of data type

#age = input("enter your DOB")
#current = input("enter the current year")
#calculation = int(current)-int(age)
#print("your age is :",calculation)

# string in python

#''' ''' triple courts for multiple line
course='''
'''
hey!
can you please enetr your details on this form
as ther are necessary to enrollmenet you in this program

#print(course)
#indexing in python string

string = " helo i am john and i am the manager of this production house"
#print(string[3]) # single char
#print (string [5:8]) #slice
# if we take chars in negative manner then it start slice from last of the string
#print(string[2:-4])

#formatted string
#string concatenation
first = 'shitij'
last = 'bharti goswami'
message = first +" "+ last + ' is an artist'
#print(message)
# in formated srting pattern it is followed by f
msg = f'{first} {last} is an artist'
#print(msg)

# here is many characters on the string to find their lenghth and many operation there are many function

#print(len(last))
#print(first.upper())
#print(first.lower())
#print(first.find('j'))
# to replace we use this function seperated by coma
#print(last.replace('i','u'))


#arithmatic operator in python

x=10
y=2.7
z=90
k=-3.67
add = x+k+z+y
print(add)
sub=x-y-z-k
print(sub)
print(round(-3.67))
print(abs(k)) # it always return posditive number

#import math
print(math.ceil(4.89))
print(math.floor(4.89))

#condition on Python
#its_hotday = True
#if  its_hotday:
#   print("enjoy icecream")
#else :
#  print("enjoy hot chocolate")

priceofhouse = 1000000000
credit = 0.1*priceofhouse
credit2 = 0.2*priceofhouse
creditscore=  True;
#if creditscore==False :
   # print("they need to put 10% down payment :" , credit)

#else :
  #  print(" they need to put 20% down payment :" ,credit2 )

  #CODE FOR AN APPLICANT INCOM AND GOOD CREDIT SCORE THEN GAVE LOAN

income = input("enter the income anual");
print(int(income))
credi_score = 0.1* int(income);

if income==100000000 and credi_score ==1000000 :
    print("LOAN APPROVED")
else :
    print("NO LOAN APPROVED")

# function in python
#def function_name(parameter_list):

def sum ( a,b):
    return a+b

print(sum(4,5))

 
 # EXEPTION ERROR !!
 try:
    # Code that may raise an exception
    risky_operation()
except SpecificException as e:
    # Code to handle the SpecificException
    print(f"An error occurred: {e}")
else:
    # Code that runs if no exception was raised
    print("No exceptions occurred!")
finally:
    # Code that always runs (optional)
    print("This block runs whether an exception occurred or not.")

 

try :
     age = int(input("enter your age :"))
     print(age)
     income = int ( input("enter your income :"))
     print(income)
     risk = income/age
     print(risk)

except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
 print("invalid age datatype !")

# Class in python

class Person :
    def exceptions(self):
         try:
             name = input("enter your name :")

         except ValueError:
             print(" name cannot be integer type !")

         try:
             age = int (input("enter your age :"))

         except ZeroDivisionError:
             print("age cannot be zero")
         except ValueError:
             print("inavlid age datatype !")

         try :
            salary = int (input("enter your salary :"))

         except ValueError:
              print("inavlid salary datatype !")


person1 = Person()
person1.exceptions()

# inheritance
class Animal :
    def properties ( self):
        print("animals can walk and run")

class Cat(Animal) :
    def characters (seif):
        print("cat eat mouse")

class Cow(Animal):
    def cando (self):
        print("eat grass")

obj=Animal()

# module

def FindMax(numbers):
    max = numbers[0]
    for number in numbers :
        if number > max :
           max=number
    return max

'''


import calendar

calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.weekheader(2))
















