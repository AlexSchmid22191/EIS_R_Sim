from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10
from Equations import e, k, T
from Semilog_Slope import semilog_slope
from matplotlib.ticker import LogLocator, NullFormatter, MultipleLocator
from matplotlib.patches import Rectangle

use('../Thesis_Small.mplstyle')

data = load('../../../Currents_Resistances_Model_8/Current_Data_Model_8.npy')


# ----------------------------------------------------------------------------------------------------------------------
#
#
# fig_abs_uh, ax_abs_uh = subplots()
# fig_abs_hi, ax_abs_hi = subplots()
# fig_abs_me, ax_abs_me = subplots()
# fig_abs_lo, ax_abs_lo = subplots()
#
# # Highest oxygen partial pressures
# for i in (2300, 2200, 2100, 2000, 1900):
#     ax_abs_uh.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
#                    label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
#
# # High oxygen partial pressures
# for i in (1800, 1700, 1600, 1500, 1400):
#     ax_abs_hi.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
#                    label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
#
# # Medium oxygen partial pressures
# for i in (1300, 1200, 1100, 1000, 900):
#     ax_abs_me.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
#                    label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
#
# # Low oxygen partial pressures
# for i in (800, 700, 600, 500, 400):
#     ax_abs_lo.plot(data['overpotential'][1::25, i], abs(data['current'][1::25, i]), linestyle='-',
#                    label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
#
# ax_abs_uh.text(-0.475, 2e4, '0')
# ax_abs_uh.add_patch(Rectangle((-0.6, 5e3), 0.25, 5e3, linewidth=0, facecolor='0.8'))
# semilog_slope(origin=(-0.05, 1e3), slope=-2*e/k/T, ax=ax_abs_uh, text=r'$\frac{2e}{kT}$', size=12, inverted=False)
# semilog_slope(origin=(0.5, 1e2), slope=2*e/k/T, ax=ax_abs_uh, text=r'$\frac{2e}{kT}$', size=12, inverted=False)
#
# ax_abs_hi.text(-0.475, 2e4, '0')
# ax_abs_hi.add_patch(Rectangle((-0.6, 5e3), 0.25, 5e3, linewidth=0, facecolor='0.8'))
# semilog_slope(origin=(-0.3, 5e1), slope=-1*e/k/T, ax=ax_abs_hi, text=r'$\frac{e}{kT}$', size=12, inverted=True)
# semilog_slope(origin=(0.4, 1e3), slope=2*e/k/T, ax=ax_abs_hi, text=r'$\frac{2e}{kT}$', size=12, inverted=False)
#
# semilog_slope(origin=(0.5, 1e2), slope=2*e/k/T, ax=ax_abs_me, text=r'$\frac{2e}{kT}$', size=12, inverted=False)
# semilog_slope(origin=(0.2, 1e-2), slope=3*e/k/T, ax=ax_abs_me, text=r'$\frac{3e}{kT}$', size=12, inverted=False)
# semilog_slope(origin=(-0.5, 1e-1), slope=-1*e/k/T, ax=ax_abs_me, text=r'$\frac{e}{kT}$', size=12, inverted=True)
#
# semilog_slope(origin=(0.25, 1e-5), slope=3*e/k/T, ax=ax_abs_lo, text=r'$\frac{3e}{kT}$', size=12, inverted=False)
# semilog_slope(origin=(0.35, 1e4), slope=2*e/k/T, ax=ax_abs_lo, text=r'$\frac{2e}{kT}$', size=12, inverted=True)
# semilog_slope(origin=(-0.3, 1e-6), slope=-1*e/k/T, ax=ax_abs_lo, text=r'$\frac{e}{kT}$', size=12, inverted=True)
#
# ax_abs_uh.set_yscale('log')
# ax_abs_hi.set_yscale('log')
# ax_abs_me.set_yscale('log')
# ax_abs_lo.set_yscale('log')
#
# ax_abs_uh.set_ylim(1e-3, 1e8)
# ax_abs_hi.set_ylim(1e-1, 1e11)
# ax_abs_me.set_ylim(1e-4, 1e8)
# ax_abs_lo.set_ylim(1e-8, 1e6)
#
# ax_abs_lo.yaxis.set_major_locator(LogLocator(numticks=13))
# ax_abs_lo.yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
# ax_abs_lo.yaxis.set_minor_formatter(NullFormatter())
#
# ax_abs_uh.yaxis.set_major_locator(LogLocator(numticks=13))
# ax_abs_uh.yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
# ax_abs_uh.yaxis.set_minor_formatter(NullFormatter())
#
# for ax in (ax_abs_uh, ax_abs_hi, ax_abs_me, ax_abs_lo):
#     ax.set_ylabel('Absolute current density (a.u.)')
#     ax.set_xlabel('Overpotential (V)')
#     ax.set_xlim(-0.65, 0.65)
#     ax.legend()
#
# fig_abs_uh.tight_layout()
# fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_8.pdf')
# fig_abs_uh.savefig('Plots/Current_Voltage_Curves_Abs_Uh_Model_8.png')
#
# fig_abs_hi.tight_layout()
# fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_8.pdf')
# fig_abs_hi.savefig('Plots/Current_Voltage_Curves_Abs_Hi_Model_8.png')
#
# fig_abs_me.tight_layout()
# fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_8.pdf')
# fig_abs_me.savefig('Plots/Current_Voltage_Curves_Abs_Me_Model_8.png')
#
# fig_abs_lo.tight_layout()
# fig_abs_lo.savefig('Plots/Current_Voltage_Curves_Abs_Lo_Model_8.pdf')
# fig_abs_lo.savefig('Plots/Current_Voltage_Curves_Abs_Lo_Model_8.png')


# ----------------------------------------------------------------------------------------------------------------------


fig_abs_co, ax_abs_co = subplots(nrows=2, ncols=2, figsize=(5.75, 5))

# Highest oxygen partial pressures
for i in (2300, 2200, 2100, 2000, 1900):
    ax_abs_co[0, 0].plot(data['overpotential'][::25, i], abs(data['current'][::25, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (2300, 2200, 2100, 2000, 1900):
    ax_abs_co[0, 0].plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# High oxygen partial pressures
for i in (1800, 1700, 1600, 1500, 1400):
    ax_abs_co[0, 1].plot(data['overpotential'][::25, i], abs(data['current'][::25, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (1800, 1700, 1600, 1500, 1400):
    ax_abs_co[0, 1].plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# Medium oxygen partial pressures
for i in (1300, 1200, 1100, 1000, 900):
    ax_abs_co[1, 0].plot(data['overpotential'][::25, i], abs(data['current'][::25, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (1300, 1200, 1100, 1000, 900):
    ax_abs_co[1, 0].plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

# Low oxygen partial pressures
for i in (800, 700, 600, 500, 400):
    ax_abs_co[1, 1].plot(data['overpotential'][::25, i], abs(data['current'][::25, i]),
                         label='$10^{%d}$ bar' % log10(data['pressure'][1, i]))
for i in (800, 700, 600, 500, 400):
    ax_abs_co[1, 1].plot(data['overpotential'][:, i], abs(data['current'][:, i]), linestyle='-', marker='')

ax_abs_co[0, 0].text(-0.475, 2e4, '0')
ax_abs_co[0, 0].add_patch(Rectangle((-0.6, 5e3), 0.25, 5e3, linewidth=0, facecolor='0.8'))
semilog_slope(origin=(-0.3, 1e0), slope=-2*e/k/T, ax=ax_abs_co[0, 0], text=r'$-\frac{2e}{kT}$', size=12, inverted=True)
semilog_slope(origin=(0.3, 1e6), slope=2*e/k/T, ax=ax_abs_co[0, 0], text=r'$\frac{2e}{kT}$', size=12, inverted=True)

ax_abs_co[0, 1].text(-0.475, 2e4, '0')
ax_abs_co[0, 1].add_patch(Rectangle((-0.6, 5e3), 0.25, 5e3, linewidth=0, facecolor='0.8'))
semilog_slope(origin=(-0.3, 5e1), slope=-1*e/k/T, ax=ax_abs_co[0, 1], text=r'$-\frac{e}{kT}$', size=12, inverted=True)
semilog_slope(origin=(0.5, 4e4), slope=2*e/k/T, ax=ax_abs_co[0, 1], text=r'$\frac{2e}{kT}$', size=12, inverted=False)

semilog_slope(origin=(0.5, 1e2), slope=2*e/k/T, ax=ax_abs_co[1, 0], text=r'$\frac{2e}{kT}$', size=12, inverted=False)
semilog_slope(origin=(0.2, 1e-2), slope=3*e/k/T, ax=ax_abs_co[1, 0], text=r'$\frac{3e}{kT}$', size=12, inverted=False)
semilog_slope(origin=(-0.4, 1e-2), slope=-1*e/k/T, ax=ax_abs_co[1, 0], text=r'$-\frac{e}{kT}$', size=12, inverted=True)

semilog_slope(origin=(0.25, 1e-5), slope=3*e/k/T, ax=ax_abs_co[1, 1], text=r'$\frac{3e}{kT}$', size=12, inverted=False)
semilog_slope(origin=(0.30, 1e4), slope=2*e/k/T, ax=ax_abs_co[1, 1], text=r'$\frac{2e}{kT}$', size=12, inverted=True)
semilog_slope(origin=(-0.3, 1e-6), slope=-1*e/k/T, ax=ax_abs_co[1, 1], text=r'$-\frac{e}{kT}$', size=12, inverted=True)


ax_abs_co[0, 0].set_yscale('log')
ax_abs_co[0, 1].set_yscale('log')
ax_abs_co[1, 0].set_yscale('log')
ax_abs_co[1, 1].set_yscale('log')

ax_abs_co[0, 0].set_title(r'(a) Very high $p_\mathrm{O_2}$', color='#006699')
ax_abs_co[0, 1].set_title(r'(b) High $p_\mathrm{O_2}$', color='#006699')
ax_abs_co[1, 0].set_title(r'(c) Medium $p_\mathrm{O_2}$', color='#006699')
ax_abs_co[1, 1].set_title(r'(d) Low $p_\mathrm{O_2}$', color='#006699')

ax_abs_co[0, 0].set_ylim(1e-3, 1e9)
ax_abs_co[0, 1].set_ylim(1e0, 1e10)
ax_abs_co[1, 0].set_ylim(1e-4, 1e8)
ax_abs_co[1, 1].set_ylim(1e-8, 1e6)


ax_abs_co[0, 0].yaxis.set_major_locator(LogLocator(numticks=13))
ax_abs_co[0, 0].yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
ax_abs_co[0, 0].yaxis.set_minor_formatter(NullFormatter())

ax_abs_co[0, 1].yaxis.set_major_locator(LogLocator(numticks=12))
ax_abs_co[0, 1].yaxis.set_minor_locator(LogLocator(numticks=12, subs=range(1, 10)))
ax_abs_co[0, 1].yaxis.set_minor_formatter(NullFormatter())

ax_abs_co[1, 0].yaxis.set_major_locator(LogLocator(numticks=13))
ax_abs_co[1, 0].yaxis.set_minor_locator(LogLocator(numticks=13, subs=range(1, 10)))
ax_abs_co[1, 0].yaxis.set_minor_formatter(NullFormatter())

ax_abs_co[1, 1].yaxis.set_major_locator(LogLocator(numticks=15))
ax_abs_co[1, 1].yaxis.set_minor_locator(LogLocator(numticks=15, subs=range(1, 10)))
ax_abs_co[1, 1].yaxis.set_minor_formatter(NullFormatter())


for ax in (ax_abs_co[0, 0], ax_abs_co[0, 1], ax_abs_co[1, 0], ax_abs_co[1, 1]):
    ax.set_ylabel('Absolute current density (a.u.)')
    ax.set_xlabel('Overpotential (V)')
    ax.set_xlim(-0.65, 0.65)
    ax.xaxis.set_major_locator(MultipleLocator(base=0.2))
    ax.xaxis.set_minor_locator(MultipleLocator(base=0.05))
    ax.legend()

    for label in ax.yaxis.get_ticklabels()[::2]:
        label.set_visible(False)

ax_abs_co[0, 0].legend(loc=(0.7, 0.0))
ax_abs_co[0, 1].legend(loc=(0.7, 0.0))
ax_abs_co[1, 0].legend(loc=(0.2, 0.55))
ax_abs_co[1, 1].legend(loc=(0.1, 0.55))

fig_abs_co.tight_layout()
fig_abs_co.savefig('Plots/Current_Voltage_Curves_Co_Model_8.pdf')
fig_abs_co.savefig('Plots/Current_Voltage_Curves_Co_Model_8.png')
fig_abs_co.savefig('Plots/Current_Voltage_Curves_Co_Model_8.tiff', dpi=300)

# ----------------------------------------------------------------------------------------------------------------------


show()
