import random

# Define the quiz questions and answers
questions = [
    {
        "question": "What does 'Kia ora' mean in English?",
        "options": ["Thank you", "Hello", "Goodbye", "Sorry"],
        "answer": "Hello"
    },
    {
        "question": "What is the Maori word for 'family'?",
        "options": ["Whanau", "Mana", "Koha", "Hapu"],
        "answer": "Whanau"
    },
    {
        "question": "What is the Maori word for 'thank you'?",
        "options": ["Koha", "Aroha", "Haere mai", "Mihi"],
        "answer": "Koha"
    },
    {
        "question": "What is the Maori word for 'love'?",
        "options": ["Mana", "Tapu", "Aroha", "Hapu"],
        "answer": "Aroha"
    },
    {
        "question": "What is the Maori word for 'welcome'?",
        "options": ["Nau mai", "Haere mai", "Whakarongo mai", "Kia ora"],
        "answer": "Nau mai"
    },
    {
        "question": "What is the Maori word for 'health'?",
        "options": ["Koha", "Whanau", "Hauora", "Mana"],
        "answer": "Hauora"
    },
    {
        "question": "What is the Maori word for 'spiritual power'?",
        "options": ["Tapu", "Hapu", "Whakapapa", "Mana"],
        "answer": "Mana"
    },
    {
        "question": "What is the Maori word for 'tribe'?",
        "options": ["Koha", "Whanau", "Hapu", "Iwi"],
        "answer": "Iwi"
    },
    {
        "question": "Count from 1 to 10 in Maori.",
        "options": ["Tahi, rua, toru, wha, rima, ono, whitu, waru, iwa, tekau",
                    "Tahi, rua, toru, wha, rima, ono, whitu, waru, iwa, tau"],
        "answer": "Tahi, rua, toru, wha, rima, ono, whitu, waru, iwa, tekau"
    }
]

# Shuffle the quiz questions
random.shuffle(questions)

# Loop through the quiz questions
score = 0
for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    if answer == str(question["options"].index(question["answer"]) + 1):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {question['answer']}.")

# Display the final score
print(f"Your final score is {score} out of {len(questions)}.")
