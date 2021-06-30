from numpy import load, zeros, dtype, save, gradient

# Load shifted Brouwer diagram
defect_data = load('../Brouwer/Brouwer_Bias_Shifted.npy')

# Create some views
vac = defect_data['vacancies']
vac_eq = defect_data['vacancies'][600, :]
hole = defect_data['holes']
hole_eq = defect_data['holes'][600, :]
ox = 3 - defect_data['vacancies']
ox_eq = 3 - defect_data['vacancies'][600, :]
fe = 1 - defect_data['holes'] - defect_data['electrons']
fe_eq = 1 - defect_data['holes'][600, :] - defect_data['electrons'][600, :]

# Create array for current data
datatype = dtype({'names': ['pressure', 'overpotential', 'oxygenpot', 'vacancies', 'holes', 'electrons', 'ex_current',
                            'current', 'resistance'],
                 'formats': ['float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64',
                             'float64']})

current_data = zeros(shape=defect_data.shape, dtype=datatype)

for field in defect_data.dtype.names:
    current_data[field] = defect_data[field]

# Calculate exchange currents, anodic prefactor set to 1
current_data['ex_current'] = ox_eq*hole_eq**2*fe_eq**-2 / (1+10*current_data['pressure']**0.5)

# Calculate net currents
current_data['current'] = current_data['ex_current'] * ((ox/ox_eq)*(hole/hole_eq)**2*(fe/fe_eq)**-2 - (vac/vac_eq))

# Calculate resistance as the inverse dervative of current with respect to overpotential
current_data['resistance'] = 1/gradient(current_data['current'], current_data['overpotential'][:, 0], axis=0)

save('Current_Data_Model_11_Shifted.npy', current_data)
