def get_username():
    """
    Ask the player for a username
    """
    username = input("Please enter a username: ")
    validate_username(username)

    
def validate_username(data):
    """
    Validate username by checking that at least two characteres were entered.  
    """
    valid = True
    try:
        if len(data) == 0:
            raise ValueError(
                "You need to enter a username")
        if len(data) < 2:
            raise ValueError(
                "The username needs to be at least two characters long")
    except ValueError as e:
        print(f"\nInvalid data: {e}. Please try again.") 
        valid = False
    
    if valid:
        print("Valid username")
    if valid is False:
        get_username()


def main():
    """
    Run all functions
    """
    print("\nTTTTTTTTTT   RRRR    IIIIII  VV       VV  IIIIII       AAA")
    print("    TT       R   R     II     VV     VV     II        AA AA")
    print("    TT       R  R      II      VV   VV      II       AA   AA")
    print("    TT       RRR       II       VV VV       II      AAAAAAAAA")
    print("    TT       R  R      II        VVV        II     AA       AA")
    print("    TT       R   R   IIIIII       V       IIIIII  AA         AA\n")

    print("Did you know that ......\n")
    print("                       Want to learn more?                      ")
    print("          Test your trivia knowledge with a quiz game!          ")
    print("----------------------------------------------------------------\n")

    get_username()
    #game_options()
    

main()
