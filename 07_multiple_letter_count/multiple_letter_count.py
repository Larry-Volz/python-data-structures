def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    return {char : phrase.count(char) for char in phrase}

    #or from teache's solution
    #for ltr in phrase:
        #counter[ltr] = counter.get(ltr, 0) + 1

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))
print(multiple_letter_count('necronomicon'))