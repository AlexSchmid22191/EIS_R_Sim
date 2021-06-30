from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from matplotlib.ticker import LinearLocator
import cmocean

use('../Paper.mplstyle')


p_fig, p_ax = subplots(figsize=(0.875, 3.268))
n_fig, n_ax = subplots(figsize=(0.875, 3.268))

p_norm = Normalize(vmin=0, vmax=0.75)
n_norm = Normalize(vmin=-3, vmax=3)

p_bar = ColorbarBase(p_ax, cmap='cmo.ice', norm=p_norm, orientation='vertical')
n_bar = ColorbarBase(n_ax, cmap='cmo.balance', norm=n_norm, orientation='vertical', extend='both')

p_bar.ax.yaxis.set_major_locator(LinearLocator(numticks=4))

p_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\ln p}$')
n_bar.set_label(r'$\frac{\mathrm{d}\ln\left|j\right|}{\mathrm{d}\eta}$')

p_bar.ax.minorticks_off()
n_bar.ax.minorticks_off()

p_fig.tight_layout()
n_fig.tight_layout()

p_fig.savefig('Plots/cbar_p.png')
p_fig.savefig('Plots/cbar_p.pdf')
n_fig.savefig('Plots/cbar_n.png')
n_fig.savefig('Plots/cbar_n.pdf')

show()
