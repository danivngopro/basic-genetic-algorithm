import random

def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z - 25

def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 100000
    else:
        return abs(1/ans)

def populate(genAmount = 1000):
    solutions = []
    for s in range(genAmount):
        solutions.append((random.uniform(0,10000), random.uniform(0,10000), random.uniform(0,10000)))
    return solutions

solutions = []

for i in range(2000):
    rankedSolutions = []

    solutions = populate()

    # play
    for s in solutions:
        rankedSolutions.append((fitness(s[0], s[1], s[2]), s))
    rankedSolutions.sort()
    rankedSolutions.reverse()

    print(f"=== Gen {i} best solutions === ")
    print(rankedSolutions[0])

    if rankedSolutions[0][0] > 90000:
        break

    bestSolutions = rankedSolutions[:50]

    elements = []
    
    for bs in bestSolutions:
        elements.append(bs[1])
    
    newGen = []

    # repopulate
    for _ in range(1000):
        e1 = random.choice(elements)[0] * random.uniform(0.99, 1.01)
        e2 = random.choice(elements)[1] * random.uniform(0.99, 1.01)
        e3 = random.choice(elements)[2] * random.uniform(0.99, 1.01)

        newGen.append((e1,e2,e3))

    solutions = newGen