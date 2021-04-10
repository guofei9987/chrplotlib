import numpy as np
from chrplotlib import bar

from chrplotlib import animation


def update_bar(i):
    data = 10 * np.random.rand(20)
    print(bar(data, label=range(20), max_height=10))
    print('\033[{}A'.format(12))


animation(update_func=update_bar, interval=range(100), pause=0.2)
