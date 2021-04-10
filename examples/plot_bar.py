import numpy as np
from chrplotlib import bar

data = 10 * np.random.rand(20)
label = range(20)
print(bar(data))
print(bar(data=data, label=range(20)))
print(bar(data, kind='barh'))
print(bar(data=data, label=range(20), kind='barh'))
