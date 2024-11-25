'''
Ashley Mapes
CS 2520 Lab 4

TASK 1: have user input 10 values then measure execution time of putting elements in list 

TASK 2: compare list creation time for different size lists; size = 50, 500, 5000, 50000

TASK 3: create a list of 500 random even integers between 1 and 100 in 5 different ways
'''
import time
import timeit
import random
import numpy as np

# Task 1
def task1():
    print("TASK 1")
    print()
    
    # function to ask user for input then append to list
    def create_list():
        list = []
        for i in range(10):
            user_input = input(f"Please enter integer value for element {i+1}: ")
            
    # calculate execution time with user input
    execution_time = timeit.timeit(create_list, number=1)    
    print(f"\nExecution time (including time for input): {execution_time} seconds")
    print()
    
    input_list = []
    for i in range(10):
        user_input = input(f"Please enter integer value for element {i+1}: ")

    # calculate time to create list
    start_time = time.time()
    list_created = input_list
    end_time = time.time()
    print()
    print(f"Execution time (excluding time for input): {end_time - start_time} seconds")
    print()

# Task 2
def task2():
    print("TASK 2:")
    print()
    
    # function to run tests of parameter size
    def diff_size_list(size):

        def loop_method(size):
            L1 = []
            for _ in range(size):
                L1.append(random.randint(1,100))

        def comprehension_method(size):
            L2 = [random.randint(1, 100) for _ in range(size)]

        # print execution times
        loop_execution = timeit.timeit(lambda: loop_method(size), number=1)
        comprehension_exeution = timeit.timeit(lambda: comprehension_method(size), number=1)
        print(f"Execution time to create list of size {size} with loop method: {loop_execution} seconds")
        print(f"Execution time to create list of size {size} with comprehension method: {comprehension_exeution} seconds")
        print()
        
    # run tests on different sizes
    for size in [50, 500, 5000, 50000]:
        diff_size_list(size)
    print()

# Task 3
def task3():
    print("TASK 3: creating list of 500 integers with random even numbers between 1-100")
    print()

    # Method 1: list comprehension
    def method1():
        even_numbers_list = [random.choice(range(2, 101, 2)) for _ in range(500)]


    # Method 2: using map() function
    def method2():
        even_numbers_list = list(map(lambda x: random.choice(range(2, 101, 2)), range(500)))

    # Method 3: using filter() function
    def method3():
        random_numbers = [random.randint(1, 100) for _ in range(1000)]  # Generate more than needed

        even_numbers = list(filter(lambda x: x % 2 == 0, random_numbers))

        while len(even_numbers) < 500:
            additional_numbers = [random.randint(1, 100) for _ in range(1000)]
            even_numbers.extend(filter(lambda x: x % 2 == 0, additional_numbers))

        even_numbers_list = even_numbers[:500]

    # Method 4: using regular for loop with append
    def method4():
        even_numbers_list = []
        for _ in range(500):
            even_numbers_list.append(random.choice(range(2, 101, 2)))

    # Method 5: using numpy
    def method5():
        even_numbers_list = np.random.choice(np.arange(2, 101, 2), size=500, replace=True).tolist()


    # print execution times
    print(f"Execution time for creating the list with the comprehension method: {timeit.timeit(method1, number=1)}")
    print(f"Execution time for creating the list with the map function: {timeit.timeit(method2, number=1)}")
    print(f"Execution time for creating the list with the filter function: {timeit.timeit(method3, number=1)}")
    print(f"Execution time for creating the list with regular for loop: {timeit.timeit(method4, number=1)}")
    print(f"Execution time for creating the list with numpy: {timeit.timeit(method5, number=1)}")

# main function to run tasks
def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()

'''
OUTPUT:

TASK 1

Please enter integer value for element 1: 1
Please enter integer value for element 2: 2
Please enter integer value for element 3: 3
Please enter integer value for element 4: 4
Please enter integer value for element 5: 5
Please enter integer value for element 6: 6
Please enter integer value for element 7: 7
Please enter integer value for element 8: 8
Please enter integer value for element 9: 9
Please enter integer value for element 10: 0

Execution time (including time for input): 4.066049600020051 seconds

Please enter integer value for element 1: 1
Please enter integer value for element 2: 2
Please enter integer value for element 3: 3
Please enter integer value for element 4: 4
Please enter integer value for element 5: 5
Please enter integer value for element 6: 6
Please enter integer value for element 7: 7
Please enter integer value for element 8: 8
Please enter integer value for element 9: 9
Please enter integer value for element 10: 0

Execution time (excluding time for input): 0.0 seconds

TASK 2:

Execution time to create list of size 50 with loop method: 4.360009916126728e-05 seconds
Execution time to create list of size 50 with comprehension method: 2.9399991035461426e-05 seconds

Execution time to create list of size 500 with loop method: 0.00028280005790293217 seconds
Execution time to create list of size 500 with comprehension method: 0.0002722002100199461 seconds

Execution time to create list of size 5000 with loop method: 0.005378799978643656 seconds
Execution time to create list of size 5000 with comprehension method: 0.005348700098693371 seconds

Execution time to create list of size 50000 with loop method: 0.03891220013611019 seconds
Execution time to create list of size 50000 with comprehension method: 0.03744200011715293 seconds


TASK 3: creating list of 500 integers with random even numbers between 1-100

Execution time for creating the list with the comprehension method: 0.0005299998447299004
Execution time for creating the list with the map function: 0.0003052998799830675
Execution time for creating the list with the filter function: 0.0025295999366790056
Execution time for creating the list with regular for loop: 0.000582600012421608
Execution time for creating the list with numpy: 0.0002747001126408577
'''