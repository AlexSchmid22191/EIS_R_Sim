from numpy import load
from numpy.ma import masked_equal
from matplotlib.style import use
from matplotlib.pyplot import subplots, show
from matplotlib.colors import SymLogNorm, LogNorm
from matplotlib.ticker import SymmetricalLogLocator, LogLocator

use('../Show.mplstyle')

data = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

abs_current_den = masked_equal(abs(data['current']), 0)

fig, axes = subplots(nrows=1, figsize=(6, 3))


axes.set_xscale('log')
axes.set_xlabel('Oxygen partial pressure (bar)')
axes.set_ylabel('Overpotential (V)')

colmesh_sym = axes.pcolormesh(data['pressure'][:, :1801], data['overpotential'][:, :1801], data['current'][:, :1801],
                                 norm=SymLogNorm(linthresh=1e-12, linscale=2, vmin=-1e4, vmax=1e4), cmap='RdBu_r')

cont_sym = axes.contour(data['pressure'][:, :1801], data['overpotential'][:, :1801], data['current'][:, :1801],
                           locator=SymmetricalLogLocator(subs=None, base=10, linthresh=1e-12), colors='k',
                           linestyles='dashed')

cbar_sym = fig.colorbar(colmesh_sym, ax=axes, ticks=SymmetricalLogLocator(subs=None, base=10, linthresh=1e-12),
                        label='Net current density (a.u.)')
cbar_sym.ax.minorticks_off()


# colmesh_abs = axes[1].pcolormesh(data['pressure'][:, :1801], data['overpotential'][:, :1801], abs_current_den[:, :1801],
#                                  norm=LogNorm(vmin=1e-14, vmax=1e4), cmap='viridis')
#
# cont_abs = axes[1].contour(data['pressure'][:, :1801], data['overpotential'][:, :1801], abs_current_den[:, :1801],
#                            locator=LogLocator(numticks=10), colors='k',
#                            linestyles='dashed')
#
# cbar_abs = fig.colorbar(colmesh_abs, ax=axes[1], ticks=LogLocator(numticks=19),
#                         label='Absolute net current density (A/m²)')
cbar_sym.ax.minorticks_off()

fig.tight_layout()
fig.savefig('Plots/Current_Densities.png', dpi=600)

show()
