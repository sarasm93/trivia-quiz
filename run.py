import os
import time
username = 0

score_board = [
    ["Jenny XX", "GameGuru XX", "lulu XX", "Carl XX"], 
    [], 
    []
    ]


# The code on line XXXXXXXXXXX(os.system(clear)) is taken from this Stackoverflow page. 
# https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
def clear_screen():
    """
    Clear screen when called, to make the user experiance better.
    """
    time.sleep(1.5)
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
        clear_screen()
    if valid == False:
        get_username()


def display_options():
    # WANT TO START A NEW PAGE (REMOVE INTRO)
    """
    Display options menu, to see what options choose game or show score board
    """
    print("\n\nChoose a quiz or show the score board")
    print("-------------------------------------\n")

    options_list = ["[s] Trivia about Science", "[m] Trivia about Movies", "[g] Trivia about Geography", "[v] View score board\n\n"]
    for option in options_list:
        print(option)


def choose_option():
    """

    """

        player_choice = input("Enter your choice: ")
    if validate_choice(player_choice, "s, m, g, or v") is True:
        clear_screen()
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
        if input_choice in (valid_options): 
            run_option(input_choice)
            return True
        else:
            raise ValueError()
    except ValueError:
        print(f"\n\nInvalid choice. Enter {valid_options} to make a choice.")
        return False


def run_option(input_choice):
    """
    Initiate the right quiz or initiate to show score board, based
    on valid choice by player.
    """
    # WANT TO START A NEW PAGE (REMOVE OPTIONS)

    if input_choice == "s":
        run_science()
    if input_choice == "m":
        run_movies()
    if input_choice == "g":
        run_geography()
    if input_choice == "v":
        run_score_board()


def run_science():
    """
    Display questions for science quiz.
    """
    # WANT TO MAKE THE FUNCTION LINGER A BIT SO THAT PLAYER HAVE TIME TO SEE CORRECT/INCORRECT
    science_questions = [
        ["Question 1: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
        ["Question 2: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
        ["Question 3: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
        ["Question 4: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
        ["Question 5: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "2"],
        ["Question 6: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"]
    ]

    print("\n\nSCIENCE TRIVIA")
    player_score = 0

    print(f"\nScore: {player_score}\n")
    correct_answer = science_questions[0].pop()

    for question in science_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = science_questions[1].pop()

    for question in science_questions[1]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = science_questions[2].pop()

    for question in science_questions[2]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")
    
    print(f"\n\nScore: {player_score}\n")
    correct_answer = science_questions[3].pop()

    for question in science_questions[3]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = science_questions[4].pop()

    for question in science_questions[4]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = science_questions[5].pop()

    for question in science_questions[5]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    player_username_score = []
    player_username_score.append(username)
    player_username_score.append(player_score)
    save_score_science(player_username_score)

    print(f"\nYou finished the science quiz! Well done! Your score: {player_score}\n")
    input("Press enter to get back to menu")
    choose_option()


def run_movies():
    """
    Display questions for movies quiz.
    """
    # WANT TO MAKE THE FUNCTION LINGER A BIT SO THAT PLAYER HAVE TIME TO SEE CORRECT/INCORRECT
    science_questions = [
        ["Question 1: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
        ["Question 2: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
        ["Question 3: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"],
        ["Question 4: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "1"],
        ["Question 5: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "2"],
        ["Question 6: What....", "[1] Option 1", "[2] Option 2", "[3] Option 3\n", "3"]
    ]

    print("\n\nSCIENCE TRIVIA")
    player_score = 0

    print(f"\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")
    
    print(f"\n\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    print(f"\n\nScore: {player_score}\n")
    correct_answer = movies_questions[0].pop()

    for question in movies_questions[0]:
        print(question)
        
    player_answer = input("Enter your answer: ")

    if player_answer == correct_answer:
        print("Correct! Well done!")
        player_score += 1
    else: 
        print("Incorrect.")

    player_username_score = []
    player_username_score.append(username)
    player_username_score.append(player_score)
    save_score_movies(player_username_score)

    print(f"\nYou finished the science quiz! Well done! Your score: {player_score}\n")
    input("Press enter to get back to menu")
    choose_option()


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
    choose_option()
    

main()