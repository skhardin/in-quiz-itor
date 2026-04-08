
def Quizzer(quiz_file):
    print("Hello! Welcome to Quizzer, your command-line quiz application.")

    quiz_content = load_quiz_file(quiz_file)
    if quiz_content is None:
        print("Error: No quiz content found. Exiting.")
        return

    while True:
        print("==============================")
        print("\nQuiz Menu:")
        print("==============================")
        print("1. Start Quiz")
        print("2. Modify Quiz Content")
        print("3. Exit")
        print("==============================")
        choice = input("Please choose an option (1-3): ")
        print("==============================")
        print("\n")

        if choice == '1':
            quiz_time(quiz_content)
        elif choice == '2':
            quiz_file = input("Enter quiz file path: ")
            quiz_content = load_quiz_file(quiz_file)
            if quiz_content is None:
                print("Error: No quiz content found. Returning to main menu.")
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
    

def quiz_time(quiz_content):
    if quiz_content is None:
        print("Error: No quiz content available. Please load a quiz file first.")
        return
    
    print("Starting the quiz...")
    print("Let's see what you know!")
    print("\n=== Pre-Assessment ===\n")
    
    quiz_content = shuffle_quiz_content(quiz_content)

    result = pre_assessment(quiz_content)
    print(f"\nPre-assessment completed. Your final score is: {result:.2f}%\n")

    while result < 75:
        print("Your score is below 75%. The fill-in-the-blank exercise is a great way to learn.")
        print("Let's try it out!\n")
        result = fill_in_the_blank(quiz_content)
        print(f"\nYour fill-in-the-blank score is: {result:.2f}%\n")



def pre_assessment(quiz_content):
    score = 0
    total = len(quiz_content)

    for i, (key, definition) in enumerate(quiz_content.items(), start=1):
        print(f"Question {i} of {total}:")
        print(f"Definition: {definition}")
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == key.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {key}")
        print("")

    result = score / total * 100
    return result



def fill_in_the_blank(quiz_content):
    import random
    if quiz_content is None:
        print("Error: No quiz content available. Please load a quiz file first.")
        return
    
    print("\n=== Fill-in-the-Blank Quiz ===")
    print("Fill in the blanks with the correct words!\n")

    quiz_content = shuffle_quiz_content(quiz_content)

    score = 0

    ignore_words = ["a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "in", "on", "at", "by", "for", "with", "about", "as", "of", "to", "from", "that", "this", "these", "those", "it", "its", "he", "she", "they", "we", "you"]

    for i, (key, definition) in enumerate(quiz_content.items(), start=1):

        definition_array = definition.strip().split(' ')
        candidate_indexes = [idx for idx, word in enumerate(definition_array) if word.lower() not in ignore_words]
        random_index = random.randint(0, len(candidate_indexes) - 1)
        blank_index = candidate_indexes[random_index]

        answer = definition_array[blank_index]
        fill_in_the_blank_definition = " ".join([word if index != blank_index else "____" for index, word in enumerate(definition_array)])
        
        print(f"Question {i} of {len(quiz_content)}:")
        print(f"{key}: {fill_in_the_blank_definition}")
        user_answer = input("Fill in the blank: ")

        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
        print("")

    result = score / len(quiz_content) * 100
    return result



def shuffle_quiz_content(quiz_content):
    import random
    if quiz_content is None:
        print("Error: No quiz content available. Please load a quiz file first.")
        return None
    
    print("Shuffling quiz content...")
    items = list(quiz_content.items())
    random.shuffle(items)
    shuffled_content = dict(items)
    print("Quiz content shuffled successfully.\n")
    return shuffled_content
