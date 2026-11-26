
# String-Based Examination Answer Evaluation
# ----------------------------------------
# Features:
# 1. Compare student answers with answer key
# 2. Calculate correct, incorrect, and unanswered answers
# 3. Apply negative marking
# 4. Calculate total marks and percentage
# 5. Display student-wise results

# Answer key
answer_key = ("A", "B", "C", "D", "A")

# Marks configuration
correct_mark = 4
negative_mark = 1
unanswered_mark = 0

# Student answers
students = [
    ("S101", "Arjun", ("A", "B", "C", "D", "A")),
    ("S102", "Priya", ("A", "C", "C", "D", "")),
    ("S103", "Rahul", ("B", "B", "", "A", "C")),
    ("S104", "Sneha", ("A", "B", "C", "D", "B"))
]

total_questions = len(answer_key)
maximum_marks = total_questions * correct_mark

results = []

# Evaluate each student
for student in students:
    student_id, name, answers = student

    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(total_questions):
        answer = answers[i].strip().upper()

        if answer == "":
            unanswered += 1
        elif answer == answer_key[i]:
            correct += 1
        else:
            incorrect += 1

    # Calculate score
    score = (
        correct * correct_mark
        - incorrect * negative_mark
        + unanswered * unanswered_mark
    )

    # Prevent negative total marks
    if score < 0:
        score = 0

    percentage = (score / maximum_marks) * 100

    # Store student result
    results.append(
        (
            student_id,
            name,
            correct,
            incorrect,
            unanswered,
            score,
            percentage
        )
    )

# Display results
print("\n========== EXAMINATION RESULTS ==========")
print("Maximum Marks:", maximum_marks)
print("Correct Answer Marks:", correct_mark)
print("Negative Marks:", negative_mark)

print("-" * 85)
print(
    f"{'ID':<8} {'Name':<12} {'Correct':<8} "
    f"{'Wrong':<8} {'Blank':<8} {'Score':<8} {'Percentage':<10}"
)
print("-" * 85)

for result in results:
    student_id, name, correct, incorrect, unanswered, score, percentage = result

    print(
        f"{student_id:<8} {name:<12} {correct:<8} "
        f"{incorrect:<8} {unanswered:<8} "
        f"{score:<8} {percentage:.2f}%"
    )

print("-" * 85)

# Find the topper
topper = results[0]

for result in results:
    if result[5] > topper[5]:
        topper = result

print("\nTopper:", topper[1])
print("Topper's Score:", topper[5], "/", maximum_marks)
