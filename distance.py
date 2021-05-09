import numpy as np
import matplotlib.pyplot as plt
from random_singlets.ZT_RSS import ZT_Random_Spin
from tqdm import tqdm

iterations = 10

for j in tqdm(range(iterations)):
    matrix = ZT_Random_Spin(100,1)
    dist = []
    i=0
    while matrix.end_rg == 0:
        matrix.renormalization()
        dist = np.append(dist, matrix.distance)

    plt.hist(dist)
plt.savefig('Figures/distance.png')
plt.show()

