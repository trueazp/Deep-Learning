# -*- coding: utf-8 -*-
"""Pertemuan01-PDL-H071191035.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KWVTDlDf84pqiBz39aAdXK8uq1gC5ncA

<H1><b>Pertemuan 1 - Python Basics</b></H1>

<H3>Nama : Akmal Zuhdy Prasetya</H3>
<H3>NIM  : H071191035</H3>

# 1. Fundamentals

Python is a programming language that has been under development for over 25 years.

**Python Reference**:

* https://docs.python.org/3.5/reference/

## 1.1 Statements

Python is an [imperative language](https://en.wikipedia.org/wiki/Imperative_programming) based on [statements](https://en.wikipedia.org/wiki/Statement_(computer_science&#41;). That is, programs in Python consists of lines composed of statements. A statement can be:

* a single expression
* an assignment
* a function call
* a function definition
* a statement; statement

### 1.1.1 Expressions

* Numbers
  * integers
  * floating-point
  * complex numbers
* strings
* boolean values
* lists and dicts

#### 1.1.1.1 Numbers
"""

1

2

-3

1
2

3.14

"""#### 1.1.1.2 Strings"""

'apple'

"apple"

"""Notice that the Out might not match exactly the In. In the above example, we used double-quotes but the representation of the string used single-quotes. Python will default to showing representations of values using single-quotes, if it can.

#### 1.1.1.3 Boolean Values
"""

True

False

"""#### 1.1.1.4 Lists and Dicts

Python has three very useful data structures built into the language:

* dictionaries (hash tables): {}
* lists: []
* tuples: (item, ...)

List is a mutable list of items. Tuple is a read-only data structure (immutable).
"""

[1, 2, 3]

(1, 2, 3)

1, 2, 3

{"apple": "a fruit", "banana": "an herb", "monkey": "a mammal"}

{"apple": "a fruit", "banana": "an herb", "monkey": "a mammal"}["apple"]

"""### 1.1.2 Function Calls

There are two ways to call functions in Python:

1. by pre-defined infix operator name
2. by function name, followed by parentheses

Infix operator name:
"""

1 + 2

abs(-1)

import operator

operator.add(1, 2)

"""#### 1.1.2.1 Print

Evaluating and display result as an Out, versus evaluating and printing result (side-effect).
"""

print(1)

"""### 1.1.3 Special Values"""

None

"""### 1.1.4 Defining Functions"""

def plus(a, b):
    return a + b

plus(3, 4)

def plus(a, b):
    a + b

plus(3, 4)

"""What happened? All functions return *something*, even if you don't specify it. If you don't specify a return value, then it will default to returning `None`."""

"a" + 1

"""<div style="background-color: lightgrey">
<h2>Sidebar 2-1: How to Read Python Error Messages</h2>

<p>
Python error messages 
<p>
<tt>TypeError: Can't convert 'int' object to str implicitly</tt>
</p>

<p>Above the error message is the "traceback" also called the "call stack". This is a representation of the sequence of procedure calls that lead to the error. If the procedure call originated from code from a file, the filename would be listed after the word "File" on each line. If the procedure call originated from a notebook cell, then the word "ipython-input-#-HEX".
</p>
</div>

## 1.2 Equality

### 1.2.1 ==
"""

1 == 1

"""### 1.2.2 is"""

[] is []

list() is list()

tuple() is tuple()

57663463467 is 57663463467

"""# 2. Advanced Topics

The Zen of Python:
"""

import this

"""## 2.1 Python's Growth

* http://web.archive.org/web/20031002184114/www.amk.ca/python/writing/warts.html
* 
* https://www.python.org/dev/peps/pep-3099/

## 2.2 Scope of variables

Is not always clear:
"""

y = 0
for x in range(10):
    y = x

x

[x for x in range(10, 20)]

x

"""## 2.3 Scope

Python follows the LEGB Rule (after https://www.amazon.com/dp/0596513984/):

* L, Local: Names assigned in any way within a function (def or lambda)), and not declared global in that function.
* E, Enclosing function locals: Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
* G, Global (module): Names assigned at the top-level of a module file, or declared global in a def within the file.
* B, Built-in (Python): Names preassigned in the built-in names module : open, range, SyntaxError,...
"""

x = 3
def foo():
    x=4
    def bar():
        print(x)  # Accesses x from foo's scope
    bar()  # Prints 4
    x=5
    bar()  # Prints 5

foo()

"""See [scope_resolution_legb_rule.ipynb](scope_resolution_legb_rule.ipynb) for some additional readings on scope.

## 2.4 Generators
"""

def function():
    for i in range(10):
        yield i

function()

for y in function():
    print(y)

"""## 2.5 Default arguments"""

def do_something(a, b, c):
    return (a, b, c)

do_something(1, 2, 3)

def do_something_else(a=1, b=2, c=3):
    return (a, b, c)

do_something_else()

def some_function(start=[]):
    start.append(1)
    return start

result = some_function()

result

result.append(2)

other_result = some_function()

other_result

"""## 3.2 List comprehension

"List comprehension" is the idea of writing some code inside of a list that will generate a list.

Consider the following:
"""

[x ** 2 for x in range(10)]

temp_list = []
for x in range(10):
    temp_list.append(x ** 2)
temp_list

"""But list comprehension is much more concise.

## 3.3 Plotting
"""

import matplotlib.pyplot as plt

"""Python has many, many libraries. We will use a few over the course of the semester.

To create a simple line plot, just give a list of y-values to the function plt.plot().
"""

plt.plot([5, 8, 2, 6, 1, 8, 2, 3, 4, 5, 6])

"""But you should never create a plot that doesn't have labels on the x and y axises, and should always have a title.

http://matplotlib.org/api/pyplot_api.html

Another commonly used library (especially with matplotlib is numpy). Often imported as:
"""

import numpy as np

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)

"""## 2.6 Closures

Are functions that capture some of the local bindings to variables.
"""

def return_a_closure():
    dict = {}
    def hidden(operator, value, other=None):
        if operator == "add":
            dict[value] = other
        else:
            return dict[value]
    return hidden

thing = return_a_closure()

thing("add", "apple", 42)

thing("get", "apple")

"""<H1>References</H1>

[1] https://en.wikipedia.org/wiki/History_of_Python
"""