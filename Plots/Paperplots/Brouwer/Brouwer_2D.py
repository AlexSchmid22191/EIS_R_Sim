from matplotlib.colors import LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter
import cmocean


use('../Paper.mplstyle')


defect_data = load('../../../Brouwer/Brouwer_Bias.npy')

fig, axes = subplots(nrows=3, ncols=1, figsize=(3.25, 6.5), gridspec_kw={'height_ratios': [10, 10, 1]})

axes[0].set_title(r'a) Oxygen vacancies')
axes[1].set_title(r'b) Electron holes')

for ax in (axes[0], axes[1]):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())


colmesh_v = axes[0].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['vacancies'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap='cmo.ice')
colmesh_h = axes[1].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['holes'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap='cmo.ice')


norm = LogNorm(vmin=1e-12, vmax=1)

bar = ColorbarBase(axes[2], cmap='cmo.ice', norm=norm, orientation='horizontal')

bar.set_label('Defects per unit cell')
bar.ax.minorticks_off()

fig.tight_layout()
fig.savefig('Plots/2D_Brouwer_Combined.pdf')
fig.savefig('Plots/2D_Brouwer_Combined.png')
fig.savefig('Plots/2D_Brouwer_Combined.tiff', dpi=300)

show()