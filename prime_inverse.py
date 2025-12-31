def inverse_analyzer(n: int) -> tuple[list[int], list[int], int, int]:
    q_s: list[int] = []
    r_s: list[int] = []
    r = 1
    q, r = divmod(r * 10, n)
    iter = 0
    while r != 0 and r not in r_s:
        q_s.append(q)
        r_s.append(r)
        q, r = divmod(r * 10, n)
        iter += 1
        if iter > 2 * n + 1:
            print("iterations exceeded: ", iter, 2 * n + 1)
            break
    if r == 0:
        q_s.append(q)
        r_s.append(r)
        print("Finite decimal representation")
        print("Number of non-zero decimal digits", len(q_s))
    elif r in r_s:
        q_s.append(q)

    return q_s, r_s, r, iter


n = 7 * 40
q_s, r_s, r, iter = inverse_analyzer(n)

print("quotients: ", q_s)
print("residues: ", r_s)
print("last residue: ", r)
print("Number of iterations: ", iter)
