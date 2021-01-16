def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        
    """
    whole_names = []
    

    for person in people:
        whole_names.append(person['first']+" "+person['last'])
    return whole_names

#TEACHER'S SOLUTION:
#return [f"{person['first']} {person['last']}" for person in people]

names = [
     {'first': 'Ada', 'last': 'Lovelace'},
     {'first': 'Grace', 'last': 'Hopper'},
     ]

print("['Ada Lovelace', 'Grace Hopper']=", extract_full_names(names))