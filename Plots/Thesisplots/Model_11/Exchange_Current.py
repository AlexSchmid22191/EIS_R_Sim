from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from mpltools.annotation import slope_marker
from matplotlib.ticker import LogLocator, NullFormatter
from matplotlib.patches import Rectangle

use('../Thesis.mplstyle')

data = load('../../../Currents_Resistances_Model_11/Current_Data_Model_11.npy')

fig, ax = subplots()

ax.plot([])
ax.plot([])
ax.plot(data['pressure'][600, ::100], data['ex_current'][600, ::100], linestyle='-', marker='o')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-7, 1e1)

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange current density (a.u.)')

ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.yaxis.set_major_locator(LogLocator(numticks=10))
ax.yaxis.set_minor_locator(LogLocator(numticks=10, subs=range(1,10)))
ax.yaxis.set_minor_formatter(NullFormatter())

for index, label in enumerate(ax.yaxis.get_ticklabels()):
    if index % 2 != 1:
        label.set_visible(False)

slope_marker(origin=(1e3, 1e-3), slope=-0.5, size_frac=0.1, invert=True, ax=ax)
slope_marker(origin=(1e-12, 5e-4), slope=0.5, size_frac=0.1, invert=True, ax=ax)

fig.tight_layout()

fig.savefig('Plots/Exchange_Current_Model_11.pdf')
fig.savefig('Plots/Exchange_Current_Model_11.png')
fig.savefig('Plots/Exchange_Current_Model_11.tiff', dpi=300)

show()
