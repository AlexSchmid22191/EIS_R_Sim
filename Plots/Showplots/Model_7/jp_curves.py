from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from mpltools.annotation import slope_marker
from numpy import load

use('../Show.mplstyle')

data = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')

fig_an, ax_an = subplots(figsize=(6, 4))
fig_cat, ax_cat = subplots(figsize=(6, 4))

# Anodic bias
for i in range(700, 1101, 100):
    ax_an.plot(data['pressure'][i, ::50], abs(data['current'][i, ::50]), linestyle='-',
               label='{:3.0f} mV'.format(data['overpotential'][i, 0]*1000))


for i in range(100, 600, 100):
    ax_cat.plot(data['pressure'][i, ::50], abs(data['current'][i, ::50]), linestyle='-',
                label='{:3.0f} mV'.format(data['overpotential'][i, 0]*1000))

for ax in (ax_an, ax_cat):
    ax.set_xlabel('Oxygen aprtial pressure (bar)')
    ax.set_ylabel('Current density (a.u.)')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(1e-9, 1e15)
    ax.legend()

slope_marker(origin=(1e0, 1e3), slope=0.5, ax=ax_an)
slope_marker(origin=(1e-12, 1e-5), slope=0.75, ax=ax_an)

slope_marker(origin=(1e1, 1e4), slope=0.5, ax=ax_cat)
slope_marker(origin=(1e-12, 1e-5), slope=0.75, ax=ax_cat)

#
# fig_hi.tight_layout()
# fig_hi.savefig('Plots/Current_Voltage_Curves_Hi.pdf')
# fig_hi.savefig('Plots/Current_Voltage_Curves_Hi.png')
#
# fig_me.tight_layout()
# fig_me.savefig('Plots/Current_Voltage_Curves_Me.pdf')
# fig_me.savefig('Plots/Current_Voltage_Curves_Me.png')
#
# fig_lo.tight_layout()
# fig_lo.savefig('Plots/Current_Voltage_Curves_Lo.pdf')
# fig_lo.savefig('Plots/Current_Voltage_Curves_Lo.png')
#
show()