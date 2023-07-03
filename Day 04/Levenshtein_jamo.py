def levenshtein_jamo(jamo1, jamo2):
    if jamo1 == jamo2:
        return 0
    if len(jamo1) < len(jamo2):
        return levenshtein_jamo(jamo1, jamo2)
    elif len(jamo1) == 0:
        return len(jamo2)
    elif len(jamo2) == 0:
        return len(jamo1)
    
    previous_row = range(len(jamo2) + 1)
    for i, c1 in enumerate(jamo1):
        current_row = [i+1]
        for j, c2 in enumerate(jamo2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]