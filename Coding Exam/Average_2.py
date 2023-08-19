#The index here is n, so we need to generate the sequence up until the nth fibonacci term

def fibonacci(n):
    sequence = [1, 1]
    
    if n == 1:
        return sequence
    else:
        #Since we already have 2 terms added, then we subtract n with 3
        n -= 3
        for i in range(n + 1):
            sequence.append(sequence[i] + sequence[i + 1])
        return sequence

        
n = int(input("Please input an integer: "))

print(fibonacci(n))