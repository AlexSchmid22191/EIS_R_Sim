from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, searchsorted


data = load('../../../Currents_Resistances_Model_1/Current_Data_Model_1.npy')
fit_data_an = load('../../../Currents_Resistances_Model_1/Tafel_Fit_Data.npy')


use('../Show.mplstyle')

fig, axes = subplots(nrows=2, figsize=(6, 8))

for pressure in fit_data_an['pressure'][0, :]:
    p_idx = searchsorted(data['pressure'][0, :], pressure)

    axes[0].plot(data['overpotential'][550::25, p_idx], data['current'][550::25, p_idx])
    axes[0].plot(data['overpotential'][600, p_idx], data['ex_current'][600, p_idx], 'Xr')

    print(data['current'][600, p_idx])
    print(data['ex_current'][600, p_idx])

for p_idx in range(5):
    axes[0].plot(fit_data_an['overpotential'][:, p_idx], fit_data_an['current'][:, p_idx], linestyle='-', marker='')

axes[0].set_yscale('log')
axes[0].set_xlim(-0.1, 0.7)

axes[0].set_xlabel('Overpotential (V)')
axes[0].set_ylabel('Current density (A/m²)')


show()
