import statistics as st
import os
import numpy as np 
import open3d as o3d
import pyscancontext as sc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seq", dest="sequence", help="Choose a sequence[00|02|05|08]", required=True)
args = parser.parse_args()

curr_dir = os.path.dirname(__file__)
data_dir_name = "../../data/" + args.sequence + "/velodyne"
data_dir = os.path.join(curr_dir, data_dir_name)

all_file_names = os.listdir(data_dir)
all_file_names.sort()
all_scd = []

scm = sc.SCManager()

def read_bin(bin_path):
    scan = np.fromfile(bin_path, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    ptcloud_xyz = scan[:, :-1]
    return ptcloud_xyz

def bin2scd(filepath, voxel_size=0.5):
    xyz = read_bin(filepath)
    print( f" The point cloud {filepath} is loaded." )
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    xyz_down = np.asarray(pcd_down.points)
    scd = scm.make_scancontext(xyz_down)
    return scd

for file in all_file_names:
    curr_file = os.path.join(data_dir, file)
    print(curr_file)
    scd = bin2scd(curr_file)
    all_scd.append(scd.tolist())

all_values = []
all_max_height = []
row_values = []
column_values = []
bin_count = 0
cval = 0

for scd in all_scd: # scd -> egy egesz bin (20x60)
    column_val = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    one_scd_row_val = []
    for row in scd: # row -> egy sor 20 ertek
        row_val = []
        for val in row: # val -> egy ertek a sorban
            all_values.append(val)
            column_val[cval] += [val]
            row_val.append(val)
            cval += 1
        cval = 0
        one_scd_row_val.append(row_val)
    row_values.append(one_scd_row_val)
    column_values.append(column_val)

def calculateColMaxValues(column_values):
    columnsResults = []
    lineResult = []
    for bin in column_values: # 1 binben 60 list van, len(column_values) = 5450
        for col in bin: # 1 oszlop (20 elem)
            tempList = []
            max_height = max(col) # maximum magasság
            if max_height != 0.0:
                all_max_height.append(max_height)
            distance = col.index(max_height)
            lineResult.append([max_height, distance])
        columnsResults.append(lineResult)
        lineResult = []
    return columnsResults

def calculateQuantilesForMaxHeight3bit():
    calculateColMaxValues(column_values)
    quantiles = []
    quantiles.append(np.quantile(all_max_height, .14))
    quantiles.append(np.quantile(all_max_height, .28))
    quantiles.append(np.quantile(all_max_height, .42))
    quantiles.append(np.quantile(all_max_height, .56))
    quantiles.append(np.quantile(all_max_height, .70))
    quantiles.append(np.quantile(all_max_height, .84))
    quantiles.sort()
    return quantiles

def calculateQuantilesForMaxHeight4bit():
    calculateColMaxValues(column_values)
    quantiles = []
    quantiles.append(np.quantile(all_max_height, 0.06))
    quantiles.append(np.quantile(all_max_height, 0.12))
    quantiles.append(np.quantile(all_max_height, 0.18))
    quantiles.append(np.quantile(all_max_height, 0.24))
    quantiles.append(np.quantile(all_max_height, 0.30))
    quantiles.append(np.quantile(all_max_height, 0.36))
    quantiles.append(np.quantile(all_max_height, 0.42))
    quantiles.append(np.quantile(all_max_height, 0.48))
    quantiles.append(np.quantile(all_max_height, 0.54))
    quantiles.append(np.quantile(all_max_height, 0.60))
    quantiles.append(np.quantile(all_max_height, 0.66))
    quantiles.append(np.quantile(all_max_height, 0.72))
    quantiles.append(np.quantile(all_max_height, 0.78))
    quantiles.append(np.quantile(all_max_height, 0.84))
    quantiles.append(np.quantile(all_max_height, 0.90))
    quantiles.sort()
    return quantiles

def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            f.write(str(value))
            f.write('\n')

def writeInFileOneValue(value, fileName):
    with open((fileName), 'w') as f:
        f.write(str(value))

colValues= calculateColMaxValues(column_values)
quantilesMaxHeight = calculateQuantilesForMaxHeight3bit()
quantilesMaxHeight4bit = calculateQuantilesForMaxHeight4bit()
writeInFile(colValues, "col_max_values"+ args.sequence +".txt")
writeInFile(quantilesMaxHeight, "3bit/3bit_quantiles_col_max_values"+ args.sequence +".txt")
writeInFile(quantilesMaxHeight4bit, "4bit/4bit_quantiles_col_max_values"+ args.sequence +".txt")