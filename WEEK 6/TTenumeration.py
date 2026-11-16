from itertools import product

def implies(a, b):
    return (not a) or b

def tf(value):
    return "T" if value else "F"

def evaluate_kb(P, Q, R):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R

    kb = s1 and s2 and s3

    return s1, s2, s3, kb

def tt_entails(query):
    for values in product([False, True], repeat=3):
        model = dict(zip(["P", "Q", "R"], values))

        if evaluate_kb(**model)[3] and not query(model):
            return False

    return True

print("\n              TRUTH TABLE ENUMERATION")
print("=" * 75)

print(f"{'P':^5} {'Q':^5} {'R':^5} | "
      f"{'Q->P':^7} {'P->~Q':^7} {'Q|R':^7} | "
      f"{'AND (KB)':^10}")

print("-" * 75)

for P, Q, R in product([False, True], repeat=3):

    s1, s2, s3, kb = evaluate_kb(P, Q, R)

    print(f"{tf(P):^5} {tf(Q):^5} {tf(R):^5} | "
          f"{tf(s1):^7} {tf(s2):^7} {tf(s3):^7} | "
          f"{tf(kb):^10}")

print("-" * 75)

print("\n              ENTAILMENT RESULTS")
print("=" * 45)

print("KB entails R       :", tf(tt_entails(lambda m: m["R"])))

print("KB entails R -> P  :", tf(tt_entails(lambda m: implies(m["R"], m["P"]))))

print("KB entails Q -> R  :", tf(tt_entails(lambda m: implies(m["Q"], m["R"]))))

print("=" * 45)
