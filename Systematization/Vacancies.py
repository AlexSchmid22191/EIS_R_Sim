import numpy as np

field = np.zeros(shape=(9, 5), dtype=int)

for i in range(3):
    for j in range(3):
        field[3*i+j, i] += 1
        field[3*i+j, j] += 1

print(np.unique(field, axis=0))


