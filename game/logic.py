def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        if secret[i] in guess and secret[i] != guess[i]:
            cows += 1
    return bulls,cows

def is_wom(bulls,length):
    return bulls == length

def init_state(secret: str, length: int, max_tries: int | None) -> dict:
    game_state = {
        "secret":secret,
        "length": length,
        "max_tries": max_tries,
        "tries_used": int,
        "history": list[tuple[str, int, int]],
        "seen": set[str]
    }
    return  game_state


