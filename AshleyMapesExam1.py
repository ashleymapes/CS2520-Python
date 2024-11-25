'''
Ashley Mapes
Exam 1
'''

# this function will count the number of non-characters in a string
def task1(input):
    count = 0
    for char in input:
        if not char.isalpha():
            count += 1
    return count

# this function performs math on a number and returns the output
def task2( n ):
    if n < 0:
        return n
    elif n == 0:
        return 0
    else:
        result = 0
        for i in range(1, n + 1):
            # if even number, subtract square
            if i % 2 == 0:
                result -= (i**2)
            # else odd, add square
            else:
                result +=(i**2)
        return result

# this function performs test cases on previous functions
def main():
    print("Testing task 1...")
    test_strings = ["Hello! How are you?", "", "123 let's go!"]
    for string in test_strings:
        print(f'Number of non-letter characters in "{string}": {task1(string)}')

    print()
    print("Testing task 2...")
    test_numbers = [10, 25, -1]
    for num in test_numbers:
        print(f"The result of n = {num}: {task2(num)}")
    
    
if __name__ == '__main__':
    main()

    
'''
RESULTS:

Testing task 1...
Number of non-letter characters in "Hello! How are you?": 5
Number of non-letter characters in "": 0
Number of non-letter characters in "123 let's go!": 7

Testing task 2...
The result of n = 10: -55
The result of n = 25: 325
The result of n = -1: -1
'''