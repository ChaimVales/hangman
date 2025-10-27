import hangman.game
def prompt_guess() -> str:
    ot = input("enter yout ot")
    if not ot.isalpha():
        print("Just a letter, not a number.")
        prompt_guess()
    if len(ot) > 1:
        print("Just one letter, no more.")
        prompt_guess()
    return ot

def print_status(state: dict) -> None:
    Display_word = hangman.game.render_display(state)
    Guessed_Taoisms = state["guessad"]
    Remaining_guesses = state["max_string"] - state["wrong_guesses"]
    print (f" Display_word {Display_word}  Guessed_Taoisms {Guessed_Taoisms} Remaining_guesses {Remaining_guesses}")
    return None

def print_result(state: dict) -> None:
    if hangman.game.is_won(state):
        print(f"win!!!!!!!!{state["secret"]}{state["guessad"]}")
    else:
        print(f"no!!!!!!!!{state["secret"]}{state["guessad"]}")
    return None




    