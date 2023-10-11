# 1.Write a program to print all three-digit numbers․

# 1.1
print("All three-digit numbers are:")
for i in range(99, 999):
    print(i+1)

# 1.2
print("All three-digit numbers are:")
num = 100
while num >= 100 and num <= 999:
    print(num)
    num += 1


# 2.Write a program to print all three-digit odds.

print("All three-digit odds are:")
for i in range(100, 1000):
    if i % 2 != 0:
        print(i)

#
# # 3. Write a program to print all five-digit couples on a line.

for i in range(10000, 100000):
    if i % 2 == 0:
        print(i, end=" ")


# 4. Print all numbers up to 1000 that are divisible by 5 and 7.

print("All numbers up to 1000 that are divisible by 5 and 7 are:")
for i in range(1000):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


# # 5․ Take a list and print every third elements from that list.
list1 = [1, 5, 7, 3, 5, 1, 5, 8, 3, 4, ]
i = 1
length = len(list1)
print(length)
while i < length:
    print(list1[i])




list1 = [1, 5, 4, 89, 2, 3, 45, 2, 34, 84, 32, 45, 84]
i = 2
print(f"The original list is: {list1}")
print("Every third elements from this list are:")
while i < len(list1):
    print(list1[i])
    i += 3



# 6.Write a program to display only lowercase elements from the list which contains 15-20 elements.

list1 = ["Red", "black", "white", "Blue", "Green", "gray", "Yellow", "pink", "Purple", "Winter", "spring", "Summer",
         "Snow", "Wind", "flower", "tree", "Rose"]
print("The lowercase elements from this list are:")
for i in list1:
    if i == i.lower():
        print(i)


















