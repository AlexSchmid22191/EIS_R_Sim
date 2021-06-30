from numpy import load, gradient, log
from matplotlib.pyplot import subplots, show
from matplotlib.style import use

data = load('../../../Brouwer/Brouwer_Ideal.npy')

grad1_h = gradient(log(data['holes']), log(data['pressure']))
grad2_h = gradient(log(grad1_h), log(data['pressure']))

fig, ax = subplots()

ax.plot(data['pressure'], grad2_h)

show()
