def prompt_guess(length):
    while True:
        guess = input("enter your number: ")
        if not guess.isdigit():
            print("please only numbers")
            continue
        if len(guess) != length:
            print("the length of the number is not correct")
            continue
        return guess



