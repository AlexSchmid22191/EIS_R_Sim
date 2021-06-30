from numpy import load
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LinearLocator
from Equations import e, k, T
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter
import cmocean

use('../Paper.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Slope_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Slope_Data_Model_10.npy')


fig_p, ax_p = subplots(nrows=3, figsize=(3.25, 6.5), gridspec_kw={'height_ratios': [10, 10, 1]})
fig_n, ax_n = subplots(nrows=3, figsize=(3.25, 6.5), gridspec_kw={'height_ratios': [10, 10, 1]})

ax_p[0].set_title(r'a) Atomic mechanism')
ax_p[1].set_title(r'b) Molecular mechanism')
ax_n[0].set_title(r'a) Atomic mechanism')
ax_n[1].set_title(r'b) Molecular mechanism')

for ax in (ax_p[0], ax_p[1], ax_n[0], ax_n[1]):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())


p_norm = Normalize(vmin=0, vmax=0.75)
n_norm = Normalize(vmin=-3, vmax=3)

p_bar = ColorbarBase(ax_p[2], cmap='cmo.ice', norm=p_norm, orientation='horizontal')
n_bar = ColorbarBase(ax_n[2], cmap='cmo.balance', norm=n_norm, orientation='horizontal', extend='both')

p_bar.ax.xaxis.set_major_locator(LinearLocator(numticks=4))

p_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\ln p}$', fontsize=10)
n_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\eta} \left(\frac{e}{kT}\right)$', fontsize=10)

p_bar.ax.minorticks_off()
n_bar.ax.minorticks_off()

colmesh_p_7 = ax_p[1].pcolormesh(data_7['pressure'], data_7['overpotential'], data_7['p_slope'], vmin=0, vmax=0.75, cmap='cmo.ice')
colmesh_p_10 = ax_p[0].pcolormesh(data_10['pressure'], data_10['overpotential'], data_10['p_slope'], vmin=0, vmax=0.75, cmap='cmo.ice')

colmesh_n_7 = ax_n[1].pcolormesh(data_7['pressure'], data_7['overpotential'], data_7['n_slope']*k*T/e, vmin=-3, vmax=3, cmap='cmo.balance')
colmesh_n_10 = ax_n[0].pcolormesh(data_10['pressure'], data_10['overpotential'], data_10['n_slope']*k*T/e, vmin=-3, vmax=3, cmap='cmo.balance')

fig_p.tight_layout()
fig_n.tight_layout()

fig_p.savefig('Plots/Slopes_7_10_p.png')
fig_n.savefig('Plots/Slopes_7_10_n.png')

fig_p.savefig('Plots/Slopes_7_10_p.pdf')
fig_n.savefig('Plots/Slopes_7_10_n.pdf')

fig_p.savefig('Plots/Slopes_7_10_p.tiff', dpi=300)
fig_n.savefig('Plots/Slopes_7_10_n.tiff', dpi=300)

show()
