def init_state(secret: str, max_tries: int) -> dict:
    display_list = "_" * len(secret)
    return {
                "secret":secret, #המילה הסודית
                "display":display_list,#רשימת תווים לתצוגה
                "guessad":[],#אותיות שנוחשו
                "wrong_guesses":0,#כמה טעויות בוצעו
                "max_string":max_tries# מגבלה
           }

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:

    if ch in guessed:
        return (False," in guessed")
    else:
        return (True,"no in guessed")
    

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state:
        return True
    return False

def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    return False


def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_string"]:
        return True
    return False

def render_display(state: dict) -> str:
    word = ""
    for i in range(len(state["secret"])):
        if state["secret"][i] in state[ "guessad"]:
            word += state["secret"][i]
        else:
            word += "_"
        state["display"] = word
    return word

def render_summary(state: dict) -> str:
    word = state["secret"]
    word += " "
    for i in state["guessad"]:
        if i in state["secret"]:
            word += i
    return word





