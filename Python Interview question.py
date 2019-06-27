# Python Interview question
https://github.com/iamrahuljha/Python-Interview-question
 
open this link and download file 



c,d=29,3289
print(type(c)) # < class 'tuple' >

#..What is pep 8?
Ans: PEP stands for Python Enhancement Proposal.
It is a set of rules that specify how to format Python code for maximum readability.

#.What is __init__?
Ans: __init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

# Lambda Function
as annonymous function is known as lambda function. 
a= lambda x,y : x+y 
print(a(7,86))
 # output-- 93 

# what does [::-1] do?
it revesre the sequence.

# how can we randomaize the function?
its randomly the function 
from random import shuffle
a=['rahul','jha',235,'love']
print(shuffle(a))

# how do you write comments in python 
comment in python start with # Character. 
# this is a comment . 

#how will you capitalize the first string ?
a='rahul'
a.capitalize()
print(a)
# -- outuput is  Rahul

# how will you convert string to lowercase and uppercase. 
a='rahul'
print(a.lower())  # rahul 
print(a.upper())  # RAHUL


# what does len() do?
it is used to determine the length of a string 
a='rahul'
print(len(a))  # output is 5 

# what are pyhton libraries ?
python libraries is a collection of python packages . 
Numpy, Pnadas , Matplotlib, are mostly used libaray., 

# what is split() do?
--- its remove the space from string 
a='Rahul Jha' 
print(a.split()) # output is 'RahulJha' 

# What is monkey patching in Python?
 In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

#  Discuss Django architecture.
Ans: Django MVT Pattern:

Django Architecture - Python Interview Questions - EdurekaFigure:

The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the user.

# Which of the following statements create a dictionary? (Multiple Correct Answers Possible)

a) d = {}
b) d = {“john”:40, “peter”:45}
c) d = {40:”john”, 45:”peter”}
d) d = (40:”john”, 45:”50”)
# answer is  b, c & d. 

Dictionaries are created by specifying keys and values.

# Which one of these is floor division?
a) /
b) //
c) %
d) None of the mentioned 
 # answer is //(floor division) 

# what is the maximum possible length of an identifier?
--- identifier can be any of the length. 

#  Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?
a) Error
b) None
c) 25
d) 2
 # answer is 25

# What is PYTHONPATH?
Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.


# What are Python decorators?

A Python decorator is a specific change that we make in Python syntax to alter functions easily.

8) What is the difference between list and tuple?

The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.

# How you can convert a number to a string?

In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().

# Local variables: If a variable is assigned a new value anywhere within the function's body, it's assumed to be local.

Global variables: Those variables that are only referenced inside a function are implicitly global.

#  What is a negative index, and how is it used in Python?
A negative index is used in Python to index a list, string, or any other container class in reverse order (from the end). Thus, [-1] refers to the last element, [-2] refers to the second-to-last element, and so on.

Here are two examples:

list = [2, 5, 4, 7, 5, 6, 9]
print (list[-1]) # outpuit is 9 

# what is Pandas?
Pandas  is a Python open-source library that provides high-performance and flexible data structures and data analysis tools that make working with relational or labeled data both easy and intuitive.

# write down 5 IDE name ?
 Pycharm,  Jupyter Notebook, sPYDER , Python IDE , Atom 	

# What is Python?
Python is a high-level, interpreted, interactive, and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently, whereas other languages use punctuation, and it has fewer syntactical constructions than other languages.


# What is the purpose of PYTHONPATH environment variable?
PYTHONPATH has a role similar to PATH. This variable tells Python Interpreter where to locate the module files imported into a program. It should include Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by Python Installer.

# What is the purpose of PYTHONSTARTUP, PYTHONCASEOK, and PYTHONHOME environment variables?
PYTHONSTARTUP: It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix, and it contains commands that load utilities or modify PYTHONPATH.
PYTHONCASEOK: It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable with any value to activate it.
PYTHONHOME: It is an alternative module search path. It is usually embedded in PYTHONSTARTUP or PYTHONPATH directories to make switching of module libraries easy.

