'''
Ashley Mapes
Project 3
CS 2520
Task 1: reads a file and outputs information regarding words found in article
Task 2: takes in a list of names and scores then puts then together and implements other functions
Task 3: main function to fun task1() and task2()
'''

import string
import statistics


# Task 1: Word Frequency Counts
def task1():
    # ask for file path from user
    fileName = input("Please enter file path: ")
    file = open(fileName)
    total_words = []
    
    # read file line by line
    for line in file :
        # normalize word and remove punctuation
        words = line.translate(str.maketrans('', '', string.punctuation + string.digits)).lower().split()
        total_words.extend(words)
    file.close()
    
    # create set using total_words to get unique words in file
    unique_words = set(total_words)
    
    # print out word and unique word counts
    print()
    print(f"Total word count:  {len(total_words)}")
    print(f"Distinct words: {len(unique_words)}")
    print()
    
    # create dictionary to store word frequency counts
    word_count = {}
    for word in total_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    

    print(f"Word frequency dictionary sample: {dict(list(word_count.items())[:5])}")
    print()

    remove_words = {"for", "and", "nor", "but", "or", "yet", "so", "a", "an", "to", "in", "at"}
    filtered_words = [word for word in unique_words if word not in remove_words]
    filtered_words.sort()

    # print first 100 from sorted list of filtered words
    print("First 100 unique words:")
    for i in range(0, min(100, len(filtered_words)), 20):
        print(" ".join(filtered_words[i:i+20]))
    print()

    # remove words from  word_count dictionary
    for word in remove_words:
        word_count.pop(word, None)

    # sort dictionary in acsending order by value
    sorted_dictionary = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    top_fifty = list(sorted_dictionary.items())[:50]
    
    # print out top 50 words by frequency
    print("Top 50 words by frequency:")
    for i in range(0, len(top_fifty), 10):
        # Create a slice of 10 items
        line_items = top_fifty[i:i + 10]
        # Format and print the line
        print(' '.join(f"{key}: {value}" for key, value in line_items))
    print()

# Task 2: Data Structures as Parameters and Return Values
def setup(names, scores):
    list_tuples = list(zip(names, scores))
    list_dictionary = dict(list_tuples)
    return list_tuples, list_dictionary

def score_update(score_dict, name, score):
    # update student's score
    if name in score_dict:
        score_dict[name] = score
        return "Done"
    else:
        return f"Student '{name}' not found."

def get_stat(score_dict):
    # calulate average and standard deviation
    scores = list(score_dict.values())
    average = statistics.mean(scores)
    std_dev = statistics.stdev(scores)

    # record student with highest score
    highest_student = max(score_dict, key=score_dict.get)
    highest_student_score = score_dict[highest_student]

    return average, std_dev, (highest_student_score, highest_student)

def task2():
    # create data for testing
    names = ["Andy", "Ben", "Cathy", "Dave", "Edward", "Fanny", "George", "Hana", "Jess", "Karen", "Nancy", "Pedro"]
    scores = [88, 92, 85, 76, 85, 96, 77, 82, 90, 72, 98, 82]
    
    # test setup function
    student_info_tuples, student_info_dictionary = setup(names, scores)
    print("Name and score tuples:", student_info_tuples)
    print("Name and score dictionary:", student_info_dictionary)
    print()
    
    # test socre_update function
    update_result = score_update(student_info_dictionary, "Andy", 90)
    print("Result of updating Andy's score:", update_result)
    update_result = score_update(student_info_dictionary, "Ashley", 100)
    print("Result of updating Ashley's score:", update_result)
    print()
    
    # test get_stat function
    average, std_dev, highest = get_stat(student_info_dictionary)
    print(f"Class Average: {average:.2f}, Standard Deviation: {std_dev:.2f}")
    print(f"{highest[1]} had the highest score of  {highest[0]}")
    print()
    
    # more data for testing
    other_names = ["Liam", "Emma", "Noah", "Olivia", "Aiden", "Sophia", "Jackson", "Isabella", "Lucas", "Mia", "Ethan", "Amelia", "Mason", "Harper", "Elijah", "Charlotte", "James", "Ava", "Oliver", "Evelyn"]
    other_scores = [80, 90, 55, 95, 63, 23, 56, 95, 96, 40, 59, 61, 74, 75, 65, 68, 93, 95, 100, 99]
    
    # test setup function
    student_info_tuples, student_info_dictionary = setup(other_names, other_scores)
    print("Name and score tuples:", student_info_tuples)
    print("Name and score dictionary:", student_info_dictionary)
    print()
    
    # test score_update function
    update_result = score_update(student_info_dictionary, "Emma", 90)
    print("Result of updating Andy's score:", update_result)
    update_result = score_update(student_info_dictionary, "Ashley", 100)
    print("Result of updating Ashley's score:", update_result)
    print()
    
    # test get_stat function
    average, std_dev, highest = get_stat(student_info_dictionary)
    print(f"Class Average: {average:.2f}, Standard Deviation: {std_dev:.2f}")
    print(f"{highest[1]} had the highest score of  {highest[0]}")
    print()

# main function for tasks
def main():
    print("Task 1 Results:")
    task1()
    print("\nTask 2 Results:")
    task2()

# run main function
if __name__ == "__main__":
    main()

'''
SAMPLE:

Task 1 Results:
Please enter file path: article.txt

Total word count:  5081
Distinct words: 1200

Word frequency dictionary sample: {'music': 2, 'to': 120, 'hear': 2, 'why': 5, 'hearst': 1}

First 100 unique words:
abide absence absent abundance abuse accessary account acknowledge acquainted active actor addition adverse advised advocate afresh after again against age
ah air alack alchemy alive all allege allow almost alone alter although am amiss among anger annoy anon another antique        
any apparel appear appearance appetite approve are argument arise art as aspect assured astronomy attend audit aught away ay babe
back banquet bar bare barren barrenly base be bear beard bearer bearing beast beauteous beauty because bed before behind behold
being believe beloved benefit beside best bestow better betwixt beweep bier birth black blame blamed blessed blest blind blood bloody

Top 50 words by frequency:
the: 147 my: 128 of: 114 i: 107 that: 98 thou: 88 thy: 81 with: 73 thee: 59 love: 58
not: 48 me: 47 when: 45 all: 42 is: 40 as: 40 by: 39 which: 37 this: 36 be: 34
you: 34 from: 33 then: 32 your: 30 do: 29 self: 28 his: 28 on: 28 mine: 27 it: 26
more: 25 art: 23 shall: 23 are: 23 one: 22 time: 21 if: 20 sweet: 20 can: 20 their: 20
heart: 19 thine: 18 no: 17 than: 17 they: 16 eye: 16 make: 16 beauty: 16 him: 16 how: 15


Task 2 Results:
Name and score tuples: [('Andy', 88), ('Ben', 92), ('Cathy', 85), ('Dave', 76), ('Edward', 85), ('Fanny', 96), ('George', 77), ('Hana', 82), ('Jess', 90), ('Karen', 72), ('Nancy', 98), ('Pedro', 82)]
Name and score dictionary: {'Andy': 88, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 85.42, Standard Deviation: 7.74
Nancy had the highest score of  98

Name and score tuples: [('Liam', 80), ('Emma', 90), ('Noah', 55), ('Olivia', 95), ('Aiden', 63), ('Sophia', 23), ('Jackson', 56), ('Isabella', 95), ('Lucas', 96), ('Mia', 40), ('Ethan', 59), ('Amelia', 61), ('Mason', 74), ('Harper', 75), ('Elijah', 65), ('Charlotte', 68), ('James', 93), ('Ava', 95), ('Oliver', 100), ('Evelyn', 99)]
Name and score dictionary: {'Liam': 80, 'Emma': 90, 'Noah': 55, 'Olivia': 95, 'Aiden': 63, 'Sophia': 23, 'Jackson': 56, 'Isabella': 95, 'Lucas': 96, 'Mia': 40, 'Ethan': 59, 'Amelia': 61, 'Mason': 74, 'Harper': 75, 'Elijah': 65, 'Charlotte': 68, 'James': 93, 'Ava': 95, 'Oliver': 100, 'Evelyn': 99}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 74.10, Standard Deviation: 21.02
Oliver had the highest score of  100

ANOTHER SAMPE:
Task 1 Results:
Please enter file path: article.txt

Total word count:  5081
Distinct words: 1200

Word frequency dictionary sample: {'music': 2, 'to': 120, 'hear': 2, 'why': 5, 'hearst': 1}

First 100 unique words:
abide absence absent abundance abuse accessary account acknowledge acquainted active actor addition adverse advised advocate afresh after again against age
ah air alack alchemy alive all allege allow almost alone alter although am amiss among anger annoy anon another antique
any apparel appear appearance appetite approve are argument arise art as aspect assured astronomy attend audit aught away ay babe
back banquet bar bare barren barrenly base be bear beard bearer bearing beast beauteous beauty because bed before behind behold
being believe beloved benefit beside best bestow better betwixt beweep bier birth black blame blamed blessed blest blind blood bloody

Top 50 words by frequency:
the: 147 my: 128 of: 114 i: 107 that: 98 thou: 88 thy: 81 with: 73 thee: 59 love: 58
not: 48 me: 47 when: 45 all: 42 is: 40 as: 40 by: 39 which: 37 this: 36 be: 34
you: 34 from: 33 then: 32 your: 30 do: 29 self: 28 his: 28 on: 28 mine: 27 it: 26
more: 25 art: 23 shall: 23 are: 23 one: 22 time: 21 if: 20 sweet: 20 can: 20 their: 20
heart: 19 thine: 18 no: 17 than: 17 they: 16 eye: 16 make: 16 beauty: 16 him: 16 how: 15


Task 2 Results:
Name and score tuples: [('Andy', 88), ('Ben', 92), ('Cathy', 85), ('Dave', 76), ('Edward', 85), ('Fanny', 96), ('George', 77), ('Hana', 82), ('Jess', 90), ('Karen', 72), ('Nancy', 98), ('Pedro', 82)]
Name and score dictionary: {'Andy': 88, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 85.42, Standard Deviation: 8.08
Nancy had the highest score of  98

Name and score tuples: [('Liam', 80), ('Emma', 90), ('Noah', 55), ('Olivia', 95), ('Aiden', 63), ('Sophia', 23), ('Jackson', 56), ('Isabella', 95), ('Lucas', 96), ('Mia', 40), ('Ethan', 59), ('Amelia', 61), ('Mason', 74), ('Harper', 75), ('Elijah', 65), ('Charlotte', 68), ('James', 93), ('Ava', 95), ('Oliver', 100), ('Evelyn', 99)]
Name and score dictionary: {'Liam': 80, 'Emma': 90, 'Noah': 55, 'Olivia': 95, 'Aiden': 63, 'Sophia': 23, 'Jackson': 56, 'Isabella': 95, 'Lucas': 96, 'Mia': 40, 'Ethan': 59, 'Amelia': 61, 'Mason': 74, 'Harper': 75, 'Elijah': 65, 'Charlotte': 68, 'James': 93, 'Ava': 95, 'Oliver': 100, 'Evelyn': 99}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 74.10, Standard Deviation: 21.56
Oliver had the highest score of  100

Task 1 Results:
Please enter file path: article.txt

Total word count:  2670
Distinct words: 902

Word frequency dictionary sample: {'that': 52, 'she': 19, 'is': 19, 'living': 2, 'were': 9}

First 100 unique words:
abide above abroad absence acceptance accident accomplished acture adulterate advance advantage advice affectedly affection afflicted afraid again against age ah
aim airy all aloof altar am amber amend among amorous amorously amplify anon answer any apace appear appetite applied aptly
aptness are arms art as assay assigned assuage atwain audience audit aught authorized away awhile ay bare bat battle be
beaded bear beauteous beautiful beauty been beguiling begun behold behoof being belong beside besiege best bestow betray between bidding bide
big black blasting bleeding blend blessing blood bloodless blush blusterer boast bond bondage bone bore bosom both bough bounty braided

Top 50 words by frequency:
of: 82 the: 79 that: 52 his: 48 her: 31 my: 30 by: 29 i: 28 all: 27 not: 26
did: 26 their: 25 me: 23 he: 23 with: 21 your: 20 what: 20 she: 19 is: 19 this: 17
o: 17 as: 17 it: 16 from: 16 which: 15 was: 15 be: 14 him: 14 you: 13 have: 13
upon: 12 they: 11 them: 11 thou: 10 are: 10 would: 10 were: 9 mine: 9 where: 9 one: 9
many: 9 whose: 9 love: 9 some: 8 may: 8 had: 8 on: 8 when: 8 how: 7 made: 7


Task 2 Results:
Name and score tuples: [('Andy', 88), ('Ben', 92), ('Cathy', 85), ('Dave', 76), ('Edward', 85), ('Fanny', 96), ('George', 77), ('Hana', 82), ('Jess', 90), ('Karen', 72), ('Nancy', 98), ('Pedro', 82)]
Name and score dictionary: {'Andy': 88, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 85.42, Standard Deviation: 7.74
Nancy had the highest score of  98

Name and score tuples: [('Liam', 80), ('Emma', 90), ('Noah', 55), ('Olivia', 95), ('Aiden', 63), ('Sophia', 23), ('Jackson', 56), ('Isabella', 95), ('Lucas', 96), ('Mia', 40), ('Ethan', 59), ('Amelia', 61), ('Mason', 74), ('Harper', 75), ('Elijah', 65), ('Charlotte', 68), ('James', 93), ('Ava', 95), ('Oliver', 100), ('Evelyn', 99)]
Name and score dictionary: {'Liam': 80, 'Emma': 90, 'Noah': 55, 'Olivia': 95, 'Aiden': 63, 'Sophia': 23, 'Jackson': 56, 'Isabella': 95, 'Lucas': 96, 'Mia': 40, 'Ethan': 59, 'Amelia': 61, 'Mason': 74, 'Harper': 75, 'Elijah': 65, 'Charlotte': 68, 'James': 93, 'Ava': 95, 'Oliver': 100, 'Evelyn': 99}

Result of updating Andy's score: Done
Result of updating Ashley's score: Student 'Ashley' not found.

Class Average: 74.10, Standard Deviation: 21.56
Oliver had the highest score of  100
'''