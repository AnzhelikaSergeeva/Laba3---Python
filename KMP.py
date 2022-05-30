# n = "Hola-hola girls are hooligans Hooligans"
# m = "Hooligan"

def solution(n, m):
    n = m + '$' + n

    mass = [0 for i in range(len(n))]

    for i in range(2*len(m)+1, len(n)):
        max_pr = -1
        for j in range(1, i-1):
            if n[:j] == n[i-j:i] and len(n[:j]) > max_pr:
                max_pr = len(n[:j])
        mass[i] = max_pr

    for i in range(len(mass)):
        if mass[i] == len(m):
            return i - len(m) * 2 - 1

# print(mass)
