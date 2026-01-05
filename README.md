# 📌 Types of Arguments in Python Functions

This repository explains the **different types of arguments** that can be passed to a function in Python, with **simple examples**.  
It is useful for **students, M.C.A./B.tech./B.C.A./B.Sc. exams, and interview preparation**.

---

## 🧠 What are Function Arguments?

Arguments are the **values passed to a function** when it is called.  
They help functions work with **dynamic input**.

---

## ✅ Types of Arguments in Python

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
