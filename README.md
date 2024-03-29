
# 1D Random Antiferromagnetic Heisenberg Model Simulation

This repository contains the code, thesis, and figures for a numerical simulation of the 1D Random Antiferromagnetic Heisenberg Model using the Real Space Renormalization Group (RSRG) method.

## File Structure
```bash
.
├── bond_distance.py
├── bond_distribution.py
├── Figures
│   └── Matrix
│       ├── startmatrix.png
│       ├── midrg1.png
│       ├── midrg5.png
│       ├── midrg10.png
│       ├── midrg13.png
│       └── singlet-phase.png
├── matrix_animation.py
├── random_chain.py
├── requirements.txt
└── Thesis
    └── thesis.pdf
```

## Files Description

-   `random_chain.py`: Contains the `Random_chain` class, which performs the renormalization group transformations for the 1D random antiferromagnetic Heisenberg model.
-   `bond_distance.py`: Calculates the distances between the bonds for a given chain length and number of simulations, and plots a Seaborn kdeplot of the distances.
-   `bond_distribution.py`: Calculates the final bond distribution for a given chain length and plots the bond strengths using a Seaborn kdeplot.
-   `matrix_animation.py`: Creates a matrix animation of the renormalization group process, saving snapshots of the process in the "Figures/Matrix" folder.
-   `requirements.txt`: Lists the required packages to run the Python code in this repository.
-
## Folders Description

-   `Figures`: Contains the output plots and animations generated by the Python scripts. It includes a subfolder `Matrix` with snapshots of the `matrix_animation` process.
-   `Thesis`: Contains the PDF file of the author's thesis.

## Thesis

The `Thesis` folder contains a PDF file of the author's thesis, which provides a detailed explanation of the 1D random antiferromagnetic Heisenberg model and the renormalization group method used in this repository.

## Python Code

The main class for the simulation is `Random_chain`, which can be found in the `random_chain.py` file. This class initializes the random chain and performs the renormalization steps.

The class has the following methods:

-   `__init__(self, bond_number, resc)`: Constructor that takes the number of bonds as an input. Also includes a resc variable (default = True) so that rescaling is turned off (Rescaling off allows for the bond_distribution to function properly.)
-   `matrix_creator(self)`: Creates the initial bond matrix with random values.
-   `bonds(self)`: Determines the maximum bond value and its indices, as well as the effective bond and the corresponding parameters (zeta, gamma, and eta).
-   `decimate(self)`: Performs the decimation step of the Real Space Renormalization Group (RSRG) method.
-   `rescale(self)`: Performs the rescaling step of the Real Space Renormalization Group (RSRG) method.
-   `renormalization(self)`: Applies the full renormalization (decimation and rescaling) on the chain.

## Installation and Usage

To run the Python scripts, first clone this repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/1d-random-antiferromagnetic-heisenberg.git
cd 1d-random-antiferromagnetic-heisenberg`
```
Next, install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Once the required packages are installed, you can run the Python scripts.

## Example

```python

from random_chain import Random_chain

# Create a random chain with 100 bonds
chain = Random_chain(100)

# Perform 50 renormalization steps
for _ in range(50):
    chain.renormalization()

# Access the final bond matrix
final_bond_matrix = chain.bond_matrix

# Access the zeta, gamma, and eta parameters
zeta = chain.zeta
gamma = chain.gamma
eta = chain.eta
```

### Dependencies

-   Python 3.x
-   NumPy
-	Matplotlib
-	tqdm
-	Seaborn
-	SciPy

### License

This project is licensed under the MIT License.
