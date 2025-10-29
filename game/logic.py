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
