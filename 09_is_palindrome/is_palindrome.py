
def is_palindrome(phrase):

    phrase2 = phrase[::-1]
    if phrase.strip().lower == phrase2.strip().lower:
        return True
    return False

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

    TEACHERS SOLUTION:
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]
        
    """

print(is_palindrome('tacocat'))
print("tacocat=True")
print(is_palindrome('noon'))
print("noon = True")
print(is_palindrome('robert'))
print("robert = False")
print(is_palindrome('taco cat'))
print("'taco cat' = True")
print(is_palindrome('Noon'))
print("'Noon' = True")