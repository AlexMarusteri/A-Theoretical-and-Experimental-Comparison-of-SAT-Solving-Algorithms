class Formula:
    def __init__(self, clauses):
        self.clauses = clauses

    def is_satisfied(self, assignment):
        for clause in self.clauses:
            if not any(lit in assignment for lit in clause):
                return False
        return True

    def simplify(self, literal):
        new_clauses = []
        for clause in self.clauses:
            if literal in clause:
                continue
            new_clause = [lit for lit in clause if lit != -literal]
            new_clauses.append(new_clause)
        return Formula(new_clauses)
