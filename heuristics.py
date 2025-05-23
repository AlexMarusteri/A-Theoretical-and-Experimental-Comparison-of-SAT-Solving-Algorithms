def choose_literal(clauses):
    counts = {}
    for clause in clauses:
        for lit in clause:
            counts[lit] = counts.get(lit, 0) + 1
    return max(counts, key=counts.get)
