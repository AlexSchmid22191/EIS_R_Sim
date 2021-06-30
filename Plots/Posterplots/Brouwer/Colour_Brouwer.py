from matplotlib.colors import LogNorm
from matplotlib.pyplot import subplots, show
from matplotlib.style import use
from numpy import load, log10, min, zeros, max
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import LogLocator, NullFormatter, LinearLocator


use('../Poster.mplstyle')


defect_data = load('../../../Brouwer/Brouwer_Bias.npy')

fig, ax = subplots()

ax.set_xlabel('Oxygen partial pressure (bar)')
ax.set_ylabel('Overpotential (V)')

data = zeros((1201, 2401, 3))

data[:, :, 0] = (log10(defect_data['vacancies']) - min(log10(defect_data['vacancies']))) /\
                (max(log10(defect_data['vacancies'])) - min(log10(defect_data['vacancies'])))
data[:, :, 1] = -(log10(defect_data['holes']) - min(log10(defect_data['holes']))) /\
                (min(log10(defect_data['holes'])) - max(log10(defect_data['holes'])))
data[:, :, 2] = -(log10(defect_data['electrons']) - min(log10(defect_data['electrons']))) /\
                (min(log10(defect_data['electrons'])) - max(log10(defect_data['electrons'])))

print(data)

ax.imshow(data)

show()