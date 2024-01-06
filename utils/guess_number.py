from random import randint

# A small puzzle to show how randint works

# Returns a tuple that contains:
# * boolean variable, true if succeded, false if not
# * integer variable, contains the answer
def guess_random_number(range: int, guess_limit: int) -> tuple:
    # randint() as the name says, randomly picks an integer number
    # between a defined range
    secret_number = randint(1, range)
    print(f"""Lets guess a number, you have {guess_limit} attempts and \
        the range is from 1 to {range}"""
    )
    attempt = 0
    while attempt < guess_limit:
        attempt += 1
        guess = int(input(f"Guess N°{attempt}: "))
        if guess == secret_number:
            return True, secret_number
    else:
        return False, secret_number


