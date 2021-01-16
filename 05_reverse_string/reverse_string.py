def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    word_to_lst = list(phrase)
    word_to_lst.reverse()
    ret = "".join(word_to_lst)
    return ret
    
print(reverse_string('awesome'))
print(reverse_string('sauce'))

# worked but teacher just did this:  return phrase[::-1] <- worth remembering!