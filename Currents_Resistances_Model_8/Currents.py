from numpy import load, zeros, dtype, save, gradient

# Load shifted Brouwer diagram
defect_data = load('../Brouwer/Brouwer_Bias.npy')

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
current_data['ex_current'] = ox_eq**2 * hole_eq**3 * fe_eq**-3 * vac_eq**-1 * \
                             1/(1+59.40*current_data['pressure']*fe_eq/hole_eq)

# Calculate net currents
current_data['current'] = current_data['ex_current'] * \
                          ((1+59.40*current_data['pressure']*fe_eq/hole_eq)/(1+59.40*current_data['pressure']*fe/hole))\
                          * ((ox/ox_eq)**2*(hole/hole_eq)**3*(fe/fe_eq)**-3*(vac/vac_eq)**-1
                             - (vac/vac_eq)*(hole/hole_eq)**-1*(fe/fe_eq))

# Calculate resistance as the inverse dervative of current with respect to overpotential
current_data['resistance'] = 1/gradient(current_data['current'], current_data['overpotential'][:, 0], axis=0)

save('Current_Data_Model_8.npy', current_data)
