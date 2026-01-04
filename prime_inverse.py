from unicodedata import decimal


def inverse_analyzer(n: int) -> tuple[list[int], list[int], int, int]:
    q_s: list[int] = []
    r_s: list[int] = []
    r = 1
    q, r = divmod(r * 10, n)
    iter = 1
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
    elif r in r_s:
        q_s.append(q)

    return q_s, r_s, r, iter


for n in range(2, 14):
    q_s, r_s, r, iter = inverse_analyzer(n)
    print(f"1/{n}")
    if r == 0:
        print("Finite decimal representation")
        decimal_representation = [str(i) for i in q_s]
        print(f"decimal representation 0.{''.join(decimal_representation)}")
        print(f"quotients: {q_s}")
        print(f"residues: {r_s}")
        print("last residue: ", r)
    else:
        print("Repeated pattern")
        decimal_representation = [str(i) for i in q_s]
        print(f"decimal representation 0.({''.join(decimal_representation)})")

    print(f"Compare to {1 / n}\n")
