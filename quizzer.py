

def Quizzer(quiz_file):
    print("Hello! Welcome to Quizzer, your command-line quiz application.")

    quiz_content = load_quiz_file(quiz_file)
    if quiz_content is None:
        print("No quiz content found. Exiting.")
        return

    while True:
        print("\nQuiz Menu:")
        print("1. Start Quiz")
        print("2. Modify Quiz Content")
        print("3. Exit")
        choice = input("Please enter your choice (1-3): ")
        print("\n")

        if choice == '1':
            quiz_time(quiz_content)
        elif choice == '2':
            quiz_file = input("Enter quiz file path: ")
            quiz_content = load_quiz_file(quiz_file)
            if quiz_content is None:
                print("No quiz content found. Returning to main menu.")
                return
        elif choice == '3':
            print("Exiting the quiz.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            



def load_quiz_file(file_path):
    print(f"Reading quiz file from: {file_path}")
    if not file_path.endswith('.csv'):
        print("Error: The quiz file must be in CSV format.")
        return None
    try:
        with open(file_path, 'r') as file:
            # Splits each line by ',' and creates a dictionary
            content = dict(line.strip().split(',') for line in file)
            file.close()
            print("Quiz file read successfully.")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the quiz file: {e}")
        return None
    

def quiz_time(content):
    print("Starting the quiz...")
    print("Let's see what you know!")
    
    content = shuffle_quiz_content(content)

    score = 0

    for word, definition in content.items():
        user_answer = input(f"{definition} ")
        if user_answer.strip().lower() == word.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {word}")

    result = score / len(content) * 100
    print(f"Quiz completed. Your final score is: {result:.2f}%")

def shuffle_quiz_content(content):
    import random
    print("Shuffling quiz content...")
    items = list(content.items())
    random.shuffle(items)
    shuffled_content = dict(items)
    print("Quiz content shuffled successfully.")
    return shuffled_content


if __name__ == "__main__":
    import argparse
    from quizzer import Quizzer

    parser = argparse.ArgumentParser(description="Quizzer: A command-line quiz application.")
    parser.add_argument("quiz_file", help="Path to the quiz file (JSON format).")
    args = parser.parse_args()

    Quizzer(args.quiz_file)