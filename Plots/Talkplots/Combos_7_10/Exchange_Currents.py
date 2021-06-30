from numpy import load
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LogLocator, NullFormatter
from mpltools.annotation import slope_marker
import cmocean

use('../Talk.mplstyle')

data_7 = load('../../../Currents_Resistances_Model_7/Current_Data_Model_7.npy')
data_10 = load('../../../Currents_Resistances_Model_10/Current_Data_Model_10.npy')


fig_at, ax_at = subplots()
fig_mo, ax_mo = subplots()


ax_at.set_title(r'a) Atomic mechanism')
ax_mo.set_title(r'b) Molecular mechanism')

ax_at.set_ylim(1e-7, 1e1)
ax_mo.set_ylim(1e-10, 1e6)

for ax in (ax_at, ax_mo):
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Exchange current density (a.u.)')
    ax.set_xlim(1e-18, 1e6)
    ax.xaxis.set_major_locator(LogLocator(numticks=4))
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.yaxis.set_major_locator(LogLocator(numticks=5))
    ax.yaxis.set_minor_formatter(NullFormatter())

ax_at.yaxis.set_minor_locator(LogLocator(numticks=9))
ax_mo.yaxis.set_minor_locator(LogLocator(numticks=17))

ax_at.plot(data_10['pressure'][600, ::100], data_10['ex_current'][600, ::100], linestyle='-')
ax_mo.plot(data_7['pressure'][600, ::100], data_7['ex_current'][600, ::100], linestyle='-')

slope_marker(origin=(1e-12, 1e-5), slope=0.5, ax=ax_at, size_frac=0.2)
slope_marker(origin=(3e-3, 1e1), slope=0.5, ax=ax_mo, size_frac=0.2)
slope_marker(origin=(1e-15, 1e-8), slope=0.75, ax=ax_mo, size_frac=0.2)

fig_at.tight_layout()
fig_at.tight_layout()

fig_at.savefig('Plots/Exchange_Current_7_10.png')
fig_at.savefig('Plots/Exchange_Current_7_10.png')

show()
