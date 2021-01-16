def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    phrase = phrase.lower()
    return {ltr : phrase.count(ltr) for ltr in phrase if ltr in vowels}
    # counter = {}
    # for ltr in phrase:
    #     if ltr in vowels:
    #         #counter[ltr] = current VALUE of counter[ltr] + 1
    #         counter[ltr]= counter.get(ltr, 0) + 1


print("{'i': 1, 'o': 2} = ", vowel_count('rithm school'))
print("{'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1} = ", vowel_count('HOW ARE YOU? i am great!'))