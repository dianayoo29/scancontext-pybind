import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np
import math

data = np.loadtxt('dataset/poses/00.txt')
print(len(data))
plt.scatter(data[:,3], data[:,11], s=1)
#colors = np.array([SCANNET_COLOR_MAP[VALID_CLASS_IDS[l]] for l in pred])
pc = o3d.geometry.PointCloud()
pc.points = o3d.utility.Vector3dVector(np.vstack([data[:,3], data[:,11], np.zeros(len(data[:,3]))]).transpose())
#pc.colors = o3d.utility.Vector3dVector(0, 1, 0)
#np.vstack([data[:,3], data[:,11], np.zeros(len(data[:,3]))]).transpose()



o3d.visualization.draw_geometries([pc])