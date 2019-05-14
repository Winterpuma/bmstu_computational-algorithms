# Это чисто по фану поглядеть кто по жизни наша F

import matplotlib.pyplot as plt
import numpy as np
from main import *

x = np.arange(2, 25, 0.5)
y = [F(xx) for xx in x]
plt.figure(1)
plt.ylabel("y")
plt.xlabel("x")
plt.plot(x, [0 for i in range(len(x))], 'k', color = "red")
plt.plot(x, y, 'k')
plt.show()

# Spoiler: Оказалось, что +- прямая :С
# Самый интересный найденный мной график при Pn = 0.5, Tn = 300, T0 = 12000, Tw = 6000, m = 12
