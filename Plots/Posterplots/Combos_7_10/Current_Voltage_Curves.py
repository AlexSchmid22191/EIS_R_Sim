from numpy import load, linspace
from cycler import cycler
from matplotlib.ticker import LogLocator, NullFormatter, MultipleLocator, FixedLocator
from mpltools.annotation import slope_marker
from Equations import e, k, T
from cmocean import cm
from matplotlib.colors import Normalize, LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.colorbar import ColorbarBase
from Plots.Colormapper import truncate_colormap
from Semilog_Slope import semilog_slope


use('../Poster.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Current_Data_Model_10.npy')


fig_at, ax_at = subplots(nrows=3, ncols=1, figsize=(5, 10), gridspec_kw={'height_ratios': [30, 30, 1]}, squeeze=True)
fig_mo, ax_mo = subplots(nrows=3, ncols=1, figsize=(5, 10), gridspec_kw={'height_ratios': [30, 30, 1]}, squeeze=True)

for axes in [ax_at, ax_mo]:
    for ax in axes[:2]:
        ax.set_yscale('log')
        ax.set_xlabel('Overpotential (V)')
        ax.set_ylabel('Absolute current density (a.u.)')
        ax.set_xlim(-0.6, 0.6)
        ax.xaxis.set_major_locator(MultipleLocator(0.3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax.yaxis.set_minor_formatter(NullFormatter())

    axes[1].set_prop_cycle(cycler(color=[cm.ice(i) for i in linspace(0, 0.4, 5)], marker=['o', 's', '^', 'd', 'v']))
    axes[0].set_prop_cycle(cycler(color=[cm.ice(i) for i in linspace(0.5, 0.9, 5)], marker=['o', 's', '^', 'd', 'v']))


for i in range(1600, 2600, 200):
    ax_at[0].plot(data_10['overpotential'][::50, i], abs(data_10['current'][::50, i]))
    ax_mo[0].plot(data_7['overpotential'][::50, i], abs(data_7['current'][::50, i]))

for i in range(1600, 2600, 200):
    ax_at[0].plot(data_10['overpotential'][:, i], abs(data_10['current'][:, i]), linestyle='-', marker='')
    ax_mo[0].plot(data_7['overpotential'][:, i], abs(data_7['current'][:, i]), linestyle='-', marker='')

for i in range(600, 1600, 200):
    ax_at[1].plot(data_10['overpotential'][::50, i], abs(data_10['current'][::50, i]))
    ax_mo[1].plot(data_7['overpotential'][::50, i], abs(data_7['current'][::50, i]))

for i in range(600, 1600, 200):
    ax_at[1].plot(data_10['overpotential'][:, i], abs(data_10['current'][:, i]), linestyle='-', marker='')
    ax_mo[1].plot(data_7['overpotential'][:, i], abs(data_7['current'][:, i]), linestyle='-', marker='')


norm = LogNorm(vmin=1e-12, vmax=1e6)
bar_at = ColorbarBase(ax_at[2], cmap=truncate_colormap(cm.ice, 0, 0.9, n=255), norm=norm, orientation='horizontal')
bar_mo = ColorbarBase(ax_mo[2], cmap=truncate_colormap(cm.ice, 0, 0.9, n=255), norm=norm, orientation='horizontal')

for bar in (bar_at, bar_mo):
    bar.set_label('Oxygen partial pressure (bar)')
    bar.ax.xaxis.set_major_locator(FixedLocator([10**i for i in range(-12, 12, 6)]))
    bar.ax.xaxis.set_minor_locator(LogLocator(numticks=10))
    bar.ax.xaxis.set_minor_formatter(NullFormatter())

ax_at[0].set_ylim(1e-2, 1e6)
ax_at[1].set_ylim(1e-5, 1e1)
ax_mo[0].set_ylim(1e0, 1e15)
ax_mo[1].set_ylim(1e-6, 1e9)

ax_at[0].yaxis.set_major_locator(LogLocator(numticks=5))
ax_at[0].yaxis.set_minor_locator(LogLocator(numticks=9))
ax_at[1].yaxis.set_major_locator(LogLocator(numticks=4))
ax_at[1].yaxis.set_minor_locator(LogLocator(numticks=7))
ax_mo[0].yaxis.set_major_locator(LogLocator(numticks=6))
ax_mo[0].yaxis.set_minor_locator(LogLocator(numticks=15))
ax_mo[1].yaxis.set_major_locator(LogLocator(numticks=6))
ax_mo[1].yaxis.set_minor_locator(LogLocator(numticks=15))

semilog_slope(origin=(-0.05, 1e4), slope=-2*e/k/T, ax=ax_at[0], text=r'$-\frac{2e}{kT}$', frac=0.15, inverted=False)

semilog_slope(origin=(0.35, 1e-3), slope=2*e/k/T, ax=ax_at[1], text=r'$\frac{2e}{kT}$', frac=0.15, inverted=False)

semilog_slope(origin=(0.4, 1e4), slope=2*e/k/T, ax=ax_mo[0], text=r'$\frac{2e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(-0.1, 1e11), slope=-2*e/k/T, ax=ax_mo[0], text=r'$-\frac{2e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(-0.4, 1e3), slope=-1*e/k/T, ax=ax_mo[0], text=r'$-\frac{e}{kT}$', frac=0.15, inverted=True)

semilog_slope(origin=(0.3, 1e-4), slope=3*e/k/T, ax=ax_mo[1], text=r'$\frac{3e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(0.3, 1e8), slope=2*e/k/T, ax=ax_mo[1], text=r'$\frac{2e}{kT}$', frac=0.15, inverted=True)
semilog_slope(origin=(-0.4, 1e-5), slope=-1*e/k/T, ax=ax_mo[1], text=r'$-\frac{e}{kT}$', frac=0.15, inverted=True)

ax_at[0].set_title('Atomic mechanism')
ax_mo[0].set_title('Molecular mechanism')

fig_at.tight_layout()
fig_mo.tight_layout()

fig_at.savefig('Plots/Current_Voltage_Curves_Model_10.png')
fig_mo.savefig('Plots/Current_Voltage_Curves_Model_7.png')

show()