import random
def choose_secret_word(words: list[str]) -> str:
    num_random = random.randint(0,len(words)-1)
    return words[num_random]
