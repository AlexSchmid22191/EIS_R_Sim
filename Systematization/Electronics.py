import numpy as np

np.set_printoptions(threshold=np.inf)

field = np.zeros(shape=(4**4, 4), dtype=int)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for index in (i, j, k, l):
                    field[4 ** 3 * i + 4 ** 2 * j + 4 * k + l, index] += 1

print(np.unique(field, axis=0))



