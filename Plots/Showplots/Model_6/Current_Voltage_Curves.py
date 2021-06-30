from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10

use('../Show.mplstyle')

data = load('../../../Currents_Resistances_Model_6/Current_Data_Model_6.npy')

fig_hi, ax_hi = subplots(nrows=2, figsize=(6, 8))
fig_me, ax_me = subplots(nrows=2, figsize=(6, 8))
fig_lo, ax_lo = subplots(nrows=2, figsize=(6, 8))


# High oxygen partial pressures
for i in (1400, 1500, 1600, 1700, 1800):
    ax_hi[0].plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

    ax_hi[1].plot(data['overpotential'][0::25, i], data['current'][0::25, i], linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

# Medium oxygen partial pressures
for i in (1000, 1100, 1200, 1300):
    ax_me[0].plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
    ax_me[1].plot(data['overpotential'][0::25, i], data['current'][0::25, i], linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

# Low oxygen partial pressures
for i in (500, 600, 700, 800, 900):
    ax_lo[0].plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
    ax_lo[1].plot(data['overpotential'][0::25, i], data['current'][0::25, i], linestyle='-',
                  label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))


ax_hi[0].set_yscale('log')
ax_me[0].set_yscale('log')
ax_lo[0].set_yscale('log')
ax_hi[1].set_yscale('symlog', linthreshy=1e-1)
ax_me[1].set_yscale('symlog', linthreshy=1e-4)
ax_lo[1].set_yscale('symlog', linthreshy=1e-9)

# ax_hi[0].set_ylim(1e-3, 1e5)
# ax_hi[1].set_ylim(-1e5, 1e0)
# ax_me[0].set_ylim(1e-6, 1e0)
# ax_me[1].set_ylim(-1e0, 1e0)
# ax_lo[0].set_ylim(1e-10, 1e0)
# ax_lo[1].set_ylim(-1e-4, 1e1)

for ax in (ax_hi[0], ax_hi[1], ax_me[0], ax_me[1], ax_lo[0], ax_lo[1]):
    ax.set_ylabel('Absolute current density (A/m²)')
    ax.set_xlabel('Overpotential (V)')
    ax.legend()


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

show()

