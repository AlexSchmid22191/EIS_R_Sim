from numpy import load
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LogLocator, NullFormatter
from mpltools.annotation import slope_marker
import cmocean

use('../Poster.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

fig, ax = subplots(constrained_layout=True)

ax.set_title(r'Molecular mechanism')

ax.set_ylim(1e-10, 1e6)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Exchange current density (a.u.)')
ax.set_xlim(1e-18, 1e6)
ax.xaxis.set_major_locator(LogLocator(numticks=4))
ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_locator(LogLocator(numticks=5))
ax.yaxis.set_minor_formatter(NullFormatter())

ax.yaxis.set_minor_locator(LogLocator(numticks=17))

ax.plot(data_7['pressure'][600, ::100], data_7['ex_current'][600, ::100], linestyle='-')

slope_marker(origin=(3e-3, 1e1), slope=0.5, ax=ax, size_frac=0.2)
slope_marker(origin=(1e-15, 1e-8), slope=0.75, ax=ax, size_frac=0.2)

fig.set_constrained_layout_pads(w_pad=0.1, h_pad=0.1, hspace=0.025, wspace=0.025)

fig.savefig('Plots/Exchange_Current_7.png')

show()
