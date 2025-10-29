def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    if len(guess) == length:
        return False,"len under the requirement"
    if guess.isdigit():
        return True,"only numbers"
    else:
        return False,"not only numbers in secret"



