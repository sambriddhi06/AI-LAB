

# First Order Logic using Forward Chaining

# Step 1: Initialize Knowledge Base
KB = {
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
}

# Step 2: Forward Chaining
def forward_chaining(KB):

    new_fact = True

    while new_fact:
        new_fact = False
        new_facts = set()

        # Rule 1: Missile(x) -> Weapon(x)
        for fact in KB:
            if fact[0] == "Missile":
                x = fact[1]
                new_facts.add(("Weapon", x))

        # Rule 2: Missile(x) AND Owns(A,x)
        # -> Sells(Robert,x,A)
        for m in KB:
            if m[0] == "Missile":
                x = m[1]

                if ("Owns", "A", x) in KB:
                    new_facts.add(
                        ("Sells", "Robert", x, "A")
                    )

        # Rule 3: Enemy(x,America) -> Hostile(x)
        for fact in KB:
            if fact[0] == "Enemy":
                x = fact[1]

                if fact[2] == "America":
                    new_facts.add(("Hostile", x))

        # Rule 4: American(p) AND Weapon(q)
        # AND Sells(p,q,r) AND Hostile(r)
        # -> Criminal(p)

        for a in KB:
            if a[0] == "American":
                p = a[1]

                for w in KB:
                    if w[0] == "Weapon":
                        q = w[1]

                        for s in KB:
                            if s[0] == "Sells":
                                seller, item, country = s[1:]

                                if seller == p and item == q:
                                    if ("Hostile", country) in KB:
                                        new_facts.add(
                                            ("Criminal", p)
                                        )

        # Add newly inferred facts
        for fact in new_facts:
            if fact not in KB:
                print("New fact:", fact)
                KB.add(fact)
                new_fact = True

    return KB


# Step 3: Execute Forward Chaining
KB = forward_chaining(KB)

# Step 4: Check the query
query = ("Criminal", "Robert")

if query in KB:
    print("\nGoal proved: Robert is Criminal")
else:
    print("\nGoal cannot be proved")


# Display final Knowledge Base
print("\nFinal Knowledge Base:")
for fact in sorted(KB):
    print(fact)

