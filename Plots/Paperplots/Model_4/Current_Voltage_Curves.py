from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from Equations import e, k, T
from Semilog_Slope import semilog_slope
from matplotlib.ticker import LogLocator, NullFormatter


use('../Paper.mplstyle')

data = load('../../../Currents_Resistances_Model_4/Current_Data_Model_4.npy')

fig_abs_uh, ax_abs_uh = subplots()
fig_abs_hi, ax_abs_hi = subplots()
fig_abs_me, ax_abs_me = subplots()
fig_abs_lo, ax_abs_lo = subplots()

# Highest oxygen partial pressures
for i in (2300, 2200, 2100, 2000, 1900):
    ax_abs_uh.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                   label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

# High oxygen partial pressures
for i in (1800, 1700, 1600, 1500, 1400):
    ax_abs_hi.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                   label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

# Medium oxygen partial pressures
for i in (1300, 1200, 1100, 1000, 900):
    ax_abs_me.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                   label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))

# Low oxygen partial pressures
for i in (800, 700, 600, 500, 400):
    ax_abs_lo.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
                   label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))


semilog_slope(origin=(-0.1, 2e6), slope=-4*e/k/T, ax=ax_abs_uh, text=r'$\frac{4e}{kT}$', size=12)
semilog_slope(origin=(0.00, 1e2), slope=-4*e/k/T, ax=ax_abs_hi, text=r'$\frac{4e}{kT}$', size=12, frac=0.05)
semilog_slope(origin=(0.2, 1e-3), slope=4*e/k/T, ax=ax_abs_me, text=r'$\frac{4e}{kT}$', size=12, frac=0.05)
semilog_slope(origin=(0.3, 1e-7), slope=4*e/k/T, ax=ax_abs_lo, text=r'$\frac{4e}{kT}$', size=12)

ax_abs_uh.set_yscale('log')
ax_abs_hi.set_yscale('log')
ax_abs_me.set_yscale('log')
ax_abs_lo.set_yscale('log')

ax_abs_uh.set_ylim(1e-2, 1e10)
ax_abs_hi.set_ylim(1e-3, 1e5)
ax_abs_me.set_ylim(1e-7, 1e1)
ax_abs_lo.set_ylim(1e-11, 1e1)

ax_abs_lo.yaxis.set_major_locator(LogLocator(numticks=13))
ax_abs_lo.yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
ax_abs_lo.yaxis.set_minor_formatter(NullFormatter())

ax_abs_uh.yaxis.set_major_locator(LogLocator(numticks=13))
ax_abs_uh.yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
ax_abs_uh.yaxis.set_minor_formatter(NullFormatter())

for ax in (ax_abs_uh, ax_abs_hi, ax_abs_me, ax_abs_lo):
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlabel('Overpotential (V)')
    ax.set_xlim(-0.65, 0.65)
    ax.legend()

fig_abs_uh.tight_layout()
fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_4.pdf')
fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_4.png')

fig_abs_hi.tight_layout()
fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_4.pdf')
fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_4.png')

fig_abs_me.tight_layout()
fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_4.pdf')
fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_4.png')

fig_abs_lo.tight_layout()
fig_abs_lo.savefig('Plots/Current_Voltage_Curves_Abs_Lo_Model_4.pdf')
fig_abs_lo.savefig('Plots/Current_Voltage_Curves_Abs_Lo_Model_4.png')

show()
