import random

# this function represents the result of actions out agents will perform. their action is based on the x,y,z they choose
# and the result of that equation is the result of these actions.
def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z - 25

# for each agent we give a fitness - score.
# if the agent managed to get exactly 0 (not gonna happen probably), we give it a high score because he hit the jackpot
# if not we give 1/ans - the closer the answer is to 0 the higher the fitness will be. (1/~0 = infinity)
def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 100000
    else:
        return abs(1/ans)

#  on the first generation we want to get 1000 agents by default and choose 3 random values.
def populate(genAmount = 1000):
    solutions = []
    for s in range(genAmount):
        solutions.append((random.uniform(0,10000), random.uniform(0,10000), random.uniform(0,10000)))
    return solutions

solutions = []

# 2000 is the maximum number of generations 
for i in range(2000):
    rankedSolutions = []

#    we store our first generation here
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

#   choose the best 50 agents
    bestSolutions = rankedSolutions[:50]

    elements = []
    
    for bs in bestSolutions:
        elements.append(bs[1])
    
    newGen = []

    # repopulate the best agents with a slite mutation
    for _ in range(1000):
        e1 = random.choice(elements)[0] * random.uniform(0.99, 1.01)
        e2 = random.choice(elements)[1] * random.uniform(0.99, 1.01)
        e3 = random.choice(elements)[2] * random.uniform(0.99, 1.01)

        newGen.append((e1,e2,e3))

    solutions = newGen
