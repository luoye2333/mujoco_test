import numpy as np
data = np.load("stair_down.npy") * 0.005
np.savetxt("stair_down.txt", data, fmt='%.2f', delimiter=' ')
