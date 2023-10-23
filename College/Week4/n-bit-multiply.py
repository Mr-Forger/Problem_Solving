def product(a, b, n):
    if n == 1:
        return a * b

    a0, a1 = a >> (n // 2), a & ((1 << (n // 2)) - 1)
    b0, b1 = b >> (n // 2), b & ((1 << (n // 2)) - 1)

    p1 = product(a0, b0, n // 2)
    p2 = product(a1, b1, n // 2)
    p3 = product(a0, b1, n // 2)
    p4 = product(a1, b0, n // 2)

    return (p1 << (2 * (n // 2))) + ((p3 + p4) << (n // 2)) + p2


print(product(12, 12, 4))
