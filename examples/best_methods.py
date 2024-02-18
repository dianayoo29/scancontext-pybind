import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
bar_labels = ["ScanContext-50", "ScanContext-10", "AQ-Dataset[2bit|HM1]", "AQ-Dataset[3bit|HM2]", "Rule-based-COLUMN", "Max-Height-AQ-4bit"]
x = np.array(["1", "2", "3", "4", "5", "6"])
y = np.array([0.9501, 0.9372, 0.9197, 0.9265, 0.8989, 0.8735])
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:cyan']
ax.bar(x, y, label=bar_labels, color=bar_colors)

ax.set_xlabel('Methods')
ax.set_ylabel('AP')
ax.legend(title='')
ax.set_ylim(0,1.3)
#plt.bar(x,y)

plt.show()