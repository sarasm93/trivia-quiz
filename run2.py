import os
import time
username = 0

score_board_science = [
        ["Jenny XX"],
        ["GameGuru XX"],
        ["lulu XX"],
        ["Carl XX"]
    ]

score_board = [[], [], []]


def clear_screen():
    time.sleep(3)
    os.system('clear')


def get_username():
    """
    Ask the player for a username.
    """
    global username
    username = input("                  Please enter a username: ")
    validate_username(username)


def validate_username(input_name):
    """
    Validate username by checking that minimum two and maximum 10
    characteres were entered.
    """
    valid = True
    try:
        for blank in input_name:
            if (blank.isspace()) == True:
                raise ValueError(
                    " It cannot contain blank spaces")
        if len(input_name) == 0:
            raise ValueError(
                " You didn't enter a username")
        if len(input_name) < 2:
            raise ValueError(
                " It needs to be at least 2 characters")
        if len(input_name) > 10:
            raise ValueError(
                " It cannot be longer than 10 characters")
    except ValueError as e:
        print(f"\n     Invalid username: {e}.")
        print("                        Please try again.\n")
        valid = False
    
    if valid:
        print("\n                           Lets play!\n\n")
    if valid == False:
        get_username()

# WANT TO LET THE GET_USERNAME FUNCTION LINGER A FEW SECONDS

def choose_option():
    # WANT TO START A NEW PAGE (REMOVE INTRO)
    """
    Display options menu, to choose game or show score board
    """
    print("\n\nChoose a quiz or show the score board")
    print("-------------------------------------\n")
    options_list = ["[s] Trivia about Science", "[m] Trivia about Movies", "[g] Trivia about Geography", "[v] View score board\n\n"]
    for option in options_list:
        print(option)
    player_choice = input("Enter your choice: ")
    if validate_choice(player_choice, ["s", "m", "g", "v"]) is True:
        run_option(player_choice)
    else:
        choose_option()


def validate_choice(input_choice, valid_options):
    """
    Function to run a game or show the score board, based on
    the choice of the player.
    """
    input_choice = input_choice.lower()
    try:
        if input_choice in valid_options:
            return True
        else:
            raise ValueError()
    except ValueError:
        print(f"\nInvalid choice. Enter {valid_options} to make a choice.")
        return False

def run_option(input_choice):
    """
    Initiate the right quiz or initiate to show score board, based
    on valid choice by player.
    """
    # WANT TO START A NEW PAGE (REMOVE OPTIONS)
    input_choice = input_choice.lower()
    if input_choice == "s":
        science_questions = [
            ["Question 1: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
            ["Question 2: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
            ["Question 3: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
            ["Question 4: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
            ["Question 5: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "2"],
            ["Question 6: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"]
        ]
        print("\n\nSCIENCE TRIVIA")
        score = run_quiz(science_questions)
        score_board[0].append(f'{username} - {score}')
        print(f'Science ScoreBoard: {score_board[0]}')

        # run_science()
    if input_choice == "m":
        movie_questions = [
            ["Question 1: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
            ["Question 2: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
            ["Question 3: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
            ["Question 4: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
            ["Question 5: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "2"],
            ["Question 6: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"]
        ]
        print("\n\nMOVIE TRIVIA")
        score = run_quiz(movie_questions)
        score_board[1].append(f'{username} - {score}')
        print(f'Movie ScoreBoard: {score_board[1]}')

        # run_movies()
    if input_choice == "g":
        run_geography()
    if input_choice == "v":
        run_score_board()


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question)
        option_valid = False
        while option_valid is False:
            player_answer = input("Enter your answer: ")
            option_valid = validate_choice(player_answer, ["1", "2", "3"])
        correct_answer = question.pop()
        if correct_answer == player_answer:
            print('Correct !')
            score = score + 1
        else:
            print('Incorrect !')
    return score

def validate_answer():
    print("validate")


def save_score_science(score):
    """
    Function to save player score for science quiz to score board.
    """
    global score_board_science
    score_board_science.append(score)


def save_score_movies(score):
    """
    Function to save player score for movie quiz to score board.
    """
    global score_board_movies
    score_board_movies.append(score)


def save_score_geography(score):
    """
    Function to save player score for geography quiz to score board.
    """
    global score_board_geography
    score_board_geography.append(score)


def run_score_board():
    """
    Function to display scores if player chooses to in options function.
    """
    # Used these Stackoverflow pages to help me build the loop with range()
    # and len() and to figure out how to use '*' to remove all '[]', ','' and
    # '""' from the score board list when printed.
    # https://stackoverflow.com/questions/48053979/print-2-lists-side-by-side
    # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
    
    for saved_score in range(len(score_board_science)):
        print(*score_board_science[saved_score])

    #for saved_score in range(len(score_board_movies)):
        #print(*score_board_movies[saved_score])
    
    #for saved_score in range(len(score_board_geography)):
        #print(*score_board_geography[saved_score])

    input("\n\nPress enter to get back to menu")
    choose_option()

def main():
    """
    Run all functions
    """
    print("\n\nTTTTTTTTTT   RRRR    IIIIII  VV       VV  IIIIII       AAA")
    print("    TT       R   R     II     VV     VV     II        AA AA")
    print("    TT       R  R      II      VV   VV      II       AA   AA")
    print("    TT       RRR       II       VV VV       II      AAAAAAAAA")
    print("    TT       R  R      II        VVV        II     AA       AA")
    print("    TT       R   R   IIIIII       V       IIIIII  AA         AA\n")

    print("----------------------------------------------------------------")
    print("   Did you know that shrimp have their hearts in their heads?   \n")
    print("                       Want to learn more?                      \n")
    print("            Test your trivia knowledge with a quiz!             ")
    print("----------------------------------------------------------------\n")

    get_username()
    clear_screen()
    choose_option()
    

main()