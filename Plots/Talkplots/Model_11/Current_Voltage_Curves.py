from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from Equations import e, k, T
from Semilog_Slope import semilog_slope
from matplotlib.ticker import LogLocator, NullFormatter, MultipleLocator


use('../Talk.mplstyle')

data = load('../../../Currents_Resistances_Model_11/Current_Data_Model_11.npy')


# ----------------------------------------------------------------------------------------------------------------------


fig_abs_uh, ax_abs_uh = subplots()
fig_abs_hi, ax_abs_hi = subplots()


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


semilog_slope(origin=(-0.05, 1e1), slope=-2*e/k/T, ax=ax_abs_uh, text=r'$\frac{2e}{kT}$', size=18, inverted=False)

semilog_slope(origin=(-0.025, 2e1), slope=-2*e/k/T, ax=ax_abs_hi, text=r'$\frac{2e}{kT}$', size=18, inverted=False)


ax_abs_uh.set_yscale('log')
ax_abs_hi.set_yscale('log')

ax_abs_uh.set_ylim(1e-5, 1e2)
ax_abs_hi.set_ylim(1e-3, 1e2)

ax_abs_uh.yaxis.set_major_locator(LogLocator(numticks=8))
ax_abs_uh.yaxis.set_minor_locator(LogLocator(numticks=8))
ax_abs_uh.yaxis.set_minor_formatter(NullFormatter())

ax_abs_hi.yaxis.set_major_locator(LogLocator(numticks=6))
ax_abs_hi.yaxis.set_minor_locator(LogLocator(numticks=6))
ax_abs_hi.yaxis.set_minor_formatter(NullFormatter())

for ax in (ax_abs_uh, ax_abs_hi):
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlabel('Overpotential (V)')
    ax.set_xlim(-0.65, 0.65)
    ax.xaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend()

fig_abs_uh.tight_layout()
fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_11.png')

fig_abs_hi.tight_layout()
fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_11.png')

show()
