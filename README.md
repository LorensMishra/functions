# 🐍 Python Functions – Complete Practice & Interview Guide

This repository contains the **Python function concepts, different types of arguments and coding problems** that can be passed to a function in Python, with **simple examples**.  
It is useful for **students, M.C.A./B.tech./B.C.A./B.Sc. exams, and interview preparation**.

It includes:
- Function basics
- Types of arguments
- Common function-based coding questions
- Logic-based implementations (without built-ins where required)
---
## 📌 What is a Function?
A **function** is a reusable block of code that performs a specific task.
Functions improve:
- Code reusability
- Readability
- Modularity
- Debugging

---
## 🧱 Function Syntax

```python
def function_name(parameters):
    statements
    return value
```
---
## 🧠 What are Function Arguments?

Arguments are the **values passed to a function** when it is called.  
They help functions work with **dynamic input**.

---
# 📌 Types of Arguments in Python Functions
---

### 1️⃣ Positional Arguments
Arguments are passed in the **same order** as parameters.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```
### 2️⃣ Keyword Arguments
Arguments are passed using **parameter** names.

```python
def add(a, b):
    print(a + b)

add(a=10, b=20)
```

### 3️⃣ Default Arguments
Parameters have default values.

```python
def fun(a,b=10):
    print("value of a",a,"value of b",b,"Sum of a+b is:",a+b)

fun(1)
fun(1,12)
```

### 4️⃣ Variable-Length Arguments
🔹 *args (Non-keyword variable length)
Used when the number of arguments is unknown.

```python
def total(*nums):
    print(sum(nums))

total(1, 2, 3, 4)
```
🔹 **kwargs (Keyword variable length)
Used to pass key–value pairs.

```python
def details(**info):
    print(info)

details(name="Lorens", age=22)
```
### 5️⃣ Positional-Only Arguments (Python 3.8+)
🔹Arguments must be positional.
```python
def func(a, b, /):
    print(a, b)

func(10, 20)
```

### 6️⃣ Keyword-Only Arguments
🔹Arguments must be passed using keywords.
```python
def func(*, a, b):
    print(a, b)

func(a=10, b=20)
```
---
## 🐍 Python Functions – Practice Questions
---

| No. | Question |
|----|---------|
| 1 | What is a function in Python? |
| 2 | Why are functions used in Python? |
| 3 | What is the syntax of a function? |
| 4 | What is the difference between a function and a method? |
| 5 | What is the purpose of the `return` statement? |
| 6 | Can a function return multiple values? |
| 7 | What is the difference between arguments and parameters? |
| 8 | What are positional arguments? |
| 9 | What are keyword arguments? |
| 10 | What are default arguments? |
| 11 | What is `*args`? |
| 12 | What is `**kwargs`? |
| 13 | What are positional-only arguments? |
| 14 | What are keyword-only arguments? |
| 15 | What is variable scope in Python functions? |
| 16 | What is the difference between local and global variables? |
| 17 | What is the `global` keyword? |
| 18 | What happens if a function does not return a value? |
| 19 | What is a recursive function? |
| 20 | What is a lambda function? |
| 21 | Write a function to add two numbers. |
| 22 | Write a function to find the maximum of two numbers. |
| 23 | Write a function to check whether a number is even or odd. |
| 24 | Write a function to calculate factorial of a number. |
| 25 | Write a function to reverse a string. |
| 26 | Write a function to count vowels in a string. |
| 27 | Write a function to find the length of a string without using `len()`. |
| 28 | Write a function to count the number of words in a string. |
| 29 | Write a function to check whether a number is prime. |
| 30 | Write a function to find the sum of digits of a number. |
| 31 | Write a function to generate Fibonacci series. |
| 32 | Write a function to check whether a string is palindrome. |
| 33 | Write a function to find the largest element in a list. |
| 34 | Write a function to remove duplicate elements from a list. |
| 35 | Write a function using default arguments. |
| 36 | Write a function using `*args`. |
| 37 | Write a function using `**kwargs`. |
| 38 | Write a function that returns multiple values. |
| 39 | Write a recursive function to calculate power of a number. |
| 40 | Write a function to count uppercase and lowercase letters in a string. |

---

## 🎯 Usage
- Practice coding
- Prepare for exams
- Interview revision
- Assignment reference

---

## 👨‍💻 Author
**Lorens Mishra**  
Python & Full Stack Developer
