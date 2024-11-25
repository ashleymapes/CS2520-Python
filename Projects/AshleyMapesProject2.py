'''
Ashley Mapes
Project 2

Task 1: practiced making functions and created get_input(),
get_num_of_letters(txt), get_acronym(...), and task1() to run tests

Task 2: created is_prime(x) and prime_generator() to
produce a sequence of prime numbers

Task 3: main() function created that encloses task1()
and task2()
'''

# TASK 1

# get user input and output number of characters then return the original string
def get_input():
    userString = input("Enter a string: ")
    print(f"Your string: {userString}")
    print(f"Number of characters: {len(userString)}")
    return userString

# count number of letters in string
def get_num_of_letters(txt=""):
    count = 0
    for char in txt:
        if char.isalpha():
            count += 1
    return count

# create acronym for series for words
def get_acronym(*words):
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

# Task 1 Function
def task1():
    # 2 test runs for get_input and get_num_of_letters
    user_string = get_input()
    num_letters = get_num_of_letters(user_string)
    print(f"Number of letters in the input: {num_letters}")
    print()
    
    user_string = get_input()
    num_letters = get_num_of_letters(user_string)
    print(f"Number of letters in the input: {num_letters}")
    print()

    # 2 test runs for get_acronym
    acronym1 = get_acronym("Random", "Access", "Memory")
    print(f"Acronym for Random Access Memory is: {acronym1}")

    acronym2 = get_acronym("American", "Airlines")
    print(f"Acronym for American Airlines is: {acronym2}")
    print()

# TASK 2

# check if given number is prime 
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# prime number generator
def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Task 2 Function
def task2():
    prime_gen = prime_generator()

    # generate first 50 prime numbers
    prime_nums = []
    prime_gen = prime_generator()
    for i in range(50):
        prime_nums.append(next(prime_gen))
    # print list
    print("First 50 prime numbers: ")
    for i in range(0, len(prime_nums), 10):
        print(prime_nums[i:i+10])
    print()

    # skip 10 prime numbers
    for i in range(10):
        next(prime_gen)
    
    # generate prime numbers 61st to 70th
    next_prime = []
    for i in range(10):
        next_prime.append(next(prime_gen))
    # print list
    print(f"Primes from 61st to 70th:")
    for i in range(0, len(next_prime), 10):
        print(next_prime[i:i+10])
    
    # count primes between 70th prime and 5000
    count = 0
    current_prime = next(prime_gen)
    while current_prime < 5000:
        count += 1
        current_prime = next(prime_gen)
    print(f"Number of primes between 70th prime and 5000: {count}")

# main function to run the tasks
def main():
    task1()
    task2()

if __name__ == '__main__':
    main()
    
'''
Enter a string: hello world
Your string: hello world
Number of characters: 11
Number of letters in the input: 10

Enter a string: i like cookies
Your string: i like cookies
Number of characters: 14
Number of letters in the input: 12

Acronym for Random Access Memory is: RAM
Acronym for American Airlines is: AA

First 50 prime numbers:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
[31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
[73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
[127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
[179, 181, 191, 193, 197, 199, 211, 223, 227, 229]

Primes from 61st to 70th:
[283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
Number of primes between 70th prime and 5000: 599
'''
