def get_username():
    """
    Ask the player for a username
    """
    username = input("                  Please enter a username: ")
    validate_username(username)

    
def validate_username(data):
    """
    Validate username by checking that at least two characteres were entered.  
    """
    valid = True
    try:
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
    if valid is False:
        get_username()


def game_options():
    """
    Display options menu, to choose game or show score board
    """
    print("Choose a quiz or show the score board")
    print("-------------------------------------\n")
    print("[s] Trivia about Science")
    print("[m] Trivia about Movies")
    print("[g] Trivia about Geography")
    print("[v] View score board\n\n")
    choice = input("Enter your choice: ")


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
    #WANT TO START A NEW PAGE (REMOVE INTRO)
    game_options(choice)
    

main()
