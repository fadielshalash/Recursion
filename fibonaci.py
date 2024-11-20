def Fibonacci_Recursive(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return Fibonacci_Recursive(n - 1) + Fibonacci_Recursive(n - 2)
    
print("Enter Your Number")
n = int(input("Please enter the number you want to do Fibonacci:"))

print(f"Result is {Fibonacci_Recursive(n)}")


