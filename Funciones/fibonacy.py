def fibonacci(n):
    # Caso base: los dos primeros números
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Los primeros 10 números de Fibonacci
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")
# fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, ...