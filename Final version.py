import random

# Define the quiz questions and answers as a dictionary
quiz_questions = {
    "What does 'one' mean? ": "tahi",
    "What does 'two mean? ": "rua",
    "What does 'three' mean? ": "toru",
    "What does 'four' mean? ": "wha",
    "What does 'five' mean? ": "rima"
}

# Shuffle the quiz questions
quiz_order = list(quiz_questions.keys())
random.shuffle(quiz_order)

# Initialize a variable to keep track of the score
score = 0

# Loop through each question in the quiz
for question in quiz_order:
    # Ask the question and get the user's answer
    answer = input(question)
    # Check if the user's answer is correct
    if answer.lower() == quiz_questions[question].lower():
        # If the answer is correct, increase the score and display a message
        score += 1
        print("Correct!")
    else:
        # If the answer is incorrect, display the correct answer
        print(f"Incorrect. The correct answer is {quiz_questions[question]}")

# Display the final score
print(f"Quiz complete! You got {score} out of {len(quiz_questions)} correct.")
