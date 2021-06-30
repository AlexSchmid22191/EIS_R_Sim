from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from Equations import e, k, T

use('../Show.mplstyle')

data = load('../../../Currents_Resistances_Model_5/Slope_Data_Model_5.npy')

fig, axes = subplots(nrows=2, figsize=(6, 8))

for ax in axes:
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')


colmesh_p = axes[0].pcolormesh(data['pressure'], data['overpotential'], data['p_slope'], vmin=-1, vmax=1)

cbar_p = fig.colorbar(colmesh_p, ax=axes[0], label=r'$\frac{d\ln j}{d\ln p}$')
cbar_p.ax.minorticks_off()


colmesh_n = axes[1].pcolormesh(data['pressure'], data['overpotential'], data['n_slope']*k*T/e, vmin=0, vmax=4)
cbar_n = fig.colorbar(colmesh_n, ax=axes[1], label=r'$\frac{d\ln j}{d\eta} (\frac{e}{kT})$')
cbar_n.ax.minorticks_off()

fig.tight_layout()
fig.savefig('Plots/Slopes.png')

show()