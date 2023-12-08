from random import randint, random, choices

def fitness(g, s):
    valid_non_s = sum(sum(s[v_int] for v in g[n] if (v_int := int(v))) >= 2 
               for n in g
               if (n_int := int(n)) and not s[n_int])
    leafs_on_s = sum(
                   g.degree(n) == 1
                   for n in g
                   if (n_int := int(n)) and s[n_int]
               )
    return valid_non_s + leafs_on_s


def mutation(g, s):
    chance = 0.15
    n = len(g)

    s_final = []
    for i in range(n):
        v = s[i]
        if random() <= chance:
            v = not v

        s_final.append(v)

    return s_final

def offsprint(g, a, b):
    c = randint(0, len(g))
    return a[:c] + b[c:]

def genetic_search(g) -> set:
    s = set()

    population_size = 100
    generations = 20

    population = [
        [1 if g.degree(n) in (0, 1) else randint(0, 1) for n in g]
        for _ in range(population_size)
    ]

    for gen in range(generations):
        # print(f"{gen=}", end=" ")
        f_p = [fitness(g, p) for p in population ]
        population += [offsprint(g, *choices(population, f_p, k=2))
                       for _ in range(population_size)]

        population += [mutation(g, p) for p in population]

        f_p = [fitness(g, p) for p in population ]
        

        np = set()
        pi = list(range(len(population)))
        for i in range(10):
            i_mf, mf = None, 0
            for ifp, f in enumerate(f_p):
                if f > mf:
                    mf = f
                    i_mf = ifp
            if i == 0:
             print(f"{mf} ")

            np.add(i_mf)
            pi.pop(i_mf)
            f_p.pop(i_mf)

        while len(np) < population_size:
            choice = choices(pi, f_p)[0]
            i_r = pi.index(choice)
            pi.pop(i_r)
            f_p.pop(i_r)
            np.add(choice)

        population = [population[i] for i in np]
       
    f_p = [fitness(g, p) for p in population ]
    i_mf, mf = None, 0
    for i, f in enumerate(f_p):
        if f > mf:
            mf = f
            i_mf = i

    # print(f"{mfp} {population[i_mfp]}")

    return {i for i in range(len(g)) if population[i_mf][i]}

