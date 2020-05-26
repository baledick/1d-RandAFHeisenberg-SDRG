import numpy as np
import matplotlib.pyplot as plt
from classes.zero_temp_spin_chain import Chain
from tqdm import tqdm
from scipy.optimize import curve_fit

def lin(x, m, b):
    return (m*x) + b

lattice = 1001
max_value = 100
iterations = 100
range_iterations = np.array(range(iterations))
continuous = np.linspace(0, iterations - 1, iterations*100)
N_systems= 1000
values = np.zeros(iterations)
mean_values = np.zeros(iterations)
cov_values = np.zeros(iterations)

for n in tqdm(range(N_systems)):

    system = Chain(lattice, max_value)

    for i in np.arange(iterations):
        values[i] = system.bonds.mean()
        system.elimination_transformation()

    mean_values += values
    cov_values += values**2

mean_values /= N_systems
cov_values /= N_systems
cov_values -= mean_values**2
cov_values = np.sqrt(cov_values)

popt, pcov = curve_fit(lin, range_iterations, mean_values)

plt.errorbar(range_iterations, mean_values, yerr = cov_values, label = f"m = {popt[0]:.3f}, b = {popt[1]:.3f}")
plt.plot(continuous, lin(continuous, *popt))
plt.legend(loc = "upper right")
plt.ylabel("mean bond")
plt.xlabel("RG iterations")
plt.title(f"Mean bond vs RG iterations, N_systems = {N_systems}")
plt.show()