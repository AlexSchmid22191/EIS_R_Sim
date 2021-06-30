from numpy import load
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import MultipleLocator
from Equations import e, k, T
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter
from Plots.Colormapper import GnBuDiv_map, GnRdDiv_map
#import cmocean
import colorcet

use('../Poster.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Slope_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Slope_Data_Model_10.npy')

fig_n, ax_n = subplots(nrows=3, figsize=(5.5, 11), gridspec_kw={'height_ratios': [20, 20, 1]}, squeeze=True)

ax_n[0].set_title(r'a) Atomic mechanism')
ax_n[1].set_title(r'b) Molecular mechanism')

for ax in ax_n[:2]:
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel(r'Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_major_locator(LogLocator(numticks=6))
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())


n_norm = Normalize(vmin=-3, vmax=3)
n_bar = ColorbarBase(ax_n[2], cmap='cmo.curl', norm=n_norm, orientation='horizontal', extend='both')

n_bar.set_label(r'Tafel slope: $\frac{\partial\ln\left|j\right|}{\partial\eta} \left(\frac{e}{kT}\right)$')
n_bar.ax.xaxis.set_major_locator(MultipleLocator(1))

n_bar.ax.minorticks_off()

colmesh_n_7 = ax_n[0].pcolormesh(data_7['pressure'], data_7['overpotential'], data_7['n_slope']*k*T/e, vmin=-3, vmax=3, cmap='cmo.curl')
colmesh_n_10 = ax_n[1].pcolormesh(data_10['pressure'], data_10['overpotential'], data_10['n_slope']*k*T/e, vmin=-3, vmax=3, cmap='cmo.curl')

fig_n.tight_layout()

fig_n.savefig('Plots/Slopes_7_10_n.png')

show()
