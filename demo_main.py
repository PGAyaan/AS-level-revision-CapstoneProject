def main():
    name = prompt_user_for_name()
    score_file = open_or_create_file(name)
    previous_score = read_previous_score(score_file)
    number_of_questions = prompt_user_for_number_of_questions()
    current_score = 0

    for i in range(1, number_of_questions + 1):
        question = get_question(i)
        correct_answer = get_correct_answer(i)
        user_answer = prompt_user_for_answer(question)
        
        if user_answer.lower() == correct_answer.lower():
            current_score += 1
        else:
            display_correct_answer(correct_answer)

    display_final_score(current_score)
    append_score_to_file(score_file, current_score)
    close_file(score_file)

    option = prompt_user_for_option()

    while option != "4":
        if option == "1":
            user_name = prompt_user_for_user_to_view()
            display_user_scores(user_name)
        elif option == "2":
            user_name = prompt_user_for_user_to_reset()
            reset_user_score(user_name)
        elif option == "3":
            main()

        option = prompt_user_for_option()

def prompt_user_for_name():
    return input("Enter your name: ")

def open_or_create_file(name):
    try:
        file = open(name + ".txt", "r+")
    except FileNotFoundError:
        file = open(name + ".txt", "w+")

    return file

def read_previous_score(file):
    previous_score = 0
    try:
        previous_score = int(file.readline())
    except ValueError:
        pass

    return previous_score

def prompt_user_for_number_of_questions():
    return int(input("How many questions do you want to answer? "))

def get_question(index):
    with open("questions.txt", "r") as file:
        questions = file.readlines()
        return questions[index - 1].strip()

def get_correct_answer(index):
    with open("answers.txt", "r") as file:
        answers = file.readlines()
        return answers[index - 1].strip()

def prompt_user_for_answer(question):
    print(question)
    return input("Enter your answer: ")

def display_correct_answer(correct_answer):
    print(f"Wrong. The correct answer is {correct_answer}")

def display_final_score(score):
    print(f"Your final score is: {score}")

def append_score_to_file(file, score):
    file.write(str(score) + "\n")

def close_file(file):
    file.close()

def prompt_user_for_option():
    print("Choose an option: ")
    print("1. View scores")
    print("2. Reset score")
    print("3. Answer more questions")
    print("4. Exit")
    return input()

def prompt_user_for_user_to_view():
    return input("Enter the name of the user: ")

def display_user_scores(user_name):
    try:
        with open(user_name + ".txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("User does not exist.")

def prompt_user_for_user_to_reset():
    return input("Enter the name of the user: ")

def reset_user_score(user_name):
    try:
        with open(user_name + ".txt", "w") as file:
            file.write("0\n")
        print("Score reset successfully.")
    except FileNotFoundError:
        print("User does not exist.")

if __name__ == "__main__":
    main()
