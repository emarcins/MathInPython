data = [2, 3, 1, 70, 11, 10, 29, 35, 49, 39, 89, 69, 85, 12]

#Linear Searching Algorithm
def linearSearch(data, item):
    print(data)
    
    for i in range(len(data)):
        if data[i] == item:
            return i
    return -1 #index not found

number = 69
score = linearSearch(data, number)

if score != -1:
    print(f"The number {number} is on {score} index.")
else:
    print(f"The number {number} was not found.")
    
print("-------------------------------------")


#Binary Searching Algorithm
def binarySearch(data, target):
    data.sort()
    print(data)
    
    left, right = 0, len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

number_2 = 11
score_2 = binarySearch(data, number_2)

if score_2 != -1:
    print(f"The number {number_2} is on {score_2} index.")
else:
    print(f"The number {number_2} was not found.")
        
print("-------------------------------------")


data_two = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#Interpolation Searching Algorithm
def interpolationSearch(data, target):
    print(data_two)
    
    low = 0
    high = len(data) - 1

    while low <= high and target >= data[low] and target <= data[high]:
        if low == high:
            if data[low] == target:
                return low
            return -1

        # Interpolation Formula
        pos = low + ((high - low) * (target - data[low])) // (data[high] - data[low])

        if data[pos] == target:
            return pos
        if data[pos] < target:
            low = pos + 1 
        else:
            high = pos - 1

    return -1

number_3 = 70
score_3 = interpolationSearch(data_two, number_3)

if score_3 != -1:
    print(f"The number {number_3} is on {score_3} index.")
else:
    print(f"The number {number_3} was not found.")
        
print("-------------------------------------")


#Jump Searching Algorithm
import math

def jumpSearch(data, target):
    data.sort()
    print(data)
    
    n = len(data)
    step = int(math.sqrt(n))  # value of jump
    prev = 0

    # range where can find target
    while data[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # linear search in the found range
    for i in range(prev, min(step, n)):
        if data[i] == target:
            return i
    return -1

number_4 = 29
score_4 = jumpSearch(data, number_4)

if score_4 != -1:
    print(f"The number {number_4} is on {score_4} index.")
else:
    print(f"The number {number_4} was not found.")
        
print("-------------------------------------")


#Exponential Searching Algorithm
def binarySearch_two(data, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1 

def exponentialSearch(data, target):
    print(data_two)
    if data[0] == target:
        return 0
    
    index = 1
    while index < len(data) and data[index] <= target:
        index *= 2
        
    return binarySearch_two(data, index // 2, min(index, len(data) -1 ), target)
        
number_5 = 90
score_5 = exponentialSearch(data_two, number_5)

if score_5 != -1:
    print(f"Element {number_5} is on {score_5} index.")
else:
    print(f"Element {number_5} was not found.")
    
print("-------------------------------------")

