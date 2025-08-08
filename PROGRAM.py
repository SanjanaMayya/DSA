#Predefined data
lst = sorted([15,7,22,3,10,18])
key = 10

#Binary search
low, high, steps = 0, len(lst)-1,0
while low <= high:
    steps += 1
    mid = (low+high) // 2
    if lst[mid] == key:
        print(f"Found {key} at position {mid}")
        break
    elif lst[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("No found")

print("Sorted list:", lst)
print("Steps taken:", steps)