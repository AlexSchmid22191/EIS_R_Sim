from matplotlib.colors import LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, gradient

use('../Show.mplstyle')

defect_data = load('../../../Brouwer/Brouwer_Bias.npy')

fig, axes = subplots(nrows=2, ncols=2, figsize=(12, 8))

for ax in axes.flatten():
    ax.set_xscale('log')
    ax.set_xlabel('Oxygen partial pressure (bar)')
    ax.set_ylabel('Overpotential (V)')


colmesh_v = axes[0, 0].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['vacancies'],
                                  norm=LogNorm(), vmin=1e-12, vmax=1)
colmesh_h = axes[0, 1].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['holes'],
                                  norm=LogNorm(), vmin=1e-8, vmax=1)
colmesh_e = axes[1, 0].pcolormesh(defect_data['pressure'], defect_data['overpotential'], defect_data['electrons'],
                                  norm=LogNorm(), vmin=1e-8, vmax=1)

cbar_v = fig.colorbar(colmesh_v, ax=axes[0, 0], label=r'Oxygen vacancies')
cbar_h = fig.colorbar(colmesh_h, ax=axes[0, 1], label=r'Electron holes')
cbar_e = fig.colorbar(colmesh_e, ax=axes[1, 0], label=r'Electrons')
cbar_v.ax.minorticks_off()
cbar_h.ax.minorticks_off()
cbar_e.ax.minorticks_off()

fig.tight_layout()
fig.savefig('Plots/2D_Brouwer.png')
show()
