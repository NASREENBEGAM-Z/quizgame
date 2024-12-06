# Python Quiz Game

# Questions, options, and answers
questions = (
    "How many elements are in the periodic table?",
    "Which is the largest egg-laying animal?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which is the hottest planet in the solar system?"
)

options = (
    ("A: 108", "B: 118", "C: 120", "D: 130"),
    ("A: Ostrich", "B: Turtle", "C: Crocodile", "D: Platypus"),
    ("A: Oxygen", "B: Hydrogen", "C: Nitrogen", "D: Carbon Dioxide"),
    ("A: 206", "B: 208", "C: 210", "D: 212"),
    ("A: Venus", "B: Mars", "C: Mercury", "D: Jupiter")
)

answers = ("B", "A", "C", "A", "A")

# To store user's guesses
guesses = []

# Score counter
score = 0

# Function to display the quiz
def run_quiz():
    global score

    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question}")
        for option in options[index]:
            print(option)
        
        # Get user's answer
        while True:
            guess = input("Enter your answer (A, B, C, or D): ").upper()
            if guess in ("A", "B", "C", "D"):
                guesses.append(guess)
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        # Check answer
        if guess == answers[index]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong. The correct answer was {answers[index]}.")

# Function to display the results
def show_results():
    print("\n--- Quiz Results ---")
    print(f"You got {score}/{len(questions)} questions correct.")
    print("\nYour answers vs. Correct answers:")
    for i, guess in enumerate(guesses):
        print(f"Question {i + 1}: You answered {guess}, Correct answer was {answers[i]}.")
    print(f"\nYour Score Percentage: {round((score / len(questions)) * 100, 2)}%")

# Run the game
if __name__ == "__main__":
    print("Welcome to the Python Quiz Game!")
    run_quiz()
    show_results()
