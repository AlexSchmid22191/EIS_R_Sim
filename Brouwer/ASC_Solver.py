from scipy.optimize import root
from numpy import array, load, searchsorted
from Equations import residual_function, residual_jacobian, oxygenpot, equi_pressure

# Lookup Brouwer diagramm to get starting conditions for optimization
lookup = load('Brouwer_Ideal.npy')


def arbitrary_solver(eta, p):
    """Solve the defect equilibria for given oxygen partial pressure and overpotential"""

    # Convert oxygen partial pressure and overpotential to equilvalent pressure for searching the lookup table
    p = equi_pressure(oxygenpot(eta, p))

    # Thermodynamic parameters for bulk LSF
    ki = 1.2e-7
    kox = 770

    # Look for closest match in the lookup Brouwer diagramm and use as starting guess
    p_idx = searchsorted(lookup['pressure'], p)
    x_guess = array([lookup['vacancies'][p_idx], lookup['holes'][p_idx], lookup['electrons'][p_idx]])

    solution = root(residual_function, x_guess, args=(p, ki, kox), jac=residual_jacobian)

    return solution.x
