from unicodedata import decimal


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
    elif r in r_s:
        q_s.append(q)

    return q_s, r_s, r, iter


for n in range(2, 14):
    q_s, r_s, r, iter = inverse_analyzer(n)
    print(n)
    if r == 0:
        print(f"finite decimal representation")
        print(f"number of digits = {len(r_s)}")
    print(f"quotients: {q_s}")
    print(f"residues: {r_s}")
    print("last residue: ", r)
    print("Number of iterations: ", iter)
    print(q_s)
    decimal_representation = [str(i) for i in q_s]
    print("repeated pattern", decimal_representation)
    print(f"Compare to {1 / n}\n")
