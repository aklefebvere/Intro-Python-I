# 3. Write a program to determine if a number, given on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).


# code for testing

# test = [True] * 31
# test[0] = False
# test[1] = False

# prime_nums = []

# print(test)


# primecheck = 2

# while primecheck < 31:
#     if test[primecheck] == True:
#         for i in range(primecheck * 2, 31, primecheck):
#             test[i] = False

#     primecheck += 1

# print(test)

# for i, v in enumerate(test):
#     if v == True:
#         prime_nums.append(i)


# print(prime_nums)

# --------------------------------------------

import sys
# Grab user's selected num throguh sys.argv
user_num = int(sys.argv[1])
# Create a list of True's with the index range of
# the user's selected number
# ex: pick 30, list indexes: 0-30
prime_range = [True] * (user_num + 1)
# index 0 is false because 0 is not prime
prime_range[0] = False
# index 1 is false because 1 is not prime
prime_range[1] = False
# empty list to hold prime nums
prime_nums = []
# starting prime num
primecheck = 2

# If the current prime num is less than 
# the user's selected number
while primecheck < user_num:
    # if the selected index is True
    if prime_range[primecheck] == True:
        # for loop to make all non prime numbers False
        # primecheck * 2 because you want to start on
        # the index after the selected number
        # n + 1 because range second num is exclusive
        # steps is primecheck
        for i in range(primecheck * 2, user_num + 1, primecheck):
            prime_range[i] = False

    # increment primecheck by 1
    primecheck += 1

# for loop that goes through each value of the list
for i, v in enumerate(prime_range):
    # if the current value is True..
    if v == True:
        # append the index to the prime_nums list
        prime_nums.append(i)

# if the user selected num is in the prime_num list
# the user selected num is a prime number
if user_num in prime_nums:
    print(f"{user_num} is a prime number!")
# if not, the user selected num is not a prime num
else:
    print(f"{user_num} is not a prime number!")


# Function implementation

def IsPrime(n):
    # Create a list of True's with the index range of
    # the user's selected number
    # ex: pick 30, list indexes: 0-30
    prime_range = [True] * (n + 1)
    # index 0 is false because 0 is not prime
    prime_range[0] = False
    # index 1 is false because 1 is not prime
    prime_range[1] = False
    # empty list to hold prime nums
    prime_nums = []
    # starting prime num
    primecheck = 2

    # If the current prime num is less than 
    # the user's selected number
    while primecheck < n:
        # if the selected index is True
        if prime_range[primecheck] == True:
            # for loop to make all non prime numbers False
            # primecheck * 2 because you want to start on
            # the index after the selected number
            # n + 1 because range second num is inclusive
            # steps is primecheck
            for i in range(primecheck * 2, n + 1, primecheck):
                prime_range[i] = False

        # increment primecheck by 1
        primecheck += 1

    # for loop that goes through each value of the list
    for i, v in enumerate(prime_range):
        # if the current value is True..
        if v == True:
            # append the index to the prime_nums list
            prime_nums.append(i)

    # if the user selected num is in the prime_num list
    # the user selected num is a prime number
    if n in prime_nums:
        print(f"{n} is a prime number!")
    # if not, the user selected num is not a prime num
    else:
        print(f"{n} is not a prime number!")


# IsPrime(30)
