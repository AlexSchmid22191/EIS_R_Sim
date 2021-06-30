from matplotlib.pyplot import gca
from matplotlib.patches import Polygon
from numpy import exp, sqrt


def semilog_slope(origin, slope, text=None, ax=None, frac=0.1, inverted=False, facecolor='0.8', **text_kwargs):
    if not ax:
        ax = gca()

    x, y = origin

    dx = (ax.get_xlim()[1] - ax.get_xlim()[0]) * frac
    dy = exp(dx*slope)

    if inverted:
        x_dx = x+dx
        y_dy = y/dy
        x_txt = x-0.15*dx
        ha = 'right'

    else:
        x_dx = x-dx
        y_dy = y*dy
        x_txt = x+0.15*dx
        ha = 'left'

    trg = Polygon([(x, y), (x, y_dy), (x_dx, y)], closed=True, facecolor=facecolor)
    ax.add_patch(trg)

    y_txt = sqrt(y * y_dy)

    if text:
        ax.text(x_txt, y_txt, text, **text_kwargs, ha=ha)
    else:
        ax.text(x_txt, y_txt, '{:4.2f}'.format(slope), **text_kwargs, ha=ha)
