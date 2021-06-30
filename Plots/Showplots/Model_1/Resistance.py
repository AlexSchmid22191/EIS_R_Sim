from numpy import load
from matplotlib.style import use
from matplotlib.patches import Rectangle
from mpltools.annotation import slope_marker
from matplotlib.pyplot import subplots, show

data = load('../../../Currents_Resistances_Model_1/Current_Data_Model_1.npy')

use('../Show.mplstyle')

fig, ax = subplots()
ax.plot(data['pressure'][600, ::50], data['resistance'][600, ::50], linestyle='-')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Oxygen exchange resitance (a.u.)')

slope_marker(origin=(1e-14, 1e9), slope=-1, size_frac=0.1, invert=False, ax=ax)
ax.add_patch(Rectangle((1e1, 4e-1), 1e6, 4e-1, linewidth=0, facecolor='0.8'))
ax.text(1e3, 2e0, '0')

fig.tight_layout()
fig.savefig('Plots/Exchange_Resistance.pdf')
fig.savefig('Plots/Exchange_Resistance.png')


fig2, ax2 = subplots()
ax2_1 = ax2.twinx()

ax2.plot(data['pressure'][600, ::50], 1/data['resistance'][600, ::50], linestyle='-', label='1/Resistance')
ax2_1.plot([])
ax2_1.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50], linestyle='-', label='Exchange curent')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2_1.set_yscale('log')

ax2.set_ylim(1e-14, 1e2)
ax2_1.set_ylim(1e-14, 1e2)

ax2.set_xlabel('Oxygen partial pressure (bar)')
ax2.set_ylabel('1 / Oxygen exchange resitance (a.u.)')
ax2_1.set_ylabel('Oxygen exchange current density (a.u.)')

ax2.legend(loc=(0.5, 0.5))
ax2_1.legend(loc=(0.5, 0.6))

fig2.tight_layout()
fig2.savefig('Plots/Exchange_Resistance_Comparison.pdf')
fig2.savefig('Plots/Exchange_Resistance_Comparison.png')


fig3, ax3 = subplots()
ax3.plot(data['pressure'][600, ::50], data['ex_current'][600, ::50] * data['resistance'][600, ::50], linestyle='-')

ax3.set_xscale('log')

ax3.set_ylim(0, 0.02)

ax3.set_xlabel('Oxygen partial pressure (bar)')
ax3.set_ylabel('Excahnge current * exchange resistance')

fig3.tight_layout()
fig3.savefig('Plots/Current_Resistance_Ratio.pdf')
fig3.savefig('Plots/Current_Resistance_Ratio.png')


show()
