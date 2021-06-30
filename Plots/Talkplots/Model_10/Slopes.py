from matplotlib.pyplot import subplots, show
from matplotlib.ticker import LogLocator, NullFormatter, FixedLocator

from matplotlib.style import use
from numpy import load
from Equations import e, k, T
import cmocean

use('../Talk.mplstyle')

data = load('../../../Currents_Resistances_Model_10/Slope_Data_Model_10.npy')

p_fig, p_ax = subplots()
n_fig, n_ax = subplots()

for ax in (p_ax, n_ax):
    ax.set_title('Atomic mechanism')
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_major_locator(FixedLocator(locs=[10**n for n in range(-24, 7, 6)]))
    ax.xaxis.set_minor_locator(LogLocator(numticks=25))
    ax.xaxis.set_minor_formatter(NullFormatter())

colmesh_p = p_ax.pcolormesh(data['pressure'], data['overpotential'], data['p_slope'], vmin=0, vmax=0.75, cmap='cmo.ice')
colmesh_n = n_ax.pcolormesh(data['pressure'], data['overpotential'], data['n_slope']*k*T/e, vmin=-3, vmax=3, cmap='cmo.balance')

p_fig.tight_layout()
n_fig.tight_layout()

p_fig.savefig('Plots/p_Slopes.png')
n_fig.savefig('Plots/n_Slopes.png')

show()