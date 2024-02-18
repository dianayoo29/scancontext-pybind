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
data_dir_name = "../data/" + args.sequence + "/velodyne"
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
row_values = []

for scd in all_scd: # scd -> egy egesz bin (20x60)
    one_scd_row_val = []
    for row in scd: # row -> egy sor 20 ertek
        row_val = []
        for val in row: # val -> egy ertek a sorban
            all_values.append(val)
            row_val.append(val)
        one_scd_row_val.append(row_val)
    row_values.append(one_scd_row_val)

def calculateQuantileForAll(all_values, num_intervals):
    quantiles = []
    min_val = min(all_values)
    max_val = max(all_values)
    step_size = (max_val - min_val) / num_intervals
    # Kiszámoljuk az intervallumokat
    quantiles = [min_val + i * step_size for i in range(num_intervals + 1)]
    quantiles.sort()
    print(quantiles)
    return quantiles

def calculateQuantileForRows(row_values, num_intervals):
    rowResults = []
    lineResult = []
    rowListsinList = []
    for i in range(0, len(row_values)):
        for j in range(0, len(row_values[i])): # 20 elem
            #lineResult.append(st.median(row_values[i][j]))
            min_val = min(row_values[i][j])
            max_val = max(row_values[i][j])
            step_size = (max_val - min_val) / num_intervals
            lineResult = [min_val + i * step_size for i in range(num_intervals + 1)]
            lineResult.sort()
            rowListsinList.append(lineResult)
            lineResult = []
        rowResults.append(rowListsinList)
        rowListsinList = []
    return rowResults

def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            f.write(str(value))
            f.write('\n')

two_bit_quantiles = calculateQuantileForAll(all_values, 4)
three_bit_quantiles = calculateQuantileForAll(all_values, 8)

writeInFile(two_bit_quantiles ,"quantization/all_2bit/two_bit_quantiles_" + args.sequence + ".txt")
writeInFile(three_bit_quantiles ,"quantization/all_3bit/three_bit_quantiles_" + args.sequence + ".txt")
#writeInFile(all_values ,"all_values.txt")

two_bit_quantiles_for_rows = calculateQuantileForRows(row_values, 4)
writeInFile(two_bit_quantiles_for_rows ,"quantization/row_2bit/two_bit_quantiles_for_rows_" + args.sequence + ".txt")

three_bit_quantiles_for_rows = calculateQuantileForRows(row_values, 8)
writeInFile(three_bit_quantiles_for_rows ,"quantization/row_3bit/three_bit_quantiles_for_rows_" + args.sequence + ".txt")