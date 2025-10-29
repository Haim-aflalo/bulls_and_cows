import random
def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None = None) -> str:
    secret_word = ""
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    while length:
        num =  random.choice(nums)
        if num not in  secret_word:
            secret_word += num
            length -= 1
    return secret_word


