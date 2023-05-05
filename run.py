import os
import time
from tabulate import tabulate as tb
from colorama import Fore, Style


class Player:
    """
    Class to create username variable that can be used in functions.
    """
    name = 0


score_boards = [
    {"Jenny": 10, "GameGuru": 7, "lulu": 7, "Carl": 6},
    {"lulu": 8, "GameGuru": 8, "Jenny": 7, "Carl": 4},
    {"Jenny": 9, "Carl": 5, "lulu": 4, "GameGuru": 4}]


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
    os.system("clear")


def get_username():
    """
    Ask the player for a username.
    """
    Player.name = input("Please enter a username: \n")
    validate_username(Player.name)


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
        print(Fore.MAGENTA)
        print("\n                           Lets play!\n\n")
        print(Style.RESET_ALL)
        delay(1.2)
    if valid is False:
        get_username()


def display_options():
    """
    Display options menu with options to choose a game or display score board.
    """
    clear_screen()
    print("\n\nChoose a quiz, show the score board menu or quit the game")
    print("-------------------------------------------------------------\n")

    options_list = [Fore.YELLOW + "[s] Trivia about Science",
                    Fore.MAGENTA + "[m] Trivia about Movies",
                    Fore.CYAN + "[g] Trivia about Geography",
                    Fore.GREEN + "[v] View score board",
                    Fore.RED + "[q] Quit\n\n"]
    for option in options_list:
        print(option)
    choose_option()


def choose_option():
    """
    Asking player to choose an option from the options menu.
    """
    print(Style.RESET_ALL)
    player_choice = input("Enter your choice: \n")
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
        print(Fore.RED)
        print(f"\n\nInvalid choice. Enter {new_options} to make a choice.")
        print(Style.RESET_ALL)
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


def display_score_menu():
    """
    Asking player to choose a score board to be displayed.
    """
    print(Style.RESET_ALL)
    clear_screen()
    print("\n\nScore menu")
    print("----------\n")
    print("which score board do you want to see?\n")
    options_list = [Fore.YELLOW + "[s] Science score board",
                    Fore.MAGENTA + "[m] Movies score board",
                    Fore.CYAN + "[g] Geography score board",
                    Fore.RED + "[b] Back to quiz menu\n\n"]
    print(Style.RESET_ALL)

    for option in options_list:
        print(option)
    choose_score_board()


def choose_score_board():
    """
    """
    player_choice = input("Enter your choice: \n")
    if validate_choice(player_choice, ["s", "m", "g", "b"]) is True:
        clear_screen()
        run_score_board(player_choice)
    else:
        choose_score_board()


def run_score_board(input_choice):
    """
    """
    input_choice = input_choice.lower()

    if input_choice == "s":
        print_score_board(score_boards[0], Fore.YELLOW + "\n\nSCIENCE TRIVIA")
        print(Style.RESET_ALL)
        input("\n\nPress enter to get back to score menu\n")
        clear_screen()
        display_score_menu()
    if input_choice == "m":
        print_score_board(score_boards[1], Fore.MAGENTA + "\n\nMOVIE TRIVIA")
        print(Style.RESET_ALL)
        input("\n\nPress enter to get back to score menu\n")
        clear_screen()
        display_score_menu()
    if input_choice == "g":
        print_score_board(score_boards[2], Fore.CYAN + "\n\nGEOGRAPHY TRIVIA")
        print(Style.RESET_ALL)
        input("\n\nPress enter to get back to score menu\n")
        clear_screen()
        display_score_menu()
    if input_choice == "b":
        print(Style.RESET_ALL)
        clear_screen()
        display_options()


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
        print(Fore.YELLOW + "\n\nSCIENCE TRIVIA\n\n")
        print(Style.RESET_ALL)
        # The last item in each nested list of questions is the correct answer
        # for that question. It´s the same for all the quizes
        # (i.e. choices "s", "m", "g").
        science_questions = [
            ["Question 1: What color is the sunset on Mars?", "[1] Yellow",
                "[2] Red", "[3] Blue\n", "3"],
            ["Question 2: What is the largest organ in the human body?",
                "[1] Brain", "[2] Skin", "[3] Liver\n", "2"],
            ["Question 3: How many elements does the periodic table contain?",
                "[1] 101", "[2] 118", "[3] 89\n", "2"],
            ["Question 4: What is the world's most poisonous spider?",
                "[1] Brown recluse", "[2] Sydney funnel spider",
                "[3] Brazilian wandering spider\n", "3"],
            ["Question 5: What metal is the best conductor of electricity?",
                "[1] Silver", "[2] Gold", "[3] Copper\n", "1"],
            ["Question 6: What is the black hole in the Milky Way called?",
                "[1] Gemini B*", "[2] Sagittarius A*",
                "[3] Capricorn C*\n", "2"],
            ["Question 7: What is the fastest animal in the world?",
                "[1] Peregrine Falcon", "[2] Cheetah",
                "[3] American Antelope\n", "1"],
            ["Question 8: Which hormone is often called the 'love hormone'?",
                "[1] Oxytocin", "[2] Oestrogen", "[3] Serotonin\n", "1"]
        ]
        score = run_quiz(science_questions)
        score_boards[0].update({Player.name: score})
        sort_score_board(score_boards, 0)
        print(Fore.YELLOW + "\nYou finished the SCIENCE TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_options()

    if input_choice == "m":
        clear_screen()
        print(Fore.MAGENTA + "\n\nMOVIE TRIVIA\n\n")
        print(Style.RESET_ALL)
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
        score_boards[1].update({Player.name: score})
        sort_score_board(score_boards, 1)
        print(Fore.MAGENTA + "\nYou finished the MOVIE TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_options()

    if input_choice == "g":
        clear_screen()
        print(Fore.CYAN + "\n\nGEOGRAPHY TRIVIA\n\n")
        print(Style.RESET_ALL)
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
        score_boards[2].update({Player.name: score})
        sort_score_board(score_boards, 2)
        print(Fore.CYAN + "\nYou finished the GEOGRAPHY TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_options()

    if input_choice == "v":
        clear_screen()
        display_score_menu()

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
            player_answer = input("Enter your answer: \n")
            option_valid = validate_choice(player_answer, ["1", "2", "3"])
        if correct_answer == player_answer:
            print(Fore.GREEN + "CORRECT! Well done!\n\n")
            print(Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "INCORRECT.\n\n")
            print(Style.RESET_ALL)
    return score


def run_quit_game():
    """
    Shuts down game when player chooses quit option "q" in options menu.
    """
    print(Fore.GREEN + "\n\nHope you had fun! :)\n\n")
    print(Style.RESET_ALL)
    print("Shutting down quiz...\n")
    delay(3)
    clear_screen()


def main():
    """
    Start the game by showing introduction, initiating function to ask
    for username and then display options menu.
    """
    print(Fore.GREEN)
    print("\n\nTTTTTTTTTT   RRRR    IIIIII  VV       VV  IIIIII       AAA")
    print("    TT       R   R     II     VV     VV     II        AA AA")
    print("    TT       R  R      II      VV   VV      II       AA   AA")
    print("    TT       RRR       II       VV VV       II      AAAAAAAAA")
    print("    TT       R  R      II        VVV        II     AA       AA")
    print("    TT       R   R   IIIIII       V       IIIIII  AA         AA\n")
    print("----------------------------------------------------------------")
    print(Fore.YELLOW)
    print("    Did you know that shrimp have their hearts in their heads?    ")
    print("                        Want to learn more?                       ")
    print("             Test your trivia knowledge with a quiz!              ")
    print(Fore.GREEN)
    print("------------------------------------------------------------------")
    print(Style.RESET_ALL)
    get_username()
    display_options()


main()
