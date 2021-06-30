from Equations import residual_function, residual_jacobian, oxygenpot
from numpy import logspace, empty, array, save, dtype, savetxt
from scipy.optimize import root


ki = 1.2e-7
kox = 770.0


datatype = dtype({'names': ['pressure', 'oxygenpot', 'vacancies', 'holes', 'electrons'],
                 'formats': ['float64', 'float64', 'float64', 'float64', 'float64']})

defect_data = empty(shape=6001, dtype=datatype)

defect_data['pressure'] = logspace(-36, 24, len(defect_data), True)

x_guess = array([6.48e-01, 1.56e-09, 8.94e-01])

for p_idx, p in enumerate(defect_data['pressure']):
    solution = root(residual_function, x_guess, args=(p, ki, kox), jac=residual_jacobian)

    defect_data['pressure'][p_idx] = p
    defect_data['vacancies'][p_idx] = solution.x[0]
    defect_data['holes'][p_idx] = solution.x[1]
    defect_data['electrons'][p_idx] = solution.x[2]

    x_guess = solution.x * 1.001

defect_data['oxygenpot'] = oxygenpot(0, defect_data['pressure'])

save('Brouwer_Ideal.npy', defect_data)
