from matplotlib.colors import LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter, LinearLocator
from Plots.TU_Colormaps import trunc_blue

use('../Thesis_Small.mplstyle')


defect_data = load('../../../Brouwer/Brouwer_Bias.npy')

fig, axes = subplots(nrows=1, ncols=3, figsize=(5.75, 2.5), gridspec_kw={'width_ratios': [30, 30, 1]},
                     constrained_layout=True)

axes[0].set_title(r'(a) Oxygen vacancies', color='#006699')
axes[1].set_title(r'(b) Electron holes', color='#006699')

for ax in (axes[0], axes[1]):
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')
    ax.set_xlim(1e-18, 1e6)
    ax.set_ylim(-0.6, 0.6)
    ax.xaxis.set_major_locator(LogLocator(numticks=4))
    ax.xaxis.set_minor_locator(LogLocator(numticks=24))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.yaxis.set_minor_locator(LinearLocator(numticks=25))


colmesh_v = axes[0].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['vacancies'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap=trunc_blue)
colmesh_h = axes[1].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['holes'],
                               norm=LogNorm(), vmin=1e-12, vmax=1, cmap=trunc_blue)


norm = LogNorm(vmin=1e-12, vmax=1)
bar = ColorbarBase(axes[2], cmap=trunc_blue, norm=norm, orientation='vertical')

bar.set_label('Defects per unit cell')
bar.ax.minorticks_off()

# fig.savefig('Plots/2D_Brouwer_Combined.pdf')
fig.savefig('Plots/2D_Brouwer_Combined.png')
# fig.savefig('Plots/2D_Brouwer_Combined.tiff', dpi=300)

show()