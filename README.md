#  Python CLI Quiz Application

## Project Overview

The **Python CLI Quiz Application** is a command-line based quiz program developed using Python.

The application loads quiz questions from a separate JSON file, displays questions and multiple-choice options to the user, accepts answers, checks whether the answers are correct, calculates the score, and displays the final result.

The project was developed as part of the **Python Programming Track**.

---

##  Objective

The main objective of this project is to practice:

- Python dictionaries
- Python lists
- Loops
- Conditional statements
- Functions and application flow
- JSON data handling
- User input
- Score calculation
- Input validation
- Randomization

---

##  Technologies Used

- **Python**
- **JSON**

---

##  Project Structure

```text
quiz_application/
│
├── quiz.py
├── questions.json
└── README.md
```

### `quiz.py`

Contains the main program logic.

It is responsible for:

- Loading questions
- Randomizing questions
- Displaying questions
- Displaying options
- Accepting user answers
- Validating answers
- Checking correct answers
- Calculating the score
- Displaying the final result

### `questions.json`

Stores the quiz questions separately from the Python program.

Each question contains:

- Question
- Four options
- Correct answer

---

##  How the Application Works

The application follows these steps:

```text
Start
  ↓
Load questions from JSON
  ↓
Randomize question order
  ↓
Display question
  ↓
Display options
  ↓
Get user's answer
  ↓
Validate answer
  ↓
Check correct answer
  ↓
Update score
  ↓
Repeat for all questions
  ↓
Calculate percentage
  ↓
Display final result
  ↓
End
```

---

##  Main Features

### 1. JSON Question Storage

Questions are stored separately in `questions.json`.

Example:

```json
{
    "question": "What is the capital of India?",
    "options": {
        "A": "Mumbai",
        "B": "Delhi",
        "C": "Chennai",
        "D": "Hyderabad"
    },
    "answer": "B"
}
```

This keeps the quiz data separate from the program logic.

---

### 2. Random Question Order

The application uses Python's `random` module.

```python
random.shuffle(questions)
```

This changes the order of questions each time the program runs.

---

### 3. Multiple Choice Questions

Each question contains four options:

```text
A
B
C
D
```

The user selects one option.

---

### 4. Input Validation

The program accepts only:

```text
A
B
C
D
```

If the user enters another value, the program displays:

```text
Invalid answer!
Please enter A, B, C, or D.
```

---

### 5. Answer Checking

The user's answer is compared with the correct answer stored in JSON.

```python
if user_answer == question["answer"]:
    score += 1
```

If the answer is correct, the score increases by 1.

---

### 6. Score Calculation

After all questions are completed, the application calculates:

- Total questions
- Correct answers
- Wrong answers
- Score
- Percentage

The percentage is calculated using:

```python
percentage = (score / total_questions) * 100
```

---

##  How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

---

### Step 2: Open the Project Folder

Open the terminal or command prompt inside the project folder.

---

### Step 3: Run the Program

Use:

```bash
python quiz.py
```

---

## Sample Output

```text
==============================
       PYTHON QUIZ
==============================

Question 1
What is the extension of a Python file?
A. .java
B. .html
C. .py
D. .js

Enter your answer (A/B/C/D): C
Correct!

Question 2
What is the capital of India?
A. Mumbai
B. Delhi
C. Chennai
D. Hyderabad

Enter your answer (A/B/C/D): B
Correct!

...

==============================
       QUIZ FINISHED
==============================

Total Questions: 10
Correct Answers: 10
Wrong Answers: 0
Score: 10 / 10
Percentage: 100.0 %
Excellent!
```

---

## Current Quiz Details

| Feature | Details |
|---|---|
| Number of Questions | 10 |
| Question Type | Multiple Choice |
| Options | A, B, C, D |
| Data Storage | JSON |
| Question Order | Random |
| Score Calculation | Yes |
| Input Validation | Yes |
| Final Result | Yes |

---

## Learning Outcomes

Through this project, I practiced:

- Reading JSON files using Python
- Working with lists and dictionaries
- Using `for` loops
- Using `while` loops
- Using `if`, `elif`, and `else`
- Taking user input
- String methods such as `strip()` and `upper()`
- Using `enumerate()`
- Using `random.shuffle()`
- Calculating percentages
- Separating data from program logic

---

##  Future Improvements

The project can be improved by adding:

- Timer for each question
- Different quiz categories
- Difficulty levels
- More questions
- High-score storage
- Player name
- Score history
- Restart quiz option
- Graphical user interface
- Database support

---

