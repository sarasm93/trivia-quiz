import os
import time
from tabulate import tabulate as tb

username = 0

score_boards = [
    {"Jenny": 10, "GameGuru": 7, "lulu": 7, "Carl": 6},
    {"lulu": 8, "GameGuru": 8, "Jenny": 7, "Carl": 4},
    {"Jenny": 9, "Carl": 5, "lulu": 4, "GameGuru": 4}
]


def delay(input_time):
    """
    When this function is called, the next code to be displayed is
    delayed. This makes user experiance better as the player have more
    time to see what happens.
    """
    time.sleep(input_time)


def clear_screen():
    """
    When this function is called, the screen is cleared. This makes user
    experiance better as the the terminal is not so cluttered with text.
    """
    # The code on line XXXXXXXXXXXX is taken from this Stackoverflow page.
    # https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
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
    Validate username by checking that a username is entered, no blank
    spaces are used, the chosen username is not already taken, and that
     minimum two and maximum 10 characteres are entered.
    """
    valid = True

    try:
        for blank in input_name:
            if (blank.isspace()) is True:
                raise ValueError(
                    " It cannot contain blank spaces")
        for board in score_boards:
            taken_usernames = board.keys()
            for name in taken_usernames:
                if input_name == name:
                    raise ValueError(
                        " This username is already taken")
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
        delay(1.2)
    if valid is False:
        get_username()


def display_options():
    """
    Display options menu with options to choose a game or display score board.
    """
    clear_screen()
    print("\n\nChoose a quiz or show the score board")
    print("-------------------------------------\n")

    options_list = ["[s] Trivia about Science", "[m] Trivia about Movies",
                    "[g] Trivia about Geography", "[v] View score board",
                    "[q] Quit\n\n"]
    for option in options_list:
        print(option)
    choose_option()


def choose_option():
    """
    Asking player to choose an option from the options menu.
    """
    player_choice = input("Enter your choice: ")
    if validate_choice(player_choice, ["s", "m", "g", "v", "q"]) is True:
        clear_screen()
        run_option(player_choice)
    else:
        choose_option()


def validate_choice(input_choice, options):
    """
    Function to run a game or show the score board, based on
    player choice. To make the valid options print nicely
    to the player, the valid options list is re-designed by (1) splitting it,
    (2) adding "or" to the second to last position, (3) putting it back
    together again and (4) removing all '[]' and ','.
    """
    # Code on line XXXXXXXXXXX is taken from the below Geeksforgeeks.org page.
    # The code has been adjusted to fit to this program by changing variable
    # names and the position to insert new word "or".
    # https://www.geeksforgeeks.org/python-add-phrase-in-middle-of-string/
    input_choice = input_choice.lower()
    options_string = str(options)

    add_word = "or"
    words = options_string.split()
    position = len(words) - 1
    join_options = " ".join(words[:position] + [add_word] + words[position:])
    new_options = str(join_options).replace("[", "").replace("]", "")

    try:
        if input_choice in (options):
            return True
        else:
            raise ValueError()
    except ValueError:
        print(f"\n\nInvalid choice. Enter {new_options} to make a choice.")
        return False


def sort_score_board(input_board, list_index):
    """
    Function sorting dictionary of scores in score board each time a player
    finishes a quiz. Only the dictionary for the quiz that the player just
    played is sorted.
    """
    # Code on line XXXXXXXXXXX is taken from the below page to loop through
    # a dictionary of scores. The code has been adjusted to fit to this
    # program by changing variable names.
    # https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
    dictionary = input_board[list_index]
    sorted_board = {}
    sorted_scores = sorted(dictionary.values(), reverse=True)
    for score in sorted_scores:
        for key in dictionary.keys():
            if dictionary[key] == score:
                sorted_board[key] = dictionary[key]

    dictionary.clear()
    dictionary.update(sorted_board)


def print_score_board(input_board, title):
    """
    When player chooses option "v" in options menu, this function is run to
    show the score board for each quiz in a table.
    """
    # Code on line XXXXXXXXXXX is taken from the below page to create the
    # tables. The code has been adjusted to fit to this program by
    # changing variable names.
    # https://www.askpython.com/python-modules/tabulate-tables-in-python
    headers = [f"{title}", "Player    ", "Score"]
    scores_as_list = [headers]
    for key in input_board.keys():
        player_data = ["", key, input_board[key]]
        scores_as_list.append(player_data)
    table = tb(scores_as_list, headers='firstrow')
    print(f"{table}\n\n")


def run_option(input_choice):
    """
    Initiate the right quiz, show score board or quit game, based
    on valid choice by player.
    """
    input_choice = input_choice.lower()

    if input_choice == "s":
        clear_screen()
        print("\n\nSCIENCE TRIVIA\n\n")
        # The last item in each nested list of questions is the correct answer
        # for that question. It´s the same for all the quizes
        # (i.e. choices "s", "m", "g").
        science_questions = [
            ["Question 1: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 2: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 3: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 4: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 5: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "2"],
            ["Question 6: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"]
        ]
        score = run_quiz(science_questions)
        score_boards[0].update({username: score})
        sort_score_board(score_boards, 0)
        print(score_boards)
        print("\nYou finished the SCIENCE TRIVIA quiz! Well done!")
        print(f"Your score: {score}\n")
        input("Press enter to get back to menu")
        display_options()

    if input_choice == "m":
        clear_screen()
        print("\n\nMOVIE TRIVIA\n\n")
        movie_questions = [
            ["Question 1: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 2: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 3: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 4: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 5: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "2"],
            ["Question 6: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"]
        ]
        score = run_quiz(movie_questions)
        score_boards[1].update({username: score})
        sort_score_board(score_boards, 1)
        print("\nYou finished the MOVIE TRIVIA quiz! Well done!")
        print("Your score: {score}\n")
        input("Press enter to get back to menu")
        display_options()

    if input_choice == "g":
        clear_screen()
        print("\n\nGEOGRAPHY TRIVIA\n\n")
        geography_questions = [
            ["Question 1: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 2: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 3: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"],
            ["Question 4: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "1"],
            ["Question 5: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "2"],
            ["Question 6: What....", "[1] Option 1", "[2] Option 2",
                "[3] Option 3\n", "3"]
        ]
        score = run_quiz(geography_questions)
        score_boards[2].update({username: score})
        sort_score_board(score_boards, 2)
        print("\nYou finished the GEOGRAPHY TRIVIA quiz! Well done!")
        print("Your score: {score}\n")
        input("Press enter to get back to menu")
        display_options()

    if input_choice == "v":
        clear_screen()
        print_score_board(score_boards[0], "SCIENCE TRIVIA  ")
        print_score_board(score_boards[1], "MOVIE TRIVIA    ")
        print_score_board(score_boards[2], "GEOGRAPHY TRIVIA")
        input("\n\nPress enter to get back to menu")
        display_options()

    if input_choice == "q":
        clear_screen()
        run_quit_game()


def run_quiz(questions):
    """
    When called this function prints questions in chosen quiz (first popping of
    the correct answer (index 4 in question list).
    """
    score = 0
    for question in questions:
        correct_answer = question.pop()
        print(f"Score: {score}\n")
        for item in question:
            print(item)
        option_valid = False
        while option_valid is False:
            player_answer = input("Enter your answer: ")
            option_valid = validate_choice(player_answer, ["1", "2", "3"])
        if correct_answer == player_answer:
            print("Correct! Well done!\n\n")
            score += 1
        else:
            print("Incorrect!\n\n")
    return score


def run_quit_game():
    """
    Shuts down game when player chooses quit option "q" in options menu.
    """
    print("\n\nHope you had fun! :)\n\n")
    print("Shutting down quiz...\n")
    delay(2)
    clear_screen()


def main():
    """
    Start the game by showing introduction, initiating function to ask
    for username and then display options menu.
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
    display_options()


main()
