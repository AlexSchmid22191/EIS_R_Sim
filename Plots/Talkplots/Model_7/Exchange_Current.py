from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from mpltools.annotation import slope_marker
from matplotlib.ticker import LogLocator, NullFormatter

use('../Talk.mplstyle')

data = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

fig, ax = subplots()

ax.set_title('Molecular mechanism')

ax.plot(data['pressure'][600, ::100], data['ex_current'][600, ::100], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-10, 1e8)

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Exchange current (a.u.)')

ax.xaxis.set_major_locator(LogLocator(numticks=4))
ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.yaxis.set_major_locator(LogLocator(numticks=9))
ax.yaxis.set_minor_locator(LogLocator(numticks=19))
ax.yaxis.set_minor_formatter(NullFormatter())


slope_marker(origin=(1e3, 3e5), slope=0.5, size_frac=0.2, invert=True, ax=ax)
slope_marker(origin=(1e-15, 1e-8), slope=0.75, size_frac=0.2, invert=False, ax=ax)

fig.tight_layout()

fig.savefig('Plots/Exchange_Current_Model_7.png')

show()
