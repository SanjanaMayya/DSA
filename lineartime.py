"""import time

# Take three inputs from the user
n1 = int(input("Enter first value of n: "))
n2 = int(input("Enter second value of n: "))
n3 = int(input("Enter third value of n: "))

for n in [n1, n2, n3]:
    start = time.time()

    total = 0
    for i in range(n):
        total += i  # simple operation

    end = time.time()

    print(f"Time taken for n = {n} is {end - start:.6f} seconds")"""

import time

def linear_time(n):
    print(f"\nO(n) for n = {n}")
    start = time.time()
    for i in range(n):
        pass # Simulate some work
    end = time.time()
    print(f"Time Taken: {end - start:.6f} seconds")

linear_time(10000)
linear_time(20000)
linear_time(40000)