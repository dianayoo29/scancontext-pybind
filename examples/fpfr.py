import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
bar_labels = ["FPFH", "FPFH+QBB"]
x = np.array(["1", "2", "3", "4", "5", "6"])
y = np.array([0.8948, 0.8697, 0.8148, 0.8781, 0.8804, 0.8601])
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:cyan']
ax.bar(x, y, label=bar_labels, color=bar_colors)

ax.set_xlabel('Methods')
ax.set_ylabel('AP')
ax.legend(title='')
ax.set_ylim(0,1.3)
#plt.bar(x,y)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()