from numpy import load, zeros, dtype, save, gradient, log, nan

# Load shifted Brouwer diagram
current_data = load('Current_Data_Model_11.npy')

# Create array for slope data
datatype = dtype({'names': ['pressure', 'overpotential', 'oxygenpot', 'p_slope', 'n_slope', 'rp_slope', 'rn_slope'],
                 'formats': ['float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64']})

slope_data = zeros(shape=current_data.shape, dtype=datatype)

for field in current_data.dtype.names:
    if field in slope_data.dtype.names:
        slope_data[field] = current_data[field]

current_data['current'][600, :] = nan

slope_data['p_slope'] = gradient(log(abs(current_data['current'])), log(current_data['pressure'][0, :]), axis=1)
slope_data['n_slope'] = gradient(log(abs(current_data['current'])), current_data['overpotential'][:, 0], axis=0)

slope_data['rp_slope'] = gradient(log(current_data['resistance']), log(current_data['pressure'][0, :]), axis=1)
slope_data['rn_slope'] = gradient(log(current_data['resistance']), abs(current_data['overpotential'][:, 0]), axis=0)

save('Slope_Data_Model_11.npy', slope_data)