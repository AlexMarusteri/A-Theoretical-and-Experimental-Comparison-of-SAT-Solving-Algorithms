def dp(formula):
    if not formula.clauses:
        return True
    if [] in formula.clauses:
        return False
    literal = next(iter(formula.clauses[0]))
    return dp(formula.simplify(literal)) or dp(formula.simplify(-literal))
