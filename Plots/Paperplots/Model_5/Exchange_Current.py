from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LogLocator, NullFormatter
from mpltools.annotation import slope_marker
from numpy import load

use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_5/Current_Data_Model_5.npy')

fig, ax = subplots()

ax.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-14, 1e0)

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange current density (a.u.)')

ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.yaxis.set_major_locator(LogLocator(numticks=8))
ax.yaxis.set_minor_locator(LogLocator(numticks=15, subs=range(1,10)))
ax.yaxis.set_minor_formatter(NullFormatter())

slope_marker(origin=(1e-14, 1e-11), slope=1, size_frac=0.1, invert=False, ax=ax)
slope_marker(origin=(1e3, 1e-6), slope=-1, size_frac=0.1, invert=True, ax=ax)

fig.tight_layout()

fig.savefig('Plots/Exchange_Current.pdf')
fig.savefig('Plots/Exchange_Current.png')

show()
