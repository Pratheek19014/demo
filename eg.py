# Function to print Fibonacci series
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_term)
    return fib_series[:n]

# Number of terms you want in the Fibonacci series
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci(num_terms))
