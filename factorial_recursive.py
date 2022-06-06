import time 
def factorial(number: int):
    """Return factorial of a number"""
    if number == 0:
        return 1
    else:
        result = number * factorial(number-1)
        return result

if __name__== '__main__':

    """driver code"""
    start_time = time.time()
    print(factorial(0) == 1)
    print(factorial(1) == 1)
    print(factorial(100) == 3628800)

    
    print("--- %s seconds ---" % format((time.time() - start_time),".2f"))