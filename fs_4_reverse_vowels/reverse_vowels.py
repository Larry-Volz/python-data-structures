def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
   
#------------------------------------ MY SOLUTION -----------------------------------------------------------
#     vowels='aeiou'
#     rvs_s_dict = {}
# #Create a dictionary of characters and positions
#     s_dict = {chr:s.index(chr) for chr in s if chr.lower() in vowels}
#     print("s_dict", s_dict)

# #turn positions into a list, reverse, turn reverse-object back into a list
#     rvs_vals = list(reversed(list(s_dict.values())))
#     print("rvs_vals", rvs_vals)

# #put the list values back into a dictionary
# #Note: I had to assign values to keys, not the reverse.  You cannot redefine keys!
#     for i, key in enumerate(s_dict):
#         s_dict[key]= rvs_vals[i]
#     print("s_dict", s_dict)

#     new_string = ""
#     idx=0
# # Reverse k/v to make them v/k to look up by position instead of letter
#     invers_s_dict = {v:k for k,v in s_dict.items()}
#     print("invers_s_dict", invers_s_dict)

# # for each position in the string s
#     for idx, char in enumerate(s):
#     # is it a position in the invers_s_dict keys?
#         if idx in invers_s_dict.keys():
#         #if so then use the character at that position
#             new_string += invers_s_dict[idx]
#         #otherwise use character from that position in s
#         else:
#             new_string += s[idx]

#     print (new_string)
#     return new_string

# reverse_vowels("Reverse Vowels In A String")

#--------------------------------------------------- NOTES --------------------------------------------------------
# Very proud of this attempt in that I learned a couple of things:
# - you cannot reset the value of a key, only values
# - you can convert to a list, reverse and convert back again
# - you can use a comprehension + unpacking to reverse the keys and values in a dictionary
# - since each key is unique you CANNOT use a dictionary for this exercise because there are repeats of the same letters
# - just because my first instinct is to use arrays (lists) does NOT mean it's wrong.  lol.
# - the teacher's solution is BRILLIANT and simple.  It mimicks how we do it in our mind.  We look at one side and 
# then the other back and forth switching each one.  While loop with i moving from left and J moving from the right
# really really clever
#--------------------------------------------------------------------------------------------------------------------

#TEACHERS SOLUTION
vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)
