

# First Order Logic - Resolution

# Literal format: (negation, predicate, arguments)

def apply_substitution(term, substitution):
    while term in substitution:
        term = substitution[term]
    return term


def unify(args1, args2):
    substitution = {}

    for a, b in zip(args1, args2):
        a = apply_substitution(a, substitution)
        b = apply_substitution(b, substitution)

        if a != b:
            if a.islower() and len(a) == 1:
                substitution[a] = b
            elif b.islower() and len(b) == 1:
                substitution[b] = a
            else:
                return None

    return substitution


def substitute_literal(literal, substitution):
    neg, pred, args = literal

    new_args = tuple(
        apply_substitution(arg, substitution) for arg in args
    )

    return (neg, pred, new_args)


def resolve(clause1, clause2):
    for i, lit1 in enumerate(clause1):
        for j, lit2 in enumerate(clause2):

            neg1, pred1, args1 = lit1
            neg2, pred2, args2 = lit2

            # Check complementary literals
            if pred1 == pred2 and neg1 != neg2:

                theta = unify(args1, args2)

                if theta is not None:

                    remaining = clause1[:i] + clause1[i+1:]
                    remaining += clause2[:j] + clause2[j+1:]

                    result = tuple(
                        substitute_literal(lit, theta)
                        for lit in remaining
                    )

                    return result, theta

    return None, None


# Knowledge Base in CNF

C1 = ((True, "food", ("x",)),
      (False, "likes", ("John", "x")))

C2 = ((True, "eats", ("y", "z")),
      (False, "killed", ("y",)),
      (False, "food", ("z",)))

C3 = ((False, "eats", ("Anil", "Peanuts")),)

C4 = ((True, "alive", ("k",)),
      (True, "killed", ("k",)))

C5 = ((False, "alive", ("Anil",)),)

# Negated goal
Goal = ((True, "likes", ("John", "Peanuts")),)


# Display function
def show(clause):
    if len(clause) == 0:
        return "{}"

    result = []

    for neg, pred, args in clause:
        sign = "NOT " if neg else ""
        result.append(sign + pred + "(" + ",".join(args) + ")")

    return " OR ".join(result)


print("FIRST ORDER LOGIC - RESOLUTION")
print("--------------------------------")

# Step 1: Resolve goal with C1
r1, s1 = resolve(C1, Goal)
print("\nStep 1:", show(r1))
print("Substitution:", s1)

# Step 2: Resolve result with C2
r2, s2 = resolve(C2, C3)
print("\nStep 2:", show(r2))
print("Substitution:", s2)

# Step 3: Resolve Step 1 and Step 2
r3, s3 = resolve(r1, r2)
print("\nStep 3:", show(r3))
print("Substitution:", s3)

# Step 4: Resolve with C4
r4, s4 = resolve(C4, r3)
print("\nStep 4:", show(r4))
print("Substitution:", s4)

# Step 5: Resolve with C5
r5, s5 = resolve(r4, C5)
print("\nStep 5:", show(r5))
print("Substitution:", s5)

# Check final result
if r5 == ():
    print("\nEmpty clause {} obtained.")
    print("Hence, John likes Peanuts is PROVED.")
else:
    print("\nGoal could not be proved.")