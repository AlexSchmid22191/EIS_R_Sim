from numpy import load
from matplotlib.colors import Normalize
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import MultipleLocator
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter
import cmocean

use('../Talk.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Slope_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Slope_Data_Model_10.npy')

fig_n, ax_p = subplots(nrows=3, figsize=(5.5, 11), gridspec_kw={'height_ratios': [30, 30, 1]}, squeeze=True)

ax_p[0].set_title(r'a) Atomic mechanism')
ax_p[1].set_title(r'b) Molecular mechanism')

for ax in ax_p[:2]:
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel(r'Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_major_locator(LogLocator(numticks=6))
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())


n_norm = Normalize(vmin=0, vmax=0.75)
n_bar = ColorbarBase(ax_p[2], cmap='cmo.ice', norm=n_norm, orientation='horizontal')

n_bar.set_label(r'$p_\mathrm{O_2}$ dependency: $\frac{\partial\ln\left|j\right|}{\partial\ln p_\mathrm{O_2}}$')
n_bar.ax.xaxis.set_major_locator(MultipleLocator(0.25))

n_bar.ax.minorticks_off()

colmesh_p_10 = ax_p[0].pcolormesh(data_10['pressure'], data_10['overpotential'], data_10['p_slope'], vmin=0, vmax=0.75, cmap='cmo.ice')
colmesh_p_7 = ax_p[1].pcolormesh(data_7['pressure'], data_7['overpotential'], data_7['p_slope'], vmin=0, vmax=0.75, cmap='cmo.ice')

fig_n.tight_layout()

fig_n.savefig('Plots/Slopes_7_10_p.png')

show()
