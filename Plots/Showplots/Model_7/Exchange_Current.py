from numpy import load
from matplotlib.style import use
from matplotlib.patches import Rectangle
from mpltools.annotation import slope_marker
from matplotlib.pyplot import subplots, show

data = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

use('../Show.mplstyle')

fig, ax = subplots()
ax.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange current density (a.u.)')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-10, 1e8)

slope_marker(origin=(1e-11, 1e-5), slope=0.75, size_frac=0.1, invert=False, ax=ax)
slope_marker(origin=(1e1, 1e3), slope=0.5, size_frac=0.1, invert=False, ax=ax)

fig.tight_layout()
fig.savefig('Plots/Exchange_Current.pdf')
fig.savefig('Plots/Exchange_Current.png')

show()
