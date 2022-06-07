import time 
def fib_recur(number: int):
    """Return fibonacci of a number"""   
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        result= fib_recur(number-1) + fib_recur(number-2)
        return result

if __name__== '__main__':

    """driver code"""
    start_time = time.time()
    print(fib_recur(0) == 0)
    print(fib_recur(1) == 1)
    print(fib_recur(2) == 1)
    print(fib_recur(20) == 6765)
    print(fib_recur(50) == 12586269025)

    
    print("--- %s seconds ---" % format((time.time() - start_time),".4f"))