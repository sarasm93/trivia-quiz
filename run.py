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
    {"Jenny": 8, "GameGuru": 5, "lulu": 5, "Carl": 4},
    {"lulu": 6, "GameGuru": 6, "Jenny": 5, "Carl": 2},
    {"Jenny": 7, "Carl": 3, "lulu": 2, "GameGuru": 2}]


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
    # The code on line 36 is taken from this Stackoverflow page.
    # https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
    os.system("clear")


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
        print(Fore.RED)
        print(f"\n     Invalid username: {e}.")
        print("                        Please try again.\n")
        print(Style.RESET_ALL)
        valid = False

    if valid:
        print(Fore.MAGENTA)
        print("\n                           Lets play!\n\n")
        print(Style.RESET_ALL)
        delay(1.2)
    if valid is False:
        get_username()


def get_username():
    """
    Ask the player for a username.
    """
    Player.name = input("Please enter a username: \n")
    validate_username(Player.name)


def display_quiz_options():
    """
    Display quiz menu with options to choose a game, display
    score board menu or quit game.
    """
    clear_screen()
    print("\n\n                        Quiz menu                        ")
    print("------------------------------------------------------------\n")
    print("Choose a quiz, show the score board menu or quit the game\n")
    print("Remember - the last score you got in a quiz is the one saved")
    print("           to the score board\n\n")

    options_list = [Fore.YELLOW + "[s] Trivia about Science",
                    Fore.MAGENTA + "[m] Trivia about Movies",
                    Fore.CYAN + "[g] Trivia about Geography",
                    Fore.GREEN + "[v] View score board menu",
                    Fore.RED + "[q] Quit\n\n"]
    for option in options_list:
        print(option)
    choose_option()


def validate_choice(input_choice, options):
    """
    Function to validate player choice. To make the valid options print nicely
    to the player, the valid options list is re-designed by (1) splitting it,
    (2) adding "or" to the second to last position, (3) putting it back
    together again and (4) removing all '[]' and ','.
    """
    # Code on line 138-142 is taken from the below Geeksforgeeks.org page.
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
        print(f"Invalid choice. Enter {new_options} to make a choice.")
        print(Style.RESET_ALL)
        return False


def choose_option():
    """
    Asking player to choose an option from the quiz menu.
    """
    print(Style.RESET_ALL)
    player_choice = input("Enter your choice: \n")
    if validate_choice(player_choice, ["s", "m", "g", "v", "q"]) is True:
        clear_screen()
        run_option(player_choice)
    else:
        choose_option()


def sort_score_board(input_board, list_index):
    """
    Function sorting dictionary of scores in score board each time a player
    finishes a quiz. Only the dictionary for the quiz that the player just
    played is sorted.
    """
    # Code on line 167-172 is taken from the below page to loop through
    # a dictionary of scores. The code has been adjusted to fit to this
    # program by changing variable names and by adding "reverse=True)"
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
    Display score board menu with options to choose a score board
    or get back to quiz menu.
    """
    print(Style.RESET_ALL)
    clear_screen()
    print("\n\n              Score menu             ")
    print("-------------------------------------\n")
    print("which score board do you want to see?\n")
    options_list = [Fore.YELLOW + "[s] Science score board",
                    Fore.MAGENTA + "[m] Movies score board",
                    Fore.CYAN + "[g] Geography score board",
                    Fore.RED + "[b] Back to quiz menu\n\n"]

    for option in options_list:
        print(option)
    choose_score_board()


def print_score_board(input_board, title):
    """
    When player chooses option "v" in options menu, this function is run to
    show the score board for each quiz in a table.
    """
    headers = [f"{title}", "\n\nPlayer    ", "\n\nScore"]
    scores_as_list = [headers]
    for key in input_board.keys():
        player_data = ["", key, input_board[key]]
        scores_as_list.append(player_data)
    table = tb(scores_as_list, headers="firstrow")
    print(f"{table}\n\n")


def run_score_board(input_choice):
    """
    Initiate the right score board or get back to score board menu, based
    on valid choice by player.
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
        display_quiz_options()


def choose_score_board():
    """
    Asking player to choose an option from the score board menu.
    """
    print(Style.RESET_ALL)
    player_choice = input("Enter your choice: \n")
    if validate_choice(player_choice, ["s", "m", "g", "b"]) is True:
        clear_screen()
        run_score_board(player_choice)
    else:
        choose_score_board()


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


def run_option(input_choice):
    """
    Initiate the right quiz, show score board menu or quit game, based
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
            ["QUESTION 1: What color is the sunset on Mars?", "[1] Yellow",
                "[2] Red", "[3] Blue\n", "3"],
            ["QUESTION 2: What is the largest organ in the human body?",
                "[1] Brain", "[2] Skin", "[3] Liver\n", "2"],
            ["QUESTION 3: How many elements does the periodic table contain?",
                "[1] 101", "[2] 118", "[3] 89\n", "2"],
            ["QUESTION 4: What is the world's most poisonous spider?",
                "[1] Brown recluse", "[2] Sydney funnel spider",
                "[3] Brazilian wandering spider\n", "3"],
            ["QUESTION 5: What metal is the best conductor of electricity?",
                "[1] Silver", "[2] Gold", "[3] Copper\n", "1"],
            ["QUESTION 6: What is the black hole in the Milky Way called?",
                "[1] Gemini B*", "[2] Sagittarius A*",
                "[3] Capricorn C*\n", "2"],
            ["QUESTION 7: What is the fastest animal in the world?",
                "[1] Peregrine Falcon", "[2] Cheetah",
                "[3] American Antelope\n", "1"],
            ["QUESTION 8: Which hormone is often called the 'love hormone'?",
                "[1] Oxytocin", "[2] Oestrogen", "[3] Serotonin\n", "1"]
        ]
        score = run_quiz(science_questions)
        score_boards[0].update({Player.name: score})
        sort_score_board(score_boards, 0)
        print(Fore.YELLOW + "\nYou finished the SCIENCE TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_quiz_options()

    if input_choice == "m":
        clear_screen()
        print(Fore.MAGENTA + "\n\nMOVIE TRIVIA\n\n")
        print(Style.RESET_ALL)
        movie_questions = [
            ["QUESTION 1: In which fictional place does Frozen take place?",
                "[1] Haven", "[2] Arendelle", "[3] Winterfell\n", "2"],
            ["QUESTION 2: What was the first James Bond movie ever made?",
                "[1] Thunderball", "[2] Dr. No", "[3] Goldfinger\n", "2"],
            ["QUESTION 3: How many Pixar animated films have been released?",
                "[1] 18", "[2] 36", "[3] 26\n", "3"],
            ["QUESTION 4: When did the Lion King premiere?",
                "[1] 1997", "[2] 1994", "[3] 1989\n", "2"],
            ["QUESTION 5: IThe code in Matrix comes from what food recipes?",
                "[1] Sushi", "[2] Dumplings", "[3] Pad thai\n", "1"],
            ["QUESTION 6: How many Oscars has Meryl Streep won?",
                "[1] 1", "[2] 2", "[3] 3\n", "3"],
            ["QUESTION 7: What item is in every Fight Club scene?",
                "[1] A Coca-Cola can", "[2] A Starbucks cup",
                "[3] A Dunkin' donut\n", "2"],
            ["QUESTION 8: What is the highest-grossing movie of all time?",
                "[1] Avatar", "[2] Titanic",
                "[3] Star Wars: The Force Awakens\n", "1"]
        ]
        score = run_quiz(movie_questions)
        score_boards[1].update({Player.name: score})
        sort_score_board(score_boards, 1)
        print(Fore.MAGENTA + "\nYou finished the MOVIE TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_quiz_options()

    if input_choice == "g":
        clear_screen()
        print(Fore.CYAN + "\n\nGEOGRAPHY TRIVIA\n\n")
        print(Style.RESET_ALL)
        geography_questions = [
            ["QUESTION 1: What is Earth's largest continent?",
                "[1] Asia", "[2] Africa", "[3] Antarctica\n", "1"],
            ["QUESTION 2: What is the highest waterfall in Europe?",
                "[1] Kjelfossen", "[2] Krimml", "[3] Triberg\n", "2"],
            ["QUESTION 3: What is the smallest country in South America?",
                "[1] Bolivia", "[2] Guyana", "[3] Suriname\n", "3"],
            ["QUESTION 4: What US state is home to Yellowstone National Park?",
                "[1] Utah", "[2] Wyoming", "[3] Colorado\n", "2"],
            ["QUESTION 5: Which African nation has the most pyramids?",
                "[1] Algeria", "[2] Egypt", "[3] Sudan\n", "3"],
            ["QUESTION 6: What country has the most coastline?",
                "[1] Canada", "[2] United States", "[3] Indonesia\n", "1"],
            ["QUESTION 7: What European country is home to Transylvania?",
                "[1] Romania", "[2] Slovania", "[3] Bulgaria\n", "1"],
            ["QUESTION 8: What is America's largest city by surface area?",
                "[1] Los Angeles", "[2] Yakuta", "[3] New York\n", "2"]
        ]
        score = run_quiz(geography_questions)
        score_boards[2].update({Player.name: score})
        sort_score_board(score_boards, 2)
        print(Fore.CYAN + "\nYou finished the GEOGRAPHY TRIVIA quiz!")
        print(f"Well done! Your score: {score}\n")
        print(Style.RESET_ALL)
        input("Press enter to get back to menu\n")
        display_quiz_options()

    if input_choice == "v":
        clear_screen()
        display_score_menu()

    if input_choice == "q":
        clear_screen()
        run_quit_game()


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
    display_quiz_options()


if __name__ == '__main__':
    main()
