from numpy import load, log10
from numpy.ma import masked_equal
from matplotlib.style import use
from matplotlib.pyplot import subplots, show
from matplotlib.colors import SymLogNorm, LogNorm
from matplotlib.ticker import SymmetricalLogLocator, LogLocator

use('../Show.mplstyle')

data = load('../../../Currents_Resistances_Model_4/Current_Data_Model_4.npy')

abs_current_den = masked_equal(abs(data['current']), 0)

fig, ax = subplots(figsize=(6, 4))

ax.set_xscale('log')
ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Overpotential (V)')

colmesh = ax.pcolormesh(data['pressure'], data['overpotential'], data['resistance'],
                        norm=LogNorm(vmin=1e-12, vmax=1e16))

cbar = fig.colorbar(colmesh, ax=ax, ticks=LogLocator(numticks=8), label='Resistance (a.u.)')
cbar.ax.minorticks_off()

fig.tight_layout()
fig.savefig('Plots/Resistances.png')

show()
