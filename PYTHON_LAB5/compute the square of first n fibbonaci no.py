
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


N = 10


fib_numbers = fibonacci(N)


squared_fib_numbers = list(map(lambda x: x ** 2, fib_numbers))


print("First", N, "Fibonacci numbers:", fib_numbers)
print("Squares of the first", N, "Fibonacci numbers:", squared_fib_numbers)
