class Position:
    def __init__(self, position, start_distance,finish_distance):
        self.position = position
        self.start_distance = start_distance
        self.finish_distance = finish_distance

    def __str__(self):
        return '\n'.join((N*'{:3}').format(*[i%(N*N) for i in self.position[i:]]) for i in range(0, N*N, N))

    # Переопределяем метод less then для работы PriorityQueue
    def __lt__(self, other):
        return self.start_distance+self.finish_distance < other.start_distance+other.finish_distance


from queue import PriorityQueue

N = 4

def shifts(position):
    zeroPosition = position.index(0)
    i, j = divmod(zeroPosition, N)
    displacement = []
    if i > 0: displacement.append(-N)     # вверх
    if i < N - 1: displacement.append(N)  # вниз
    if j > 0: displacement.append(-1)     # влево
    if j < N - 1: displacement.append(1)  # вправо
    for offset in displacement:
        swap = zeroPosition + offset
        yield tuple(position[swap] if x==zeroPosition else position[zeroPosition] if x==swap else position[x] for x in range(N*N))

def parityOfPairs(state):
    countOfPairs = 0
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            countOfPairs +=1
    return countOfPairs % 2


def fifteenGame(startState):
    terminalState = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    if parityOfPairs(startState)==0:
        print("Нет решений")
    else:
        startState= tuple(startState)
        p = Position(startState, 0,0)
        print(p)
        print()
        fieldStates= PriorityQueue()
        fieldStates.put(p)
        closePoints = set([p])
        parents = {p.position: None}

        while p.position != terminalState:
            p =fieldStates.get()

            for k in shifts(p.position):
                count= 0
                if k not in closePoints:
                    for m in range(len(k)):
                        if k[m] != terminalState[m]:
                            count+=1

                    fieldStates.put(Position(k, p.start_distance +1,p.finish_distance+count))
                    parents[k] = p
                    closePoints.add(k)

        path = []
        x = p
        previous = p
        while p.position != startState:
            p = parents[p.position]
            number = p.position[previous.position.index(0)]
            path.append(number)
            previous = p
        path.reverse()

        print(path)
        print(x)

startState = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9,11,12,10,14,15,0]
fifteenGame(startState)