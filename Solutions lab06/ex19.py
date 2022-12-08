def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def cria_racional(num: int, den: int):
    if den == 0:
        raise ValueError("o denominador não pode ser 0")

    if not isinstance(num, int) or not isinstance(den, int):
        raise ValueError("os números devem ser inteiros")

    div_by = gcd(num, den)
    return {
        "n": num // div_by,
        "d": den // div_by
    }


def escreve_racional(num: dict):
    num = cria_racional(num["n"], num["d"])
    print(f"{num['n']}/{num['d']}")
    return


def soma_racionais(n1: dict, n2: dict):
    return cria_racional(
        n1["n"] * n2["d"] + n2["n"] * n1["d"],
        n1["d"] * n2["d"]
    )