def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return phrase.title()

print("This Is Awesome = ", titleize('this is awesome'))
print("Only Capitalize First = ", titleize('oNLy cAPITALIZe fIRSt'))
