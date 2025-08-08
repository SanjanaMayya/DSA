n = int(input("Enter number of elements: "))

# Read elements into list
numbers = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    numbers.append(num)

# Read key to search
key = int(input("Enter element to search: "))

# Linear search
position = -1
for i in range(n):
    if numbers[i] == key:
        position = i
        break

# Display result
if position != -1:
    print(f"Element found at position {position}")
else:
    print("Element not found")
