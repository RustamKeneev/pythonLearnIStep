import numpy as np
a1 = np.random.randint(20, size=(3, 3, 3))
a2 = np.random.randint(20, size=(3, 3, 3))
a3 = np.random.randint(20, size=(3, 3, 3))
print(a1, a2, a3, sep="\n\n", end="\n\n")

print("____________________________")
concat = np.concatenate((a1, a2, a3), axis=0)
print("concat 0", concat, sep="\n")

print("____________________________")
concat = np.concatenate((a1, a2, a3), axis=1)
print("concat 1", concat, sep="\n")

print("____________________________")
concat = np.concatenate((a1, a2, a3), axis=2)
print("concat 2", concat, sep="\n")

print("____________________________")
concat = np.concatenate((a1, a2, a3), axis=None)
print("concat none", concat, sep="\n")
