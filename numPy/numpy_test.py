import numpy as np # import numpy package
# one_d_array = np.array([1,2,3,4]) # create 1D array
# print(one_d_array) # printing 1d array
#
# two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # create 1D array
# print(two_d_array) #printing 2D array


a1 = np.random.randint(20, size=(3, 3, 3))
a2 = np.random.randint(20, size=(3, 3, 3))
a3 = np.random.randint(20, size=(3, 3, 3))
print(a1)
print("*****************************\n")
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
