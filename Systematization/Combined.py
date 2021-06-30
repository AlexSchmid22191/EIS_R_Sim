import numpy as np

np.set_printoptions(threshold=np.inf)

field = np.zeros(shape=(4**4*3*3, 7), dtype=int)

q = 0

# 4 times range(4): distribute 4 electronic charge carriers amon 4 "positions":
# anodic equilibrium, anodic rds, cathodic rsd, cathodic equilibrium

# 2 times range(3): distribute 2 oxygen vacancies among 3 positions:
# anodic equilibrium, cathodic rsd, cathodic equilibrium


for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4, 7):
                    for n in range(4, 7):
                        for index in (i, j, k, l):
                            field[q, index] += 1
                        for index in (m, n):
                            field[q, index] += 1
                        q += 1

for line_idx, line in enumerate(np.unique(field, axis=0)):
    print('#####################################################')
    print('Mechanism {:d}:'.format(line_idx+1))
    print('Holes in anodic equilibirium: {:d}'.format(line[0]))
    print('Holes in anodic rds: {:d}'.format(line[1]))
    print('Electrons in cathodic rds: {:d}'.format(line[2]))
    print('Electrons in cathodic equilibirium: {:d}\n'.format(line[3]))
    print('Vacancies in anodic equilibirium: {:d}'.format(line[4]))
    print('Vacancies in cathodic rds: {:d}'.format(line[5]))
    print('Vacancies in cathodic equilibirium: {:d}'.format(line[6]))
    print('#####################################################\n\n')


print(field[0])

