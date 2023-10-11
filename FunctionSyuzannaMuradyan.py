# 1. Write a function to multiply all the numbers in a given list.

def mul_numbers(list1):
    num1 = 1
    for i in list1:
        num1 = num1 * i
    return num1


list1 = [2, 4, 5]
print(f"The original list is: {list1}")
print("The product of the list numbers is:")
print(mul_numbers(list1))


# 2. Write a function that takes a list and returns a new list with unique elements of the first list

def unique_elements(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


print("The unique elements are:")
print(unique_elements([2, 4, 5, 5, 5, 6, 7, 6]))



# 3. Write a function to print the even numbers from a given list.
3.1

def get_even_numbers(mylist):
    for i in mylist:
        if i % 2 == 0:
            print(i, end=" ")


print("The even numbers from a list are:")
mylist = [1, 7, 2, 4, 6, 3, 8, 9, 5]
get_even_numbers(mylist)

3.2
def get_even_numbers(mylist):
    mylist1 = []
    for i in mylist:
        if i % 2 == 0:
            mylist1.append(i)
    return mylist1

print("The even numbers from a list are:")
print(get_even_numbers([1, 7, 2, 4, 6, 3, 8, 9, 5]))



# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#       Sample String : 'The quick Brow Fox'
#       Expected Output :
#       No. of Upper case characters : 3
#       No. of Lower case Characters : 12

def calculate_letters(text1):
    upper = 0
    lower = 0
    for i in text1:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
    print(f"No. of Upper case characters : {upper}")
    print(f"No. of Lower case characters : {lower}")


text1 = "The quick Brow Fox"
calculate_letters(text1)





# 5. Write a Python function that takes a number as a parameter and check the number is prime or not





# 6. Write a Python  function that accepts a string and calculates the number of words which contain "g" letter.
def number_of_g(text1):
    count = text1.count("g")
    return count


text1 = "Beautiful girls are dancing in the garden."
print(number_of_g(text1))

