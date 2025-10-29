import validate
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        if secret[i] in guess and secret[i] != guess[i]:
            cows += 1
    return bulls,cows

def is_won(bulls,length):
    return bulls == length

def init_state(secret: str, length: int, max_tries: int | None) -> dict:
    game_state = {
        "secret":secret,
        "length": length,
        "max_tries": max_tries,
        "tries_used": 0,
        "history": [],
        "seen": set()
    }
    return  game_state

def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    bulls = score_guess(state["secret"],guess)[0]
    cows = score_guess(state["secret"], guess)[1]
    state["tries_used"] += 1
    state["seen"].add(guess)
    state["history"].append((guess,cows,bulls))
    return bulls,cows

