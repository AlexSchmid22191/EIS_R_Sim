from numpy import load, linspace
from cycler import cycler
from matplotlib.ticker import LogLocator, NullFormatter
from mpltools.annotation import slope_marker
from cmocean import cm
from matplotlib.colors import Normalize, LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.colorbar import ColorbarBase


use('../Poster.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Current_Data_Model_10.npy')


fig, axes = subplots(nrows=3, ncols=1, figsize=(5.5, 11), gridspec_kw={'height_ratios': [30, 30, 1]}, squeeze=True)


for ax in axes[:-1]:
    ax.set_yscale('log')
    ax.set_xlabel('Overpotential (V)')
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlim(-0.65, 0.65)
    ax.set_prop_cycle(cycler(color=[cm.ice(i) for i in linspace(0, 0.9, 10)], marker=['o', 's', '^', 'd', 'v']*2))

    # ax.yaxis.set_major_locator(LogLocator(numticks=5))
    # ax.yaxis.set_minor_formatter(NullFormatter())


# # axes[0].yaxis.set_minor_locator(LogLocator(numticks=9))
# # axes[1].yaxis.set_minor_locator(LogLocator(numticks=17))
#
for i in range(400, 2400, 200):
    axes[0].plot(data_10['overpotential'][::100, i], abs(data_10['current'][::100, i]))
    axes[1].plot(data_7['overpotential'][::100, i], abs(data_7['current'][::100, i]))
for i in range(400, 2400, 200):
    axes[0].plot(data_10['overpotential'][:, i], abs(data_10['current'][:, i]), linestyle='-', marker='')
    axes[1].plot(data_7['overpotential'][:, i], abs(data_7['current'][:, i]), linestyle='-', marker='')



norm = LogNorm(vmin=1e-14, vmax=1e6)
bar = ColorbarBase(axes[2], cmap='cmo.ice', norm=norm, orientation='horizontal')

bar.set_label(r'$p_\mathrm{O_2}$ dependency: $\frac{\partial\ln\left|j\right|}{\partial\ln p_\mathrm{O_2}}$')
#bar.ax.xaxis.set_major_locator(MultipleLocator(0.25))
bar.ax.minorticks_off()


# # for i in range(400, 2300, 200):
# #
# # for i in range(400, 2300, 200):
# #
#
# # slope_marker(origin=(1e-12, 1e-5), slope=0.5, ax=axes[0], size_frac=0.2)
# # slope_marker(origin=(3e-3, 1e1), slope=0.5, ax=axes[1], size_frac=0.2)
# # slope_marker(origin=(1e-15, 1e-8), slope=0.75, ax=axes[1], size_frac=0.2)
# #
# #
# fig_at.savefig('Plots/Slopes_7_10_p.pdf')

show()