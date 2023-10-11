# 1*. Write a Python program that accepts a word from the user and reverse it.

word1 = input("Enter a word for reversing it: ")
reverse = word1[::-1]
print(reverse)



# 2. Write a Python program to count that user inputed number is even or odd.

num1 = int(input("Please enter some number: "))
result = num1 % 2
if result > 0:
    print(f"{num1} is odd number.")
else:
    print(f"{num1} is even number.")



# 3. Write a Python program to find is inputed number in 100 to 400 (both included). Hint(dont google task description)


num1 = int(input("Please enter some number: "))
if num1 >= 100 and num1 <= 400:
    print(f"{num1} is in 100 to 400(both included)")
else:
    print("False")




# 4. Write a Python program that get 2 numbers from user and return Biggest, Median, Sum, Multiply, Divide and Subtract

num1 = int(input("please enter the first number: "))
num2 = int(input("Please enter the second number: "))
if num1 > num2:
    print(f"The Biggest of these two numbers is: {num1}")
elif num2 > num1:
    print(f"The biggest of these two number is: {num2}")
result1 = (num1 + num2) / 2
print(f"The Median of these two numbers is: {result1}")
result2 = num1 + num2
print(f"The Addition result of these two numbers is: {result2}")
result3 = num1 * num2
print(f"The Multiplication result of these two numbers is: {result3}")
result4 = num1 - num2
result5 = num1 / num2
if num1 > num2:
    print(f"The Subtraction result  of these numbers is: {result4}", f"The Division result is: {result5}", sep="\n")
elif num2 > num1:
    print (f"The Subtraction result of these numbers is: {num2 - num1}")
    print(f"The Division result is: {num2 / num1}")






# indexing


name = "guguremg"
print(name[0], name[2], name[7])
print(name[-1], name[-6], name[-8])


name = "Syuzanna Muradyan Edvardi"
print(name[:7], name[9:17], name[17:])

word1 = input("Please enter a word: ")
reverse = word1[::-1]
if len(word1) >= 20:
    print(reverse)
else:
    print("This word is small")

text = "hello world"
print(text[6])

