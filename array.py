#1. Print All Elements of an Array


#Write a Python program to print all elements of an array.


arr = [10, 20, 30, 40, 50]

for i in arr:
    print(i)


#Write a Python program to find the sum of all elements in an array.


arr = [5, 10, 15, 20]

total = 0

for i in arr:
    total += i

print("Sum =", total)


#Write a Python program to find the largest element in an array.


arr = [25, 10, 45, 30, 18]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest Element =", largest)


#Write a Python program to find the smallest element in an array.


arr = [25, 10, 45, 30, 18]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest Element =", smallest)



#Write a Python program to count even and odd numbers in an array.


arr = [2, 5, 8, 11, 14, 17]

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers =", even)
print("Odd Numbers =", odd)


#Write a Python program to search for an element in an array.


arr = [10, 20, 30, 40, 50]

num = int(input("Enter element to search: "))

if num in arr:
    print("Element Found")
else:
    print("Element Not Found")


#Write a Python program to print an array in reverse order.


arr = [10, 20, 30, 40, 50]

print("Reversed Array:")

for i in arr[::-1]:
    print(i)




#Write a Python program to copy one array into another.


arr1 = [5, 10, 15, 20]

arr2 = arr1.copy()

print("Original Array:", arr1)
print("Copied Array:", arr2)




#Write a Python program to sort an array in ascending order.


arr = [40, 10, 50, 20, 30]

arr.sort()

print("Sorted Array:", arr)



#Write a Python program to calculate the average of array elements.

arr = [10, 20, 30, 40, 50]

total = 0

for i in arr:
    total += i

average = total / len(arr)

print("Average =", average)

#Write a Python program to find the second largest number in an array without using sort().

numbers = [10, 45, 20, 80, 60]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest Number:", largest)
print("Second Largest Number:", second_largest)


#Write a Python program to move all zeros to the end of an array while maintaining the order of other elements.
numbers = [10, 0, 20, 0, 30, 40, 0]

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print("Original Array:", numbers)
print("Updated Array:", result)

#Write a Python program to find duplicate elements in an array without using set().

numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

print("Duplicate Elements:", duplicates)









