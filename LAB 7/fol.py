

variables = {"x", "y", "z"}

def is_variable(term):
    return isinstance(term, str) and term in variables

def apply_substitution(term, subs):
    if is_variable(term):
        if term in subs:
            return apply_substitution(subs[term], subs)
        return term

    if isinstance(term, tuple):
        return tuple(apply_substitution(t, subs) for t in term)

    return term

def occurs(variable, term, subs):
    term = apply_substitution(term, subs)

    if variable == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(variable, t, subs) for t in term)

    return False

def unify(x, y, subs):
    x = apply_substitution(x, subs)
    y = apply_substitution(y, subs)

    if x == y:
        return subs

    if is_variable(x):
        if occurs(x, y, subs):
            return None
        subs[x] = y
        return subs

    if is_variable(y):
        if occurs(y, x, subs):
            return None
        subs[y] = x
        return subs

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            subs = unify(a, b, subs)

            if subs is None:
                return None

        return subs

    return None

expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

result = unify(expr1, expr2, {})

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)
    print("Unified Expression:", apply_substitution(expr1, result))

