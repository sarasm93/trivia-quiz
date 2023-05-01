def get_username():
    """
    Ask the player for a username
    """
    username = input("                  Please enter a username: ")
    validate_username(username)


def validate_username(data):
    """
    Validate username by checking that minimum two and maximum 10
    characteres were entered.
    """
    valid = True

    try:
        for blank in data:
            if (blank.isspace()) == True:
                raise ValueError(
                    " It cannot contain blank spaces")
        if len(data) == 0:
            raise ValueError(
                " You didn't enter a username")
        if len(data) < 2:
            raise ValueError(
                " It needs to be at least 2 characters")
        if len(data) > 10:
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


def choose_game():
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
    validate_game(player_choice)


def validate_game(data):
    """
    Function to run a game or show the score board, based on 
    the choice of the user.
    """
    option_one = "s"
    option_two = "m"
    option_three = "g"
    option_four = "v"
    
    try:
        if data in (option_one, option_two, option_three, option_four): 
            games()
        else:
            raise ValueError()
    except ValueError:
        print("\nInvalid choice. Enter s, m, g or v to make a choice.")
        input("Press enter to choose again.")
        choose_game()

    



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
    choose_game()
    

main()