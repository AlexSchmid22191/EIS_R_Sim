from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from Equations import e, k, T

use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_5/Slope_Data_Model_5.npy')

p_fig, p_ax = subplots()
n_fig, n_ax = subplots()

for ax in (p_ax, n_ax):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)

colmesh_p = p_ax.pcolormesh(data['pressure'], data['overpotential'], data['p_slope'], vmin=-1, vmax=1)
cbar_p = p_fig.colorbar(colmesh_p, ax=p_ax, label=r'$\frac{d\ln j}{d\ln p}$', orientation='horizontal')
cbar_p.ax.minorticks_off()

colmesh_n = n_ax.pcolormesh(data['pressure'], data['overpotential'], data['n_slope']*k*T/e, vmin=-4, vmax=4)
cbar_n = n_fig.colorbar(colmesh_n, ax=n_ax, label=r'$\frac{d\ln j}{d\eta} (\frac{e}{kT})$', orientation='horizontal')
cbar_n.ax.minorticks_off()

p_fig.tight_layout()
n_fig.tight_layout()

p_fig.savefig('Plots/p_Slopes.png')
n_fig.savefig('Plots/n_Slopes.png')

show()
