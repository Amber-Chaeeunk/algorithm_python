def fibonacci(n):
    store = [0, 1]
    if n < len(store):
        return store[n]
    fib = fibonacci(n-1) + fibonacci(n-2)
    store.append(fib)
    return fib