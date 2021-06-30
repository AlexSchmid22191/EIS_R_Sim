from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from mpltools.annotation import slope_marker
from matplotlib.patches import Rectangle
from matplotlib.ticker import LogLocator, NullFormatter

use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_3/Current_Data_Model_3.npy')

fig, ax = subplots()

ax.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-4, 1e1)

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange current density (a.u.)')

ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())

slope_marker(origin=(1e-14, 3e-3), slope=0.25, size_frac=0.10, invert=False, ax=ax)
ax.add_patch(Rectangle((4e-1, 1e0), 1e5, 4e-1, linewidth=0, facecolor='0.8'))
ax.text(1e2, 5e-1, '0')

fig.tight_layout()

fig.savefig('Plots/Exchange_Current.pdf')
fig.savefig('Plots/Exchange_Current.png')

show()
