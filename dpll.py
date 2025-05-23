def dpll(formula, assignment=[]):
    if not formula.clauses:
        return True, assignment
    if [] in formula.clauses:
        return False, []
    literal = next(iter(formula.clauses[0]))
    sat, result = dpll(formula.simplify(literal), assignment + [literal])
    if sat:
        return True, result
    return dpll(formula.simplify(-literal), assignment + [-literal])
