def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

    """
    #extract hobbies
    a_name, a_num_friends, a_hobbies = a
    b_name, b_num_friends, b_hobbies = b

    #make them into sets
    a_hobbies = set(a_hobbies)
    b_hobbies = set(b_hobbies)

    #return if (the intersection of hobbies for the two people)
    if a_hobbies & b_hobbies:
        return True
    return False
    
    #****TEACHER'S SOLUTION (simpler)
    # if set(a[2]) & set(b[2]):
    #     return True
    # else:
    #     return False

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print("False = ", friend_date(elmo, sauron))
print("True = ", friend_date(sauron, gandalf))