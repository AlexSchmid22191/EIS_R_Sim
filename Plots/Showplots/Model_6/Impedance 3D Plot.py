from matplotlib.pyplot import figure, show
from matplotlib.ticker import LinearLocator, ScalarFormatter, FixedFormatter
from matplotlib.style import use
from mpl_toolkits.mplot3d import proj3d
from numpy import load, log10, array


data = load('../../../Currents_Resistances_Model_6/Current_Data_Model_6.npy')

logp = log10(data['pressure'])
logz = log10(data['resistance'])

use('../Show.mplstyle')


def orthogonal_proj(zfront, zback):
    a = (zfront + zback) / (zfront - zback)
    b = -2 * (zfront * zback) / (zfront - zback)
    return array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, a, b],
                  [0, 0, -0.0001, zback]])


proj3d.persp_transformation = orthogonal_proj

fig = figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=25, azim=145)

ax.plot_surface(data['overpotential'], logp, logz, cmap='viridis', alpha=0.4)

ax.set_xlabel('Overpotential (V)')
ax.set_ylabel('Oxygen partial pressure (bar)')
ax.set_zlabel('Polarisation resistance (a.u.)')

ax.xaxis.set_major_locator(LinearLocator(numticks=4))
ax.xaxis.set_major_formatter(ScalarFormatter())

ax.yaxis.set_major_locator(LinearLocator(numticks=6))
ax.yaxis.set_major_formatter(FixedFormatter(('0.1', '1', '10', '100', '1000', '10000')))

ax.zaxis.set_major_locator(LinearLocator(numticks=6))
ax.zaxis.set_major_formatter(FixedFormatter(('0.01', '0.1', '1', '10', '100', '1000', '1000')))


show()
