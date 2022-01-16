def fibonacci(n):
    store = [0, 1]
    i = 2
    while True:
        if i-1  == n:
            return store[n]
        store.append(store[i-1] + store[i-2])
        i += 1

print(fibonacci(5))