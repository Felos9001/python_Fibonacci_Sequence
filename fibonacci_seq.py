def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci_iterative(10)  # Prints the first 10 Fibonacci numbers
# Output: 0 1 1 2 3 5 8 13 21 34
