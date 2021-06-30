import numpy as np
from colorspacious import cspace_convert
from matplotlib.colors import ListedColormap
from matplotlib.cm import get_cmap
from matplotlib.cm import register_cmap
from Plots.Colormapper import truncate_colormap

tu_blue_rgb = [0, 102, 153]
tu_blue_jch = cspace_convert(tu_blue_rgb, 'sRGB255', 'JCh')


# A variation of TU Blue - centered in luminosity ----------------------------------------------------------------------
tu_map_centered_j = np.zeros(shape=(256, 3))

# Luminosity gradient centered on TU Blue
tu_map_centered_j[:128, 0] = np.linspace(1.9 * tu_blue_jch[0], tu_blue_jch[0], 128, False)
tu_map_centered_j[128:, 0] = np.linspace(tu_blue_jch[0], 0.1 * tu_blue_jch[0], 128, True)

# Chroma gradient centered on TU blue, desaturated towards the edges
tu_map_centered_j[:128, 1] = np.linspace(0.7 * tu_blue_jch[1], 1 * tu_blue_jch[1], 128, False)
tu_map_centered_j[128:, 1] = np.linspace(1 * tu_blue_jch[1], 0.7 * tu_blue_jch[1], 128, True)
tu_map_centered_j[:, 2] = tu_blue_jch[2]

tu_map_centered_rgb = cspace_convert(tu_map_centered_j, "JCh", "sRGB1")
tu_map_centered_rgb = np.clip(tu_map_centered_rgb, 0, 1)
tu_map_centered = ListedColormap(tu_map_centered_rgb)

register_cmap(name='TU_Map_Centered', cmap=tu_map_centered)

# A variation of TU Blue - uniform luminosity gradient, not centered on tu blue ----------------------------------------
tu_map_j = np.zeros(shape=(256, 3))

# Uniform luminosity gradient
tu_map_j[:, 0] = np.linspace(0, 90, 256, True)

# Chroma gradient centered on TU blue, desaturated towards the edges
tu_map_j[:128, 1] = np.linspace(0.5 * tu_blue_jch[1], 1 * tu_blue_jch[1], 128, False)
tu_map_j[128:, 1] = np.linspace(1 * tu_blue_jch[1], 0.3 * tu_blue_jch[1], 128, True)
tu_map_j[:, 2] = tu_blue_jch[2]

tu_map_rgb = cspace_convert(tu_map_j, "JCh", "sRGB1")
tu_map_rgb = np.clip(tu_map_rgb, 0, 1)
tu_map = ListedColormap(tu_map_rgb)

register_cmap(name='TU_Map', cmap=tu_map)


# Diverging TU Blue Map ------------------------------------------------------------------------------------------------
tu_map_div_j = np.zeros(shape=(256, 3))

# Luminosity gradient
tu_map_div_j[:128:, 0] = np.linspace(10, 100, 128, False)
tu_map_div_j[128:, 0] = np.linspace(100, 10, 128, True)

# Chroma gradient
tu_map_div_j[:64, 1] = np.linspace(0.6 * tu_blue_jch[1], tu_blue_jch[1], 64, False)
tu_map_div_j[64:128, 1] = np.linspace(tu_blue_jch[1], 0.0 * tu_blue_jch[1], 64, False)
tu_map_div_j[128:192, 1] = np.linspace(0.0 * tu_blue_jch[1], tu_blue_jch[1], 64, False)
tu_map_div_j[192:, 1] = np.linspace(tu_blue_jch[1], 0.6 * tu_blue_jch[1], 64, True)

# Hue from TU blue and complementary color
tu_map_div_j[:128, 2] = tu_blue_jch[2]
tu_map_div_j[128:, 2] = (tu_blue_jch[2] - 180) % 360

tu_map_div_rgb = cspace_convert(tu_map_div_j, "JCh", "sRGB1")
tu_map_div_rgb = np.clip(tu_map_div_rgb, 0, 1)
tu_map_div = ListedColormap(tu_map_div_rgb)

register_cmap(name='TU_Map_Divergent', cmap=tu_map_div)


# Blue Color Map -------------------------------------------------------------------------------------------------------
trunc_blue = truncate_colormap(get_cmap('Blues'), minval=0.2)
register_cmap('Blues_t', trunc_blue)


# Diverging Blue Map ---------------------------------------------------------------------------------------------------
blue_div_map_rgb = np.zeros(shape=(256, 3))

blue_section_rgb = np.array([get_cmap('Blues')(i/128)[:3] for i in range(128)])
blue_section_jch = cspace_convert(blue_section_rgb, 'sRGB1', 'JCh')

orange_section_jch = blue_section_jch[::-1, :]
orange_section_jch[:, 2] += 180
orange_section_jch[:, 2] %= 360

orange_section_rgb = cspace_convert(orange_section_jch, 'JCh', 'sRGB1')

blue_div_map_rgb[128:] = blue_section_rgb
blue_div_map_rgb[:128] = orange_section_rgb

blue_div_map_rgb = np.clip(blue_div_map_rgb, 0, 1)

blue_div_map = ListedColormap(blue_div_map_rgb)
register_cmap('Blues_div', blue_div_map)