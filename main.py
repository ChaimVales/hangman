import hangman.game
import hangman.words
import hangman.io

import random

def play(words: list[str], max_tries: int = 6) -> None:
    word = random.randint(0,len(words)-1)
    state_dict = hangman.game.init_state(words[word],max_tries)

    for j in range(max_tries):
        ot = hangman.io.prompt_guess()


        if ot in state_dict["guessad"]:
            state_dict["wrong_guesses"] += 1
            guess = hangman.game.validate_guess(ot,state_dict["guessad"])
            print(guess)
        elif hangman.game.apply_guess(state_dict,ot) == True:

            guess = hangman.game.validate_guess(ot,state_dict["guessad"])
            print(guess)
            state_dict["guessad"].append(ot)
        else:
            state_dict["wrong_guesses"] += 1

            guess = hangman.game.validate_guess(ot,state_dict["guessad"])
            print(guess)
            state_dict["guessad"].append(ot) 
        print(hangman.game.render_display(state_dict))
        
        hangman.io.print_status(state_dict)
        if  hangman.game.is_won(state_dict):
            break
        print(state_dict["display"])
        

    hangman.game.render_summary(state_dict)
    hangman.io.print_result(state_dict)



if __name__ == "__main__":
    play(hangman.words.this_word())
    


