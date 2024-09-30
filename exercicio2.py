def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci(num):
    sequence = fibonacci_sequence(num)
    if num in sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."


num = 33 
print(is_fibonacci(num))