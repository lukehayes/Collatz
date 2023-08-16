import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from collatz.collatz import collatz

for x in range(10):
    print("----")
    collatz(x)


# heights = []

# for n in range(10):
    # heights.append(n)

# x = heights
# y = np.cos(x)

# fig,ax = plt.subplots()

# ax.plot(x,y)

# plt.show()
