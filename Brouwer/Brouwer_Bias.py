from numpy import zeros, logspace, linspace, dtype, meshgrid, save
from ASC_Solver import arbitrary_solver


datatype = dtype({'names': ['pressure', 'overpotential', 'oxygenpot', 'vacancies', 'holes', 'electrons'],
                 'formats': ['float64', 'float64', 'float64', 'float64', 'float64', 'float64']})

# Create Grid of overpotential and oxygen partial pressure
defect_data = zeros(shape=(1201, 2401), dtype=datatype)

overpotentials = linspace(-0.6, 0.6, 1201, True)
pressures = logspace(-18, 6, 2401, True)

pressures, overpotentials = meshgrid(pressures, overpotentials)

defect_data['overpotential'] = overpotentials
defect_data['pressure'] = pressures

# Calculate defect cncentrations for each grid point
for eta_idx, eta in enumerate(defect_data):
    for p_idx, p in enumerate(eta):

        result = arbitrary_solver(defect_data['overpotential'][eta_idx, p_idx], defect_data['pressure'][eta_idx, p_idx])

        defect_data[eta_idx, p_idx]['vacancies'] = result[0]
        defect_data[eta_idx, p_idx]['holes'] = result[1]
        defect_data[eta_idx, p_idx]['electrons'] = result[2]

save('Brouwer_Bias.npy', defect_data)