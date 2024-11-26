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

import random

# define a class Question that takes in question, choices, and correct answer
class Question:
    def __init__(self, question_text, choices, correct_answer):
        self.question_text = question_text
        self.choices = choices
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question_text)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
    
    def get_answer(self):
        return self.correct_answer

    def get_choices(self):
        return self.choices

    def get_question(self):
        return self.question_text
    
    def check_answer(self, answer):
        return answer == self.correct_answer



# define the Test class
class Test:
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
    
    
    def __init__(self):
        self.questions = random.sample(self.question_bank, 5)

    def administer(self, student):
        print(f"\nStarting test for {student.name} (ID: {student.student_id})")
        wrong_answers = []
        score = 0
        for i, question in enumerate(self.questions, start=1):
            print(f"\nProblem {i}:")
            question.display_question()
            while True:
                answer = input("Your answer: ")
                if answer not in question.get_choices():
                    print("Invalid choice. Please choose a valid option.")
                else:
                    break
            if question.check_answer(answer):
                score += 1
            else:
                wrong_answers.append((i, question, answer))
                
        print(f"\nTest completed! Score: {score}/{len(self.questions)}")
        student.update_score(score)
        
        if wrong_answers:
            print("\nIncorrect answers:\n")
            for i, question, answer in wrong_answers:
                print(f"Problem {i}: {question.get_question()}\nYour answer: {answer}\nCorrect answer: {question.get_answer()}\n")
        print("END OF TEST")
        print()
                

# define the Student class which takes in a name and id and sets test score to None initially
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.test_score = None

    def update_score(self, score):
        self.test_score = score
    
    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - Test Score: {self.test_score}"



# Example usage
if __name__ == "__main__":
    name = "Pickle Rick"
    studentID = 666666
    student_rick = Student(name, studentID)
    print(f"Example of student: {student_rick}")
    
    student_name = input("Enter the student's name: ")
    student_id = input("Enter the student's ID: ")
    student = Student(student_name, student_id)
    
    print()    
    print(f"Student info: {student}")

    test = Test()
    test.administer(student)

    print()
    print(f"\nFinal Score for {student.name} (ID: {student.student_id}): {student.test_score}")
    
    print()
    print(f"Updated student info: {student}")
