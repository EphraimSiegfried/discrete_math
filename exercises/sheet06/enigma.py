# Returns the inverse of a function
def inv(f: dict):
    return {f.get(key): key for key in f.keys()}


# Computes the composition for two functions
def comp(f: dict, g: dict):
    return {key: f.get(g.get(key)) for key in g.keys()}


# Computes the composition of arbitrary many functions
def composition(*functions):
    functions = list(functions)
    if len(functions) == 1:
        return functions[0]
    functions[-2] = comp(functions[-2], functions[-1])
    functions.pop()
    return composition(*functions)


def rotate(rotor, n):
    functions = [rotor]
    for i in range(n):
        functions.insert(0, inv(p))
        functions.append(p)
    return composition(*functions)


def engima(n, j):
    right = [rotate(R_0, n), rotate(L_0, j), P, C]
    left = [inv(elem) for elem in right]
    left.reverse()
    return composition(*(left + [U] + right))


C = {"A": "D", "B": "C", "C": "B", "D": "A", "E": "E"}
P = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
p = {1: 2, 2: 3, 3: 4, 4: 5, 5: 1}
R_0 = {1: 3, 2: 2, 3: 4, 4: 5, 5: 1}
L_0 = {1: 4, 2: 1, 3: 2, 4: 5, 5: 3}
U = {1: 5, 2: 3, 3: 2, 4: 4, 5: 1}

R_1 = rotate(R_0, 1)
print(R_1)
print(engima(n=0, j=0).get("E"))
print(engima(n=1, j=0).get("D"))
