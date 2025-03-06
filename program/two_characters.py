def alternate(s):
    unique = list(set(s))  
    max_length = 0  
    
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            char1 = unique[i]
            char2 = unique[j]

            filtered = []
            for char in s:
                if char == char1 or char == char2:
                    filtered.append(char)

            is_alternate = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    is_alternate = False
                    break  
                
            if is_alternate:
                max_length = max(max_length, len(filtered))

    return max_length 

print()
