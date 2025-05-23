def unit_propagate(formula):
    assignment = []
    unit_clauses = [c[0] for c in formula.clauses if len(c) == 1]
    while unit_clauses:
        lit = unit_clauses.pop()
        assignment.append(lit)
        formula = formula.simplify(lit)
        unit_clauses = [c[0] for c in formula.clauses if len(c) == 1]
    return formula, assignment
