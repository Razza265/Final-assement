import random

print("Welcome to the Maori Quiz!")
print("This quiz will test your knowledge of the Maori language, specifically the days of the week.")
print("Let's get started!")

name = input("Please enter your name: ")
age = input("Please enter your age: ")

start_quiz = input("Hi " + name + "! Would you like to take the Maori Quiz? (yes/no): ")
if start_quiz.lower() != "yes":
    print("No problem! Feel free to come back whenever you're ready to test your Maori knowledge. Goodbye!")
    exit()

questions = [
    {
        "question": "What is the Maori word for 'Monday'?",
        "options": ["Ratu", "Tuarua", "Tuatea", "Tuterei"],
        "answer": "Ratu"
    },
    {
        "question": "What is the Maori word for 'Tuesday'?",
        "options": ["Tuarua", "Ratu", "Tuatea", "Tuterei"],
        "answer": "Tuarua"
    },
    {
        "question": "What is the Maori word for 'Wednesday'?",
        "options": ["Tuatea", "Ratu", "Tuarua", "Tuterei"],
        "answer": "Tuatea"
    },
    {
        "question": "What is the Maori word for 'Thursday'?",
        "options": ["Tuterei", "Ratu", "Tuarua", "Tuatea"],
        "answer": "Tuterei"
    },
    {
        "question": "What is the Maori word for 'Friday'?",
        "options": ["Paraire", "Ratu", "Tuarua", "Tuatea"],
        "answer": "Paraire"
    },
    {
        "question": "What is the Maori word for 'Saturday'?",
        "options": ["Hatarei", "Ratu", "Tuarua", "Tuatea"],
        "answer": "Hatarei"
    },
    {
        "question": "What is the Maori word for 'Sunday'?",
        "options": ["Ra Tapu", "Ratu", "Tuarua", "Tuatea"],
        "answer": "Ra Tapu"
    }
]

# Shuffle the questions
random.shuffle(questions)

# Initialize the score
score = 0

# Ask the questions
for question in questions:
    print(question["question"])
    random.shuffle(question["options"])
    for i in range(len(question["options"])):
        print(str(i+1) + ". " + question["options"][i])
    user_answer = input("Enter your answer (1-" + str(len(question["options"])) + "): ")
    if user_answer.isnumeric():
        user_answer = int(user_answer)
        if user_answer > 0 and user_answer <= len(question["options"]):
            if question["options"][user_answer-1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is: " + question["answer"])
        else:
            print("Invalid input. Skipping this question...")
    else:
        print("Invalid input. Skipping this question...")

# Display the score
print("Quiz complete, " + name + "! You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")

