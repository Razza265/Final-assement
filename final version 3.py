import random

# Define the questions
questions = [
    {
        "question": "What is the Maori word for 'hello'?",
        "options": ["Kia ora", "Haere mai", "Nau mai", "Tena koe"],
        "answer": "Kia ora"
    },
    {
        "question": "What is the Maori word for 'goodbye'?",
        "options": ["Haere ra", "Ka kite ano", "Aroha mai", "Hei konei ra"],
        "answer": "Haere ra"
    },
    {
        "question": "What is the Maori word for 'thank you'?",
        "options": ["Aroha mai", "Ka kite ano", "Kia ora", "Kia pai to ra"],
        "answer": "Kia ora"
    },
    {
        "question": "What is the Maori word for 'please'?",
        "options": ["Tena koe", "Tautoko mai", "Whakarongo mai", "Whakarongo mai"],
        "answer": "Tautoko mai"
    },
    {
        "question": "What is the Maori word for 'one'?",
        "options": ["Tahi", "Rua", "Toru", "Wha"],
        "answer": "Tahi"
    },
    {
        "question": "What is the Maori word for 'two'?",
        "options": ["Rua", "Tahi", "Toru", "Wha"],
        "answer": "Rua"
    },
    {
        "question": "What is the Maori word for 'three'?",
        "options": ["Toru", "Tahi", "Rua", "Wha"],
        "answer": "Toru"
    },
    {
        "question": "What is the Maori word for 'four'?",
        "options": ["Wha", "Tahi", "Rua", "Toru"],
        "answer": "Wha"
    },
    {
        "question": "What is the Maori word for 'five'?",
        "options": ["Rima", "Tahi", "Rua", "Toru"],
        "answer": "Rima"
    },
    {
        "question": "What is the Maori word for 'six'?",
        "options": ["Ono", "Tahi", "Rua", "Toru"],
        "answer": "Ono"
    },
    {
        "question": "What is the Maori word for 'seven'?",
        "options": ["Whitu", "Tahi", "Rua", "Toru"],
        "answer": "Whitu"
    },
    {
        "question": "What is the Maori word for 'eight'?",
        "options": ["Waru", "Tahi", "Rua", "Toru"],
        "answer": "Waru"
    },
    {
        "question": "What is the Maori word for 'nine'?",
        "options": ["Iwa", "Tahi", "Rua", "Toru"],
        "answer": "Iwa"
    },
    {
        "question": "What is the Maori word for 'ten'?",
        "options": ["Tekau", "Tahi", "Rua", "Toru"],
        "answer": "Tekau"
    },
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
print("Quiz complete! You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")



