AI-generated hello world:

print("Hello, World!")


def fibonacci_digit(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Example: Compute the 10th digit of the Fibonacci sequence
n = 10
result = fibonacci_digit(n)
print(f"The {n}th digit of the Fibonacci sequence is: {result}")
