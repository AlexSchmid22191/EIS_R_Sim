from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LogLocator, NullFormatter, FixedLocator
from mpltools.annotation import slope_marker
from numpy import load

from Equations import e, k, T
from Semilog_Slope import semilog_slope

defect_data = load('../../../Brouwer/Brouwer_Ideal.npy')

# Create some views
po = defect_data['pressure'][000:4300:100]
vac = defect_data['vacancies'][000:4300:100]
hol = defect_data['holes'][000:4300:100]
ele = defect_data['electrons'][000:4300:100]
ox = 3 - defect_data['vacancies'][000:4300:100]
fe = 1 - defect_data['holes'][000:4300:100] - defect_data['electrons'][000:4300:100]


use('../Thesis.mplstyle')

fig, ax_p = subplots(figsize=(4, 3.5))

ax_p.plot(po, vac, linestyle='-', label=r'$\mathrm{V}_\mathrm{O}^\mathrm{\cdot\cdot}$')
ax_p.plot(po, hol, linestyle='-', label=r'$\mathrm{h}^\mathrm{\cdot}$')
ax_p.plot(po, ele, linestyle='-', label=r"$\mathrm{e}^\mathrm{'}$")
ax_p.plot(po, ox, linestyle='-', label=r'$\mathrm{O}_\mathrm{O}^\mathrm{x}$')
ax_p.plot(po, fe, linestyle='-', label=r'$\mathrm{Fe}_\mathrm{Fe}^\mathrm{x}$')

ax_p.set_xscale('log')
ax_p.set_yscale('log')

ax_p.set_xlim(1e-30, 1e6)
ax_p.set_ylim(1e-8, 1e2)

slope_marker((1e-2, 5e-2), -0.5, ax=ax_p)
slope_marker((1e-20, 1.5e-4), 0.25, ax=ax_p, invert=True)
slope_marker((1e-24, 3e-2), -0.25, ax=ax_p)

ax_p.set_xlabel('Oxygen partial pressure (bar)')
ax_p.set_ylabel('Defects/Ions per unit cell')

ax_p.legend(ncol=2, loc=(0.15, 0.0))

ax_m = ax_p.twiny()
ax_m.set_xlabel('Oxygen chemical potential (eV)')
ax_m.set_xlim(defect_data['oxygenpot'][600]*2, defect_data['oxygenpot'][4201]*2)

semilog_slope((-0.4, 1e-4), slope=-0.5*e/k/T, ax=ax_m, text=r'$-\frac{1}{2kT}$', inverted=True)
semilog_slope((-3.4, 6e-6), slope=0.25*e/k/T, ax=ax_m, text=r'$\frac{1}{4kT}$')
semilog_slope((-4.2, 1e-3), slope=-0.25*e/k/T, ax=ax_m, text=r'$-\frac{1}{4kT}$', inverted=True)

ax_p.xaxis.set_major_locator(LogLocator(numticks=6))
ax_p.xaxis.set_minor_locator(LogLocator(numticks=36))
ax_p.xaxis.set_minor_formatter(NullFormatter())

ax_p.yaxis.set_major_locator(LogLocator(numticks=12))
ax_p.yaxis.set_minor_locator(LogLocator(numticks=12, subs=range(10)))

for index, label in enumerate(ax_p.yaxis.get_ticklabels()):
    if index % 2 != 1:
        label.set_visible(False)

fig.tight_layout()
fig.savefig('Plots/Brouwer.pdf')
fig.savefig('Plots/Brouwer.png')
fig.savefig('Plots/Brouwer.tiff', dpi=300)

show()