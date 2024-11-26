'''
Ashley Mapes
CS 2520 Lab 5

1) define a class Question that creates a question bank that contains at least 10 question objects
2) a test is a list of 5 questions, randomly drawn from the question bank
3) Define a student class. Each student object contains a name, an ID number, and a test score. Before the student
taking a test, the score is None or 0 (or whatever you designate.)
4) Now let a student take the test. After taking the test, you will display the score and update the student object
with the new test score.
'''

import randomg

# define a class Question that takes in question, choices, and correct answer
class Question:
    # create constructor
    def __init__(self, question_text, choices, correct_answer):
        self.question_text = question_text
        self.choices = choices
        self.correct_answer = correct_answer

    # display question in proper format
    def display_question(self):
        print(self.question_text)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
    
    # get correct answer
    def get_answer(self):
        return self.correct_answer

    # get array of choices
    def get_choices(self):
        return self.choices

    # get the question
    def get_question(self):
        return self.question_text
    
    # check if answer is correct
    def check_answer(self, answer):
        return answer == self.correct_answer



# define the Test class
class Test:
    # create question bank
    question_bank = [
    Question("Where is Cal Poly Pomona located?", 
             ["Texas", "California", "Nevada", "Washington"], 
             "California"),
    Question("On your student records system, what does CSU stand for?", 
             ["California State Universities", "Colorado State Universities", "Color Sparkling Unicorn", "Canadian Swan Upping"], 
             "California State Universities"),
    Question("What is the mascot of Cal Poly Pomona?", 
             ["Bronco", "Tiger", "Eagle", "Bear"], 
             "Bronco"),
    Question("What is the name of Ashley's dog?", 
             ["Finny", "Pixie", "Diego", "Cali"], 
             "Finny"),
    Question("Where was Ashley born?", 
             ["Yangxi", "Guiyang", "Shanghai", "Xi'an"], 
             "Guiyang"),
    Question("What is Ashley's favorite color?", 
             ["blue", "red", "black", "pink"], 
             "blue"),
    Question("Who is Ashley's best friend?", 
             ["Sayumi", "Joelle", "Yichen", "Courtney"], 
             "Joelle"),
    Question("What's Ashley's favorite number?", 
             ["9", "7", "21", "13"], 
             "13"),
    Question("What is Courtney's favorite color?", 
             ["pink", "red", "green", "yellow"], 
             "yellow"),
    Question("What is the best type of animal?", 
             ["cat", "dog", "horse", "snake"], 
             "dog"),
    ]
    
    # make constructor
    def __init__(self):
        self.questions = random.sample(self.question_bank, 5)

    # answer questions to a given student
    def administer(self, student):
        
        print(f"\nStarting test for {student.name} (ID: {student.student_id})")
        
        # create array to hold wrong answers to print later
        wrong_answers = []
        score = 0
        
        # iterate through questions
        for i, question in enumerate(self.questions, start=1):
            print(f"\nProblem {i}:")
            question.display_question()
            
            # input validation
            while True:
                answer = input("Your answer: ")
                if answer not in question.get_choices():
                    print("Invalid choice. Please choose a valid option.")
                else:
                    break
            # increase score if correct
            if question.check_answer(answer):
                score += 1
            # add wrong answer to array
            else:
                wrong_answers.append((i, question, answer))
                
        print(f"\nTest completed! Score: {score}/{len(self.questions)}")
        # update student score
        student.update_score(score)
        
        # if there are wrong answers, print them
        if wrong_answers:
            print("\nIncorrect answers:\n")
            for i, question, answer in wrong_answers:
                print(f"Problem {i}: {question.get_question()}\nYour answer: {answer}\nCorrect answer: {question.get_answer()}\n")
                
        print("END OF TEST")
                

# define the Student class which takes in a name and id and sets test score to None initially
class Student:
    # create constructor
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.test_score = None

    # update student test score
    def update_score(self, score):
        self.test_score = score
    
    # print student info
    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - Test Score: {self.test_score}"

def main():
    # create a student and print info
    name = "Pickle Rick"
    studentID = 666666
    student_rick = Student(name, studentID)
    print(f"Example of student: {student_rick}")
    
    # test .update_score method
    print(f"Testing update score...")
    student_rick.update_score(10)
    print(f"New information: {student_rick}\n")
    
    # get student info from user and create student
    student_name = input("Enter the student's name: ")
    student_id = input("Enter the student's ID: ")
    student = Student(student_name, student_id)
    
    print()    
    print(f"Student info: {student}")

    # administer test
    test = Test()
    test.administer(student)

    print()
    print(f"\nFinal Score for {student.name} (ID: {student.student_id}): {student.test_score}")
    
    print()
    print(f"Updated student info: {student}")

# Example usage
if __name__ == "__main__":
    main()

'''
TEST 1:

Example of student: Pickle Rick (ID: 666666) - Test Score: None
Testing update score...
New information: Pickle Rick (ID: 666666) - Test Score: 10

Enter the student's name: Finny
Enter the student's ID: 1234

Student info: Finny (ID: 1234) - Test Score: None

Starting test for Finny (ID: 1234)

Problem 1:
What is the mascot of Cal Poly Pomona?
1. Bronco
2. Tiger
3. Eagle
4. Bear
Your answer: Bronco

Problem 2:
Where is Cal Poly Pomona located?
1. Texas
2. California
3. Nevada
4. Washington
Your answer: California

Problem 3:
What is the name of Ashley's dog?
1. Finny
2. Pixie
3. Diego
4. Cali
Your answer: Finny

Problem 4:
What's Ashley's favorite number?
1. 9
2. 7
3. 21
4. 13
Your answer: 7

Problem 5:
Who is Ashley's best friend?
1. Sayumi
2. Joelle
3. Yichen
4. Courtney
Your answer: testing input validation
Invalid choice. Please choose a valid option.
Your answer: Joelle

Test completed! Score: 4/5

Incorrect answers:

Problem 4: What's Ashley's favorite number?
Your answer: 7
Correct answer: 13

END OF TEST


Final Score for Finny (ID: 1234): 4

Updated student info: Finny (ID: 1234) - Test Score: 4

TEST 2:

Example of student: Pickle Rick (ID: 666666) - Test Score: None
Testing update score...
New information: Pickle Rick (ID: 666666) - Test Score: 10

Enter the student's name: Mickey Mouse
Enter the student's ID: 101010

Student info: Mickey Mouse (ID: 101010) - Test Score: None

Starting test for Mickey Mouse (ID: 101010)

Problem 1:
What's Ashley's favorite number?
1. 9
2. 7
3. 21
4. 13
Your answer: 13

Problem 2:
What is Ashley's favorite color?
1. blue
2. red
3. black
4. pink
Your answer: black

Problem 3:
What is the best type of animal?
1. cat
2. dog
3. horse
4. snake
Your answer: horse

Problem 4:
Where is Cal Poly Pomona located?
1. Texas
2. California
3. Nevada
4. Washington
Your answer: California

Problem 5:
Who is Ashley's best friend?
1. Sayumi
2. Joelle
3. Yichen
4. Courtney
Your answer: Courtney

Test completed! Score: 2/5

Incorrect answers:

Problem 2: What is Ashley's favorite color?
Your answer: black
Correct answer: blue

Problem 3: What is the best type of animal?
Your answer: horse
Correct answer: dog

Problem 5: Who is Ashley's best friend?
Your answer: Courtney
Correct answer: Joelle

END OF TEST


Final Score for Mickey Mouse (ID: 101010): 2

Updated student info: Mickey Mouse (ID: 101010) - Test Score: 2
'''