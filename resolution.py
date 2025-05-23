def resolve(c1, c2):
    for lit in c1:
        if -lit in c2:
            new_clause = list(set(c1 + c2))
            new_clause.remove(lit)
            new_clause.remove(-lit)
            return new_clause
    return None

def resolution_algorithm(formula):
    clauses = formula.clauses[:]
    new = set()
    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvent = resolve(clauses[i], clauses[j])
                if resolvent == []:
                    return True
                if resolvent and tuple(resolvent) not in new:
                    new.add(tuple(resolvent))
        if new.issubset(set(map(tuple, clauses))):
            return False
        clauses.extend([list(c) for c in new])
