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
        if iter > n + 1:
            print("iteration: ", iter)
            break

    return q_s, r_s, r, iter


print(inverse_analyzer(213))
