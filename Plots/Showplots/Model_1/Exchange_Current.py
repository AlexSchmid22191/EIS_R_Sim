from numpy import load
from matplotlib.style import use
from matplotlib.patches import Rectangle
from mpltools.annotation import slope_marker
from matplotlib.pyplot import subplots, show

data = load('../../../Currents_Resistances_Model_1/Current_Data_Model_1.npy')

use('../Show.mplstyle')

fig, ax = subplots()
ax.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange current density (a.u.)')

slope_marker(origin=(1e-14, 1e-11), slope=1, size_frac=0.1, invert=False, ax=ax)
ax.add_patch(Rectangle((1e1, 1e-2), 1e6, 4e-2, linewidth=0, facecolor='0.8'))
ax.text(1e3, 2e-3, '0')

fig.tight_layout()
fig.savefig('Plots/Exchange_Current.pdf')
fig.savefig('Plots/Exchange_Current.png')

show()
