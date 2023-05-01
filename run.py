def get_username():
    """
    Ask the player for a username
    """
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
    print("[s] Trivia about Science")
    print("[m] Trivia about Movies")
    print("[g] Trivia about Geography")
    print("[v] View score board\n\n")
    player_choice = input("Enter your choice: ")
    validate_choice(player_choice)


def validate_choice(input_choice):
    """
    Function to run a game or show the score board, based on 
    the choice of the player.
    """
    option_one = "s"
    option_two = "m"
    option_three = "g"
    option_four = "v"
    
    try:
        if input_choice in (option_one, option_two, option_three, option_four):  
            options(input_choice)
        else:
            raise ValueError()
    except ValueError:
        print("\nInvalid choice. Enter s, m, g or v to make a choice.")
        input("Press enter to choose again.")
        choose_option()

    
def options(input_choice):
    """
    Displaying questions in chosen quiz or score board, based on valid choice by player. 
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
    """
    valid = True

    try:
        for question in question_list:
            correct_answer = question.pop()
            for item in question:
                print(item)
                player_answer = input("Enter your answer: ")
                validate_answer(player_answer)

def validate_answer(input_answer):
    """
    Validating player answer to question
    """
    answer_one = "1"
    answer_two = "2"
    answer_three = "3"
    
    try:
        if input_anwser in (answer_one, answer_two, answer_three):  
            options(input_choice)
        else:
            raise ValueError()
    except ValueError:
        print("\nInvalid answer. Enter 1, 2 or 3 to answer.")
        input("Press enter to try again.")
        options(input_choice)
        # Another function is supposed to be called (when it is built)

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
    print("    Did you know that shrimps have their heart in the brain?    \n")
    print("                       Want to learn more?                      \n")
    print("            Test your trivia knowledge with a quiz!             ")
    print("----------------------------------------------------------------\n")

    get_username()
    choose_option()
    

main()