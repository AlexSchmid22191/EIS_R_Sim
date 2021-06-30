from cmocean import cm
from cycler import cycler
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LogLocator, NullFormatter, MultipleLocator
from numpy import load, linspace

from Equations import e, k, T
from Semilog_Slope import semilog_slope

use('../Poster.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

fig_mo, ax_mo = subplots(nrows=2, ncols=1, figsize=(5, 10), gridspec_kw={'height_ratios': [30, 30]}, squeeze=True,
                         constrained_layout=True)

for axes in [ax_mo]:
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
    ax_mo[0].plot(data_7['overpotential'][::50, i], abs(data_7['current'][::50, i]))

for i in range(1600, 2600, 200):
    ax_mo[0].plot(data_7['overpotential'][:, i], abs(data_7['current'][:, i]), linestyle='-', marker='')

for i in range(600, 1600, 200):
    ax_mo[1].plot(data_7['overpotential'][::50, i], abs(data_7['current'][::50, i]))

for i in range(600, 1600, 200):
    ax_mo[1].plot(data_7['overpotential'][:, i], abs(data_7['current'][:, i]), linestyle='-', marker='')


# norm = LogNorm(vmin=1e-12, vmax=1e6)
# bar_mo = ColorbarBase(ax_mo[2], cmap=truncate_colormap(cm.ice, 0, 0.9, n=255), norm=norm, orientation='horizontal')

# for bar in bar_mo, :
#     bar.set_label('Oxygen partial pressure (bar)')
#     bar.ax.xaxis.set_major_locator(FixedLocator([10**i for i in range(-12, 12, 6)]))
#     bar.ax.xaxis.set_minor_locator(LogLocator(numticks=10))
#     bar.ax.xaxis.set_minor_formatter(NullFormatter())

ax_mo[0].set_title(r'$10^{6}$ to $10^{-2}$ bar $\mathrm{O}_2$')
ax_mo[1].set_title(r'$10^{-4}$ to $10^{-12}$ bar $\mathrm{O}_2$')

ax_mo[0].set_ylim(1e0, 1e15)
ax_mo[1].set_ylim(1e-6, 1e9)

ax_mo[0].yaxis.set_major_locator(LogLocator(numticks=6))
ax_mo[0].yaxis.set_minor_locator(LogLocator(numticks=15))
ax_mo[1].yaxis.set_major_locator(LogLocator(numticks=6))
ax_mo[1].yaxis.set_minor_locator(LogLocator(numticks=15))

semilog_slope(origin=(0.4, 1e4), slope=2*e/k/T, ax=ax_mo[0], text=r'$\frac{2e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(-0.1, 1e11), slope=-2*e/k/T, ax=ax_mo[0], text=r'$-\frac{2e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(-0.4, 1e3), slope=-1*e/k/T, ax=ax_mo[0], text=r'$-\frac{e}{kT}$', frac=0.15, inverted=True)

semilog_slope(origin=(0.3, 1e-4), slope=3*e/k/T, ax=ax_mo[1], text=r'$\frac{3e}{kT}$', frac=0.15, inverted=False)
semilog_slope(origin=(0.3, 1e8), slope=2*e/k/T, ax=ax_mo[1], text=r'$\frac{2e}{kT}$', frac=0.15, inverted=True)
semilog_slope(origin=(-0.4, 1e-5), slope=-1*e/k/T, ax=ax_mo[1], text=r'$-\frac{e}{kT}$', frac=0.15, inverted=True)

fig_mo.suptitle('Molecular mechanism\n')
fig_mo.set_constrained_layout_pads(w_pad=0.1, h_pad=0.1, hspace=0.025, wspace=0.025)

fig_mo.savefig('Plots/Current_Voltage_Curves_Model_7.png')

show()