def fibonacci(x):
    if x <= 0:
        return []
    elif x == 1:
        return [0]
    
    fibonacci_sequence = [0, 1]
    for _ in range(2, x):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:x]

y = fibonacci(5)
print(y)
