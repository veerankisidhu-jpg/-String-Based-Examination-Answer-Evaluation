# -String-Based-Examination-Answer-Evaluation
Name:V.Siva Sambhavi 
 Roll number:N26V01A0389
 section:05
# String-Based Examination Answer Evaluation

## Project Description

This project is a Python-based examination evaluation system.
It compares student answer strings with a predefined answer key
and calculates examination results automatically.

The program identifies correct, incorrect, and unanswered
questions and applies negative marking to incorrect answers.

## Objectives

- Compare student answers with the answer key.
- Count correct answers.
- Count incorrect answers.
- Identify unanswered questions.
- Apply negative marking.
- Calculate total marks and percentage.
- Generate student-wise examination results.
- Identify the highest-scoring student.

## Technologies Used

- Python 3
- Strings
- Tuples
- Lists
- Conditional statements
- Loops
- Arithmetic operators

## Features

1. Automatic answer evaluation.
2. Negative marking calculation.
3. Student-wise result generation.
4. Percentage calculation.
5. Topper identification.
6. Simple and readable output.

## How to Run

1. Install Python 3.
2. Save the program as `exam_evaluation.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the program.
5. Execute the following command:

   python exam_evaluation.py

## Input Format

The answer key is stored as a tuple.

Example:

    answer_key = ("A", "B", "C", "D", "A")

Student answers are stored using student ID, name,
and a tuple of answers.

Example:

    ("S101", "Arjun", ("A", "B", "C", "D", "A"))

An empty string represents an unanswered question.

## Marking Scheme

- Correct answer: +4 marks
- Incorrect answer: -1 mark
- Unanswered question: 0 marks

The final score is not allowed to fall below zero.

## Formula

    Score = (Correct Answers * Correct Marks)
            - (Incorrect Answers * Negative Marks)

    Percentage = (Score / Maximum Marks) * 100

## Sample Output

    ========== EXAMINATION RESULTS ==========
    Maximum Marks: 20
    Correct Answer Marks: 4
    Negative Marks: 1

    ID       Name         Correct  Wrong    Blank    Score    Percentage
    ---------------------------------------------------------------------
    S101     Arjun        5        0        0        20       100.00%
    S102     Priya        3        1        1        11       55.00%
    S103     Rahul        2        2        1        6        30.00%
    S104     Sneha        4        1        0        15       75.00%

    Topper: Arjun
    Topper's Score: 20 / 20

## Conclusion

This project demonstrates how Python strings, tuples, lists,
loops, and conditional statements can be used to automate
examination answer evaluation and generate accurate
student-wise results.
