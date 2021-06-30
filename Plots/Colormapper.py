import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def colormapper(cmap, nlines, start=0, cuttoff=1):
    a = [cmap(j) for j in np.linspace(start, cuttoff, nlines, True)]
    b = np.round(a, 3)
    c = [(d[0], d[1], d[2], d[3]) for d in b]

    return c


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=256):
    new_cmap = LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap
