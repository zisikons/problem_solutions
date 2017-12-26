def number_needed(a, b):

    # Letters counter
    counter = 0

    # For each letter in string a
    for l in a:
        # Case 1: The letter belongs to b as well
        if l in b:
            # Remove letter from b 
            b = b.replace(l,'',1)

        # Case 2: The letter belongs only to a in which case we simply
        #         increase the counter
        else:
            counter += 1

    # In the end, the letters left in b should be removed 
    # in order to have an anagram (explain better)
    counter += len(b)
    return counter

a = input().strip()
b = input().strip()

print(number_needed(a, b))
