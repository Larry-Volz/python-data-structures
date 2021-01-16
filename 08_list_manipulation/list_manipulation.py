

def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed



    add: add item at beginning/end, and return list

 ACCORDING TO TEACHER - ANOTHER SOLUTION:
 if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    """


    if command == "remove":
        if location == "beginning":
            return lst[0:1]

        elif location == "end":
            return lst[:-2:-1]

        else:
            return None

    elif command == "add":
        #add
        if location == "beginning":
            lst.insert(0, value)

        elif location == "end":
            lst.append(value)

        else:
            return None

    else:
        return None

    return None
            
lst = [1, 2, 3]

print("add/end 30 = [1,2,3,30]?")
print(list_manipulation(lst, 'add', 'end', 30))

lst = []
lst = [1, 2, 3]

print("add/beginning 20 = [20, 1, 2, 3]?")
print(list_manipulation( lst, 'add', 'beginning', 20))

lst = []
lst = [1, 2, 3]

print("remove/end 3 = 3 ?")
print(list_manipulation( lst, 'remove', 'end'))

lst = []
lst = [1, 2, 3]

print("remove/beginning =1 ?")
print(list_manipulation(lst, 'remove', 'beginning'))

lst = []
lst = [1, 2, 3]

print(list_manipulation(lst, 'remove', 'dude'))