import json
import random
with open("questions.json", "r") as file:
    questions = json.load(file)
random.shuffle(questions)
score = 0
print("==============================")
print("       PYTHON QUIZ")
print("==============================")
for number, question in enumerate(questions, start=1):
    print()
    print("Question", number)
    print(question["question"])
    for key, value in question["options"].items():
        print(key + ".", value)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid answer!")
        user_answer = input("Please enter A, B, C, or D: ").strip().upper()
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])
total_questions = len(questions)
wrong_answers = total_questions - score
percentage = (score / total_questions) * 100
print()
print("==============================")
print("       QUIZ FINISHED")
print("==============================")
print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong Answers:", wrong_answers)
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")
if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Need More Practice!")
