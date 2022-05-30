# n = "Hola-hola girls are hooligans Hooligans"
# m = "Hooligan"


def solution(n, m):
    # Creating & filling
    mass = [0 for i in range(len(m))]
    for i in range(len(m) - 1, -1, -1):
        for j in range(len(m) - 1, i, -1):
            if m[i] == m[j]:
                mass[i] = mass[j]
                break
            else:
                mass[i] = len(m) - i - 1

    # Create an alphabetical table (key = symbol, value = number)
    a = {i: len(m) for i in set(n)}
    for key, val in a.items():
        for i in range(len(m)):
            if key == m[i]:
                a[key] = mass[i]
                break

    # Algorithm itself
    el = len(m)-1
    while el < len(n):
        old_el = el
        for i in range(len(m)-1, -1, -1):
            if m[i] == n[el]:
                el -= 1
            else:
                el += a[n[el]]
                break
        if old_el - el == len(m):
            return el + 1


# for key, val in a.items():
#     print(key, val)