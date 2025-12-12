def validate_guess(guess, word_length=5):
    if not isinstance(guess, str):
        return False
    if len(guess) != word_length:
        return False
    if not guess.isalpha():
        return False
    return guess.islower()


def check_guess(secret_word, guess):
    if len(secret_word) != len(guess):
        return []

    result = []
    secret_list = list(secret_word)
    guess_list = list(guess)

    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result.append((guess_list[i], 'green'))
            secret_list[i] = None
            guess_list[i] = None
        else:
            result.append((guess_list[i], None))

    for i in range(len(guess_list)):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                result[i] = (guess_list[i], 'yellow')
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (guess_list[i], 'gray')

    return result


def is_valid_word(word, word_list):
    return word.lower() in [w.lower() for w in word_list]


def calculate_game_score(guesses_used, max_guesses=6):
    if guesses_used <= 0 or guesses_used > max_guesses:
        return 0
    return max_guesses - guesses_used + 1
