import logic
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


def print_status(state) -> None:

        print("length:",state["length"],"\n"
        "max_tries:",state["max_tries"],"\n"
        "tries_used:",state["tries_used"],"\n"
        "history:",state["history"],"\n"
        "seen:",state["seen"])





