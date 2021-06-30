from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from Equations import e, k, T
from Semilog_Slope import semilog_slope
from matplotlib.ticker import LogLocator, NullFormatter, MultipleLocator

use('../Talk.mplstyle')

data = load('../../../Currents_Resistances_Model_6/Current_Data_Model_6.npy')


fig_abs_uh, ax_abs_uh = subplots()
fig_abs_hi, ax_abs_hi = subplots()
fig_abs_me, ax_abs_me = subplots()
fig_abs_lo, ax_abs_lo = subplots()

# Highest oxygen partial pressures
for i in (2300, 2200, 2100, 2000, 1900):
    ax_abs_uh.plot(data['overpotential'][::50, i], abs(data['current'][::50, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (2300, 2200, 2100, 2000, 1900):
    ax_abs_uh.plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# High oxygen partial pressures
for i in (1800, 1700, 1600, 1500, 1400):
    ax_abs_hi.plot(data['overpotential'][::50, i], abs(data['current'][::50, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (1800, 1700, 1600, 1500, 1400):
    ax_abs_hi.plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# Medium oxygen partial pressures
for i in (1300, 1200, 1100, 1000, 900):
    ax_abs_me.plot(data['overpotential'][::50, i], abs(data['current'][::50, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (1300, 1200, 1100, 1000, 900):
    ax_abs_me.plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# Low oxygen partial pressures
for i in (800, 700, 600, 500, 400):
    ax_abs_lo.plot(data['overpotential'][::50, i], abs(data['current'][::50, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (800, 700, 600, 500, 400):
    ax_abs_lo.plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')


semilog_slope(origin=(-0.1, 1e9), slope=-2*e/k/T, ax=ax_abs_uh, text=r'$-\frac{2e}{kT}$', size=18, inverted=False)
semilog_slope(origin=(-0.45, 1e6), slope=-1*e/k/T, ax=ax_abs_uh, text=r'$-\frac{e}{kT}$', size=18, inverted=True)
semilog_slope(origin=(0.3, 1e11), slope=2*e/k/T, ax=ax_abs_uh, text=r'$\frac{2e}{kT}$', size=18, inverted=True)

semilog_slope(origin=(-0.4, 1e2), slope=-1*e/k/T, ax=ax_abs_hi, text=r'$-\frac{e}{kT}$', size=18, inverted=True)
semilog_slope(origin=(0.4, 1e3), slope=2*e/k/T, ax=ax_abs_hi, text=r'$\frac{2e}{kT}$', size=18, inverted=False)

semilog_slope(origin=(-0.5, 1e2), slope=-2*e/k/T, ax=ax_abs_me, text=r'$-\frac{2e}{kT}$', size=18, inverted=True)

semilog_slope(origin=(0.25, 1e-5), slope=3*e/k/T, ax=ax_abs_lo, text=r'$\frac{3e}{kT}$', size=18, inverted=False)
semilog_slope(origin=(0.35, 2e4), slope=2*e/k/T, ax=ax_abs_lo, text=r'$\frac{2e}{kT}$', size=18, inverted=True)
semilog_slope(origin=(-0.325, 1e-6), slope=-1*e/k/T, ax=ax_abs_lo, text=r'$-\frac{e}{kT}$', size=18, inverted=True)


ax_abs_uh.set_yscale('log')
ax_abs_hi.set_yscale('log')
ax_abs_me.set_yscale('log')
ax_abs_lo.set_yscale('log')

ax_abs_uh.set_ylim(1e1, 1e13)
ax_abs_hi.set_ylim(1e-1, 1e10)
ax_abs_me.set_ylim(1e-4, 1e8)
ax_abs_lo.set_ylim(1e-8, 1e6)

ax_abs_uh.yaxis.set_major_locator(LogLocator(numticks=7))
ax_abs_uh.yaxis.set_minor_locator(LogLocator(numticks=13))
ax_abs_uh.yaxis.set_minor_formatter(NullFormatter())

ax_abs_hi.yaxis.set_major_locator(LogLocator(numticks=7))
ax_abs_hi.yaxis.set_minor_locator(LogLocator(numticks=13))
ax_abs_hi.yaxis.set_minor_formatter(NullFormatter())

ax_abs_me.yaxis.set_major_locator(LogLocator(numticks=7))
ax_abs_me.yaxis.set_minor_locator(LogLocator(numticks=13))
ax_abs_me.yaxis.set_minor_formatter(NullFormatter())

ax_abs_lo.yaxis.set_major_locator(LogLocator(numticks=8))
ax_abs_lo.yaxis.set_minor_locator(LogLocator(numticks=15))
ax_abs_lo.yaxis.set_minor_formatter(NullFormatter())

for ax in (ax_abs_uh, ax_abs_hi, ax_abs_me, ax_abs_lo):
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlabel('Overpotential (V)')
    ax.set_xlim(-0.65, 0.65)
    ax.xaxis.set_major_locator(MultipleLocator(0.2))

ax_abs_uh.legend(loc=(0.725, 0.00))
ax_abs_hi.legend(loc=(0.35, 0.475))
ax_abs_me.legend()
ax_abs_lo.legend(loc=(0.275, 0.45))


fig_abs_uh.tight_layout()
fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_6.png')

fig_abs_hi.tight_layout()
fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_6.png')

fig_abs_me.tight_layout()
fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_6.png')
fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_6.pdf', transparent=True)

fig_abs_lo.tight_layout()
fig_abs_lo.savefig('Plots/Current_Voltage_Curves_Abs_Lo_Model_6.png')

show()