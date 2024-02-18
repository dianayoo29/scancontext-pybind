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
column_values = []
bin_count = 0
cval = 0

for scd in all_scd: # scd -> egy egesz bin (20x60)
    column_val = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    one_scd_row_val = []
    for row in scd: # row -> egy sor 20 ertek
        row_val = []
        for val in row: # val -> egy ertek a sorban
            print(val)
            all_values.append(val)
            column_val[cval] += [val]
            row_val.append(val)
            cval += 1
        cval = 0
        one_scd_row_val.append(row_val)
    row_values.append(one_scd_row_val)
    column_values.append(column_val)

def calculateMedianOrAvgForAllData(all_values, type):
    allResults = 0
    if type == "median":
        #for i in range(0, len(all_values)):
        allResults = st.median(all_values)
    elif type == "avg":
        #for i in range(0, len(all_values)):
        allResults = st.mean(all_values)
    return allResults

def calculateMedianOrAvgForRows(row_values, type):
    rowResults = []
    lineResult = []
    if type == "median":
        for i in range(0, len(row_values)):
            for j in range(0, len(row_values[i])): # 20 elem
                lineResult.append(st.median(row_values[i][j]))
            rowResults.append(lineResult)
            lineResult = []
    elif type == "avg":
        for i in range(0, len(row_values)):
            for j in range(0, len(row_values[i])):
                lineResult.append(st.mean(row_values[i][j]))
            rowResults.append(lineResult)
            lineResult = []
    return rowResults

def calculateMedianOrAvgForColumns(column_values, type):
    columnsResults = []
    lineResult = []
    temp = 0
    if type == "median":
        for bin in column_values: # 60 oszlop
            for column in bin: # 1 oszlop (20 elem)
                lineResult.append(st.median(column))
                temp += 1
            columnsResults.append(lineResult)
            temp = 0
            lineResult = []
    elif type == "avg":
        for bin in column_values: # 60 oszlop
            for column in bin: # 1 oszlop (20 elem)
                lineResult.append(st.mean(column))
                temp += 1
            columnsResults.append(lineResult)
            temp = 0
            lineResult = []
    return columnsResults

def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            f.write(str(value))
            f.write('\n')

def writeInFileOneValue(value, fileName):
    with open((fileName), 'w') as f:
        f.write(str(value))


allMedians = calculateMedianOrAvgForAllData(all_values, "median")
allAvgs = calculateMedianOrAvgForAllData(all_values, "avg")
rowMedians = calculateMedianOrAvgForRows(row_values, "median")
rowAvgs = calculateMedianOrAvgForRows(row_values, "avg")
#colMedians = calculateMedianOrAvgForColumns(column_values, "median")
#colAvgs = calculateMedianOrAvgForColumns(column_values, "avg")

writeInFileOneValue(allMedians ,"thresholding/all_median/all_median_" + args.sequence + ".txt")
writeInFileOneValue(allAvgs ,"thresholding/all_avg/all_avg_" + args.sequence + ".txt")
writeInFile(rowMedians ,"thresholding/row_median/row_median_" + args.sequence + ".txt")
writeInFile(rowAvgs ,"thresholding/row_avg/row_avg_" + args.sequence + ".txt")
#writeInFile(colMedians ,"thresholding/col_median/col_median" + args.sequence + ".txt")
#writeInFile(colAvgs ,"thresholding/col_avg/col_avg" + args.sequence + ".txt")
#writeInFile(row_values ,"row_values.txt")