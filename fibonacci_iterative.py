import time 
def fib_recur(number: int):
    """Return fibonacci of a number"""   
    result=0
    sumando_1: int=0
    sumando_2: int=0
    
    for i in range(0,number+1):
        
        if i == 0:
            result=i
            sumando_1=i
            
        elif i == 1:
            result = i
            sumando_2 =i
            
        elif i > 1:
            
            result= sumando_1 + sumando_2
            sumando_1= sumando_2
            sumando_2= result
            
        
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