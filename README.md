# Recursive functions

Python supports recursive functions; functions that call themselves in order to loop. Recursion is an advanced practice in Python. Recursive functions are very useful for traversing unknown shapes and structures.

### A Recursive Example

```python
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1,2,3,4,5,6,7,8,9]))
# 45
```

This function takes a list of numbers and recursively calls itself to add the next item to a summation. The first condition `if not L` allows us to terminate the recursive function; when the list is empty we add 0 to our sum and terminate, as no more recursive calls are made. To better understand this, let's add a couple of print statements to our function.

```python
def mysum(L):
    print("first L", L)
    if not L:
    	print("not L", L)
        return 0
    else:
    	print("else L",  L, "L[0]", L[0], "L[1:]", L[1:] )
        return L[0] + mysum(L[1:])

print(mysum([1,2,3,4,5,6,7,8,9]))

```

```
first L [1, 2, 3, 4, 5, 6, 7, 8, 9]
else  L [1, 2, 3, 4, 5, 6, 7, 8, 9] L[0] 1 L[1:] [2, 3, 4, 5, 6, 7, 8, 9]
first L [2, 3, 4, 5, 6, 7, 8, 9]
else  L [2, 3, 4, 5, 6, 7, 8, 9] L[0] 2 L[1:] [3, 4, 5, 6, 7, 8, 9]
first L [3, 4, 5, 6, 7, 8, 9]
else  L [3, 4, 5, 6, 7, 8, 9] L[0] 3 L[1:] [4, 5, 6, 7, 8, 9]
first L [4, 5, 6, 7, 8, 9]
else  L [4, 5, 6, 7, 8, 9] L[0] 4 L[1:] [5, 6, 7, 8, 9]
first L [5, 6, 7, 8, 9]
else  L [5, 6, 7, 8, 9] L[0] 5 L[1:] [6, 7, 8, 9]
first L [6, 7, 8, 9]
else  L [6, 7, 8, 9] L[0] 6 L[1:] [7, 8, 9]
first L [7, 8, 9]
else  L [7, 8, 9] L[0] 7 L[1:] [8, 9]
first L [8, 9]
else  L [8, 9] L[0] 8 L[1:] [9]
first L [9]
else  L [9] L[0] 9 L[1:] []
first L []
not   L []
45
``` 

### Scope

Each new call to your function creates a new local scope. In other words, this creates a new namespace for the variables within that function call. This can be seen above as our `print(L)` statement continually shows `L` within the local context of that particular function call.

### Alternatives & Performance

```python
"""Recursive function"""

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

import time 
start_time = time.time() 

mysum([1,2,3,4,5,6,7,8,9])

print("--- %s seconds ---" % (time.time() - start_time)) 

# --- 1.1920928955078125e-05 seconds ---
```

```python
"""While Loop"""

def mysum(L):
    sum_1 = 0 
    while L:
        sum_1 += L[0]
        L = L[1:]
    return sum_1

import time 
start_time = time.time() 

mysum([1,2,3,4,5,6,7,8,9])

print("--- %s seconds ---" % (time.time() - start_time)) 

# --- 1.0013580322265625e-05 seconds ---
``` 
```python 
"""For Loop"""

def mysum(L):
    sum_1 = 0 
    for x in L:
        sum_1 += x

    return sum_1

import time
start_time = time.time() 

mysum([1,2,3,4,5,6,7,8,9])
# --- 5.9604644775390625e-06 seconds ---
```

## Exercise 1 - Factorial

Define a function that gets `n factorial` of a number.

Evaluate the performance for an iterative and a recursive function.

```python
"""Iterative function"""

...

``` 
```python
"""Recursive function"""

...
```
```python
"""driver code"""
print(factorial(0) == 1)
print(factorial(1) == 1)
print(factorial(10) == 3628800)
``` 

## Exercise 2 - Fibonacci

Define a function that gets `Fibonacci sequence` of a number.

Evaluate the performance for an iterative and a recursive function.

```python
"""Iterative function"""

...

``` 
```python
"""Recursive function"""

...
```
```python
"""driver code"""

print(fib_recur(0) == 0)
print(fib_recur(1) == 1)
print(fib_recur(2) == 1)
print(fib_recur(20) == 6765)
print(fib_recur(50) == 12586269025) 

``` 

> [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number)
