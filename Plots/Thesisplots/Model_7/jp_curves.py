from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from mpltools.annotation import slope_marker
from numpy import load
import cmocean

use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

fig_an, ax_an = subplots()
fig_cat, ax_cat = subplots()

for i in range(100, 600, 100):
    ax_cat.plot(data['pressure'][i, ::50], abs(data['current'][i, ::50]), linestyle='-',
                label='{:3.0f} mV'.format(data['overpotential'][i, 0]*1000))

for i in range(700, 1200, 100):
    ax_an.plot(data['pressure'][i, ::50], abs(data['current'][i, ::50]), linestyle='-',
               label='{:3.0f} mV'.format(data['overpotential'][i, 0]*1000))


for ax in ax_an, ax_cat:
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim(1e-18, 1e6)
    ax.legend()

ax_an.set_ylim(1e-8, 1e13)
ax_cat.set_ylim(1e-9, 1e12)

slope_marker((1e0, 1e3), 0.5, invert=False, size_frac=0.1, ax=ax_an)
slope_marker((1e-13, 1e-5), 0.75, invert=False, size_frac=0.1, ax=ax_an)

slope_marker((1e-13, 1e-6), 0.75, invert=False, size_frac=0.1, ax=ax_cat)
slope_marker((1e1, 3e4), 0.5, invert=False, size_frac=0.1, ax=ax_cat)

fig_an.tight_layout()
fig_an.savefig('Plots/jp_Curves_An_Model_7.pdf')
fig_an.savefig('Plots/jp_Curves_An_Model_7.png')

fig_cat.tight_layout()
fig_cat.savefig('Plots/jp_Curves_Cat_Model_7.pdf')
fig_cat.savefig('Plots/jp_Curves_Cat_Model_7.png')

show()
