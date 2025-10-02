import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size

_DEFAULT_PARAMS = {
    'legend.fontsize': 'x-large',
    'figure.figsize': (4, 4),
    'axes.labelsize': 'x-large',
    'axes.titlesize': 'x-large',
    'xtick.labelsize': 'x-large',
    'ytick.labelsize': 'x-large',
    'figure.dpi': 80,
    'figure.autolayout': False,
}

def apply_rcparams(params=None):
    """Apply default rcParams (or your override dict)."""
    p = dict(_DEFAULT_PARAMS)
    if params:
        p.update(params)
    plt.rcParams.update(p)

def set_size(w, h, ax=None):
    """Set axes size in inches accounting for subplot margins."""
    if ax is None:
        ax = plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

def new_fig(hs=3, vs=3, hf=6, vf=6):
    """Create a figure with fixed paddings using Divider/Size."""
    fig = plt.figure(figsize=(hf, vf))
    h = [Size.Fixed(1.0), Size.Fixed(hs)]
    v = [Size.Fixed(0.7), Size.Fixed(vs)]
    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    ax = fig.add_axes(divider.get_position(),
                      axes_locator=divider.new_locator(nx=1, ny=1))
    return ax