from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from mpltools.annotation import slope_marker
from matplotlib.ticker import LogLocator, NullFormatter
from matplotlib.patches import Rectangle
from Equations import e, k, T


use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_10/Current_Data_Model_10.npy')

fig, ax = subplots()

ax.plot(data['pressure'][600, ::50], data['resistance'][600, ::50], linestyle='-', label='Real resistance')
ax.plot(data['pressure'][600, ::50], k*T/e/data['ex_current'][600, ::50], linestyle='-',
        label='From exchange current')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1e-18, 1e6)
ax.set_ylim(1e-2, 1e6)

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange resistance (a.u.)')

ax.xaxis.set_minor_locator(LogLocator(numticks=24))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.yaxis.set_major_locator(LogLocator(numticks=9))
ax.yaxis.set_minor_locator(LogLocator(numticks=9, subs=range(1,10)))
ax.yaxis.set_minor_formatter(NullFormatter())

ax.text(1e2, 3e-1, '0')
ax.add_patch(Rectangle((1e0, 1e-1), 1e5, 5e-2, linewidth=0, facecolor='0.8'))
slope_marker(origin=(1e-12, 1e2), slope=-0.5, size_frac=0.1, invert=True, ax=ax)

fig.tight_layout()

ax.legend()

fig.savefig('Plots/Exchange_Resistance_Model_10.pdf')
fig.savefig('Plots/Exchange_Resistance_Model_10.png')

show()
