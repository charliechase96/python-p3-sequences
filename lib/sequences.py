#!/usr/bin/env python3

def print_fibonacci(length):

    if length <= 0:
        # Return an empty list if the length is 0 or less
        print([])
        return
    elif length == 1:
        # Return a list with only the first number in the sequence if length is 1
        print([0])
        return
    # Initialize the first two terms
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the specified length
    for i in range(2, length):
        next_term = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_term)
    
    # Print the sequence
    print(fibonacci_sequence)