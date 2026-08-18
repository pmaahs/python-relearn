def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)
    
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n<=1:
        return n
    else:
        first = 1
        second = 0
        for _ in range(n-1):
            next = first + second
            second = first
            first = next
        return next

def fibonacci_memoized(n):
    pass

print(factorial(5))
print(fibonacci(5))
print(fibonacci_iterative(5))