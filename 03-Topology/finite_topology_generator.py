# MathCore-PK | Finite Topology Generator from A_p
# Based on Neighbourhood System N1-N4
# Author: Mathcore-PK (Peshawar)

def generate_topology(X, A_p):
    """
    X = set of points e.g., {1,2,3}
    A_p = dictionary of neighbourhood bases, e.g., {1: [{1}, {1,2}], 2: [{2}]}
    """
    print(f"X = {X}")
    print(f"A_p = {A_p}")

    # For each p, K({p}) = intersection of all N in A_p
    K_single = {}
    for p in X:
        if p in A_p and A_p[p]:
            # intersection of neighbourhoods
            inter = set.intersection(*[set(s) for s in A_p[p]])
            K_single[p] = inter
        else:
            K_single[p] = {p}

    print(f"K(p) for each p: {K_single}")

    # Simple topology generation: tau = {X - K(A) complement logic}
    # For teaching purpose - generates all supersets of K(p)
    topology = [set()]
    topology.append(set(X))

    for p, k in K_single.items():
        if k not in topology:
            topology.append(k)

    # Add unions
    topology.append(set(X)) # ensure X is there

    print("\nGenerated Topology (basic):")
    for t in topology:
        print(t)
    return topology

# --- Example for Undergraduate Students ---
if __name__ == "__main__":
    # Example: X = {1,2,3}, A_1={{1},{1,2}}, A_2={{2}}, A_3={{3},{2,3}}
    X = {1,2,3}
    A_p = {
        1: [{1}, {1,2}],
        2: [{2}],
        3: [{3}, {2,3}]
    }
    generate_topology(X, A_p)
