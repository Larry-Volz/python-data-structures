def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    #convert each to str
    freq1={}
    freq2={}
    num_str1 = str(num1)
    num_str2 = str(num2)
    # for ea in str's use count(eat)
    for char in num_str1:
        freq1[char]= freq1.get(char, 0) + 1
    for chr in num_str2:
        freq2[chr]= freq2.get(chr, 0) + 1
    return freq1 == freq2

    #compare strA with strB