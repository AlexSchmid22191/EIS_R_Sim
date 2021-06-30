from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from Equations import e, k, T
from matplotlib.ticker import LinearLocator

use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_10/Slope_Data_Model_10.npy')

p_fig, p_ax = subplots()
n_fig, n_ax = subplots()

for ax in (p_ax, n_ax):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)

colmesh_p = p_ax.pcolormesh(data['pressure'], data['overpotential'], data['rp_slope'], vmin=-0.5, vmax=0.5, cmap='jet')
cbar_p = p_fig.colorbar(colmesh_p, ax=p_ax, label=r'$\frac{d\ln R}{d\ln p}$', orientation='horizontal')
cbar_p.ax.xaxis.set_major_locator(LinearLocator(numticks=6))
cbar_p.ax.minorticks_off()

colmesh_n = n_ax.pcolormesh(data['pressure'], data['overpotential'], data['rn_slope']*k*T/e)
cbar_n = n_fig.colorbar(colmesh_n, ax=n_ax, label=r'$\frac{d\ln R}{d\eta} (\frac{e}{kT})$', orientation='horizontal')
cbar_n.ax.xaxis.set_major_locator(LinearLocator(numticks=5))
cbar_n.ax.minorticks_off()

p_fig.tight_layout()
n_fig.tight_layout()

p_fig.savefig('Plots/Rp_Slopes.png')
n_fig.savefig('Plots/Rn_Slopes.png')

show()