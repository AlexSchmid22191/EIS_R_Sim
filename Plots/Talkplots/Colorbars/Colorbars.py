from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize, LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LinearLocator
import cmocean

use('../Talk.mplstyle')


p_fig, p_ax = subplots(figsize=(5, 1.5))
n_fig, n_ax = subplots(figsize=(5, 1.5))
b_fig, b_ax = subplots(figsize=(5, 1.5))

p_norm = Normalize(vmin=0, vmax=0.75)
n_norm = Normalize(vmin=-3, vmax=3)
b_norm = LogNorm(vmin=1e-12, vmax=1)

p_bar = ColorbarBase(p_ax, cmap='cmo.ice', norm=p_norm, orientation='horizontal')
n_bar = ColorbarBase(n_ax, cmap='cmo.balance', norm=n_norm, orientation='horizontal', extend='both')
b_bar = ColorbarBase(b_ax, cmap='cmo.ice', norm=b_norm, orientation='horizontal')

p_bar.ax.xaxis.set_major_locator(LinearLocator(numticks=4))

p_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\ln p_\mathrm{O_2}}$', fontsize=19)
n_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\eta}$', fontsize=19)
b_bar.set_label('Defects per unit cell', fontsize=19)

p_bar.ax.minorticks_off()
n_bar.ax.minorticks_off()
b_bar.ax.minorticks_off()

p_fig.tight_layout()
n_fig.tight_layout()
b_fig.tight_layout()

p_fig.savefig('Plots/cbar_p.png')
n_fig.savefig('Plots/cbar_n.png')
b_fig.savefig('Plots/cbar_b.png')

show()





#bar = ColorbarBase(ax_v, cmap='cmo.ice', norm=norm, orientation='horizontal')

#bar.set_label('Defects per unit cell')
#bar.ax.minorticks_off()