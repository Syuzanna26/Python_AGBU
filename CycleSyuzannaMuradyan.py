# 1. Write a program to construct the following pattern.
#       *
#       * *
#       * * *
#       * * * *
#       * * * * *
#       * * * *
#       * * *
#       * *
#       *

num1 = 1
num2 = 5





# 2. Write a program to create the multiplication table (from 1 to 10) of a number.
      Input a number: 6
      6 x 1 = 6
      6 x 2 = 12
      6 x 3 = 18
      6 x 4 = 24
      6 x 5 = 30
      6 x 6 = 36
      6 x 7 = 42
      6 x 8 = 48
      6 x 9 = 54
      6 x 10 = 60

num1 = 6
num2 = 1
while num2 <= 10:
    print(f"6 * {num2} = {num1 * num2}")
    num2 += 1


# 3. Write a program to print alphabet pattern 'O'
#    Expected Output:
#          *
#        *   *
#        *   *
#        *   *
#        *   *
#        *   *
#          *



# 4. Calculate the sum of all numbers from 1 to a given number from user
num1 = 1
num2 = int(input("Please enter a number here: "))
while num1 < num2:
    print(f"The sum of all numbers from 1 to {num2} will be: {sum(range(num1, num2+1))}")
    break



# 5. Write a program to check whether a specified list is sorted or not

list1 = [1, 8, 6]
print(f"The original list is: {list1}")
list1.sort()
print(f"The sorted version of the list is: {list1}")
if list1 == list1.sort():
    print("true")
else:
    print("false")








# 1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;



# 2*. Print the following pattern
#     5 4 3 2 1
#     4 3 2 1
#     3 2 1
#     2 1
#     1

# 3. Display numbers from -10 to -1 using for loop

# num1 = -10
# while num1 <= -1:
#     print(num1)
#     num1 += 1




#   4. Calculate the cube of all numbers from 1 to a given number from user
# #
# num1 = 1
# num2 = int(input("Please enter here a number: "))
# while num1 <= num2:
#     print(f"The cube of all numbers from 1 to your given will be: {num1**3}")
#     num1 += 1



# 5. Find the factorial of a given number.
# (The factorial of a number is the product of all the integers from 1 to that number.)

num1 = 1
num2 = int(input("Please enter some number here: "))
while num1 < num2:
    print(sum(num1 * num2))
    num1 += 1