# What are the supported data types in Python?
Python has five standard data types:

Numbers
Strings
Lists
Tuples
Dictionaries

# differnce between list,tuple,set, dictionaries 

# How are range and xrange different from one another?
Functions in Python, range() and xrange() are used to iterate a fixed number of times in a for loop. Functionality-wise, both of these functions are the same. Difference comes when talking about Python version support for these functions and their return values.

# Define pickling and unpickling in Python.
Pickling is the process of converting Python objects such as lists, dicts, etc. into a character stream. This is done using a module named pickle, hence the name pickling.

The process of retrieving the original Python object from the stored string representation, which is the reverse of the pickling process, is called unpickling.

# Is indentation optional in Python?
Indentation in Python is compulsory and is part of its syntax. 


#Which of the following is an invalid statement?
a) xyz = 1,000,000
b) x y z = 1000 2000 3000
c) x,y,z = 1000, 2000, 3000
d) x_y_z = 1,000,000
Answer: b

# Write a command to open the file c:\hello.txt for writing.
f= open(“hello.txt”, “wt”)

#What would be the output if I run the following code block?
list1 = [2, 33, 222, 14, 25]

print(list1[-2])

(A)          14

(B)          33

(C)          25

(D)          Error

Ans: 14

# What do you understand by Tkinter?
Tkinter is an inbuilt Python module that is used to create GUI applications.

# What is the difference between append() and extend() methods?
Both append() and extend() methods are methods used for lists. These methods are used to add elements at the end of a list.

# Q-3. What Is The Right Way To Transform A Python String Into A List?
Ans. In Python, strings are just like lists. And it is easy to convert a string into the list. Simply by passing the string as an argument to the list would result in a string-to-list conversion.

list("I am learning Python.")
Program Output.
Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.8.2] on linux

=> ['I', ' ', 'a', 'm', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'P', 'y', 't', 'h', 'o', 'n', '.']

# What Is The Result Of The Below Python Code?
keyword = 'aeioubcdfg'
print keyword [:3] + keyword [3:]
Ans. The above code will produce the following result.

<'aeioubcdfg'>

#  What Are The Core Default Modules Available In Python? List Down A Few Of Them.
Ans. Following are a few of the default modules available in Python.

email – Help to parse, handle, and generate email messages.
string – Contains functions to process standard Python strings.
sqlite3 – Provides methods to work with the SQLite database.
XML – Enables XML support.
logging – Adds support for log classes and methods.
traceback – Allows to extract and print stack trace details.


# How Will You Print The Sum Of Numbers Starting From 1 To 100 (Inclusive Of Both)?
print(sum(range(1,101)))  # output is 5050

#  What is a Variable in Python?

# How do you represent binary and hexadecimal numbers?

If  ‘0b’ is leading then the Python interprets it as a binary number.

‘0x’ as hexadecimal.

# What is a module in Python?

A module is a .py file in Python in which variables, functions, and classes can be defined. It can also have a runnable code.


# How do you merge one dictionary with the other?

Python provides an update() method which can be used to merge one dictionary on another.

Example:

>>> a = {'a':1}

>>> b = {'b':2}

>>> a.update(b)

>>> a

{'a': 1, 'b': 2}



# Write a generator expression to get the numbers that are divisible by 2?

a=[267,28,198,1,2,5,6]
print([i for i in a if i%2==0])     # output is -- 28,198,2,6


# print the table of 5. 
a=5 
for i in range(1,11):
    print('mul of',a,a*i)

# print the calendar of June 2019. 

year=2019
month=6
import calendar
print(calendar.month(year,month))

# print the calendar of year 2019. 

year=2019
import calendar
print(calendar.calendar(year))

# Python Program to Print the Fibonacci sequence

# Python Program to Display Fibonacci Sequence Using Recursion
