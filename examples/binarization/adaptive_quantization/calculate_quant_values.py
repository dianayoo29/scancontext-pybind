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
row_values = []

for scd in all_scd: # scd -> egy egesz bin (20x60)
    one_scd_row_val = []
    for row in scd: # row -> egy sor 20 ertek
        row_val = []
        for val in row: # val -> egy ertek a sorban
            if val != 0.0:
                all_values.append(val)
                row_val.append(val)
        one_scd_row_val.append(row_val)
    row_values.append(one_scd_row_val)

def calculateQuantileForAll2bit(all_values):
    quantiles = []
    quantiles.append(np.quantile(all_values, .33))
    quantiles.append(np.quantile(all_values, .66))
    quantiles.sort()
    return quantiles

def calculateQuantileForAll3bit(all_values):
    quantiles = []
    quantiles.append(np.quantile(all_values, .14))
    quantiles.append(np.quantile(all_values, .28))
    quantiles.append(np.quantile(all_values, .42))
    quantiles.append(np.quantile(all_values, .56))
    quantiles.append(np.quantile(all_values, .70))
    quantiles.append(np.quantile(all_values, .84))
    quantiles.sort()
    return quantiles

def calculateQuantileForRows2bit(row_values):
    rowResults = []
    lineResult = []
    rowListsinList = []
    for i in range(0, len(row_values)):
        for j in range(0, len(row_values[i])): # 20 elem
            if len(row_values[i][j]) != 0:
                lineResult.append(np.quantile(row_values[i][j], .33))
                lineResult.append(np.quantile(row_values[i][j], .66))
            else:
                lineResult.append(0.5)  #?? ez így működhet?, mivel a sorban csak 0.0 van elvileg nem kéne gond legyen a binarizációnál
                lineResult.append(1)
            lineResult.sort()
            rowListsinList.append(lineResult)
            lineResult = []
        rowResults.append(rowListsinList)
        rowListsinList = []
    return rowResults

def calculateQuantileForRows3bit(row_values):
    rowResults = []
    lineResult = []
    rowListsinList = []
    for i in range(0, len(row_values)):
        for j in range(0, len(row_values[i])): # 20 elem
            if len(row_values[i][j]) != 0:
                lineResult.append(np.quantile(row_values[i][j], .14))
                lineResult.append(np.quantile(row_values[i][j], .28))
                lineResult.append(np.quantile(row_values[i][j], .42))
                lineResult.append(np.quantile(row_values[i][j], .56))
                lineResult.append(np.quantile(row_values[i][j], .70))
                lineResult.append(np.quantile(row_values[i][j], .84))
            else:
                lineResult.append(0.2)  #?? ez így működhet?, mivel a sorban csak 0.0 van elvileg nem kéne gond legyen a binarizációnál
                lineResult.append(0.3)
                lineResult.append(0.4)
                lineResult.append(0.5)
                lineResult.append(0.6)
                lineResult.append(1)
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

two_bit_quantiles = calculateQuantileForAll2bit(all_values)
writeInFile(two_bit_quantiles ,"ad_all_2bit/two_bit_quantiles_" + args.sequence + ".txt")
two_bit_quantiles_for_rows = calculateQuantileForRows2bit(row_values)
writeInFile(two_bit_quantiles_for_rows ,"ad_row_2bit/two_bit_quantiles_for_rows_" + args.sequence + ".txt")

three_bit_quantiles = calculateQuantileForAll3bit(all_values)
writeInFile(three_bit_quantiles ,"ad_all_3bit/three_bit_quantiles_" + args.sequence + ".txt")

three_bit_quantiles_for_rows = calculateQuantileForRows3bit(row_values)
writeInFile(three_bit_quantiles_for_rows ,"ad_row_3bit/three_bit_quantiles_for_rows_" + args.sequence + ".txt")