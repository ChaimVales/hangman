import hangman.game
def prompt_guess() -> str:
    ot = input("enter yout ot")
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




    