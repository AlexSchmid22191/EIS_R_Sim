from matplotlib.colors import LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter, FixedLocator
import cmocean


use('../Talk.mplstyle')


defect_data = load('../../../Brouwer/Brouwer_Bias.npy')

fig_v, ax_v = subplots()
fig_h, ax_h = subplots()

ax_v.set_title(r'Oxygen vacancies')
ax_h.set_title(r'Electron holes')

for ax in (ax_v, ax_h):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_major_locator(FixedLocator(locs=[10**n for n in range(-24, 7, 6)]))
    ax.xaxis.set_minor_locator(LogLocator(numticks=25))
    ax.xaxis.set_minor_formatter(NullFormatter())


colmesh_v = ax_v.pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['vacancies'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap='cmo.ice')
colmesh_h = ax_h.pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['holes'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap='cmo.ice')


fig_v.tight_layout()
fig_v.savefig('Plots/2D_Brouwer_Vacancies.png')
fig_h.tight_layout()
fig_h.savefig('Plots/2D_Brouwer_Holes.png')

show()