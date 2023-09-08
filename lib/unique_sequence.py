def remove_duplicate(sequence):
    new_list = []
    seen = set()
    for item in sequence:
        if item not in seen:
            new_list.append(item)
            seen.add(item)

    return new_list        

#Test cases
input_sequence = [2, 3, 2, 4, 5, 3, 6, 8, 4, 7, 5]
print(remove_duplicate(input_sequence))
