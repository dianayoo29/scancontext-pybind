import os
import numpy as np 
import open3d as o3d
import pyscancontext as sc
import argparse
from statistics import mean 

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seq", dest="sequence", help="Choose a sequence[00|02|05|08]", required=True)
args = parser.parse_args()

curr_dir = os.path.dirname(__file__)
data_dir_name = "../../../data/" + args.sequence + "/velodyne"
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

query_cloud_filepath = os.path.join(data_dir, '001340.bin')
query_scd = bin2scd(query_cloud_filepath)
query_scd.tolist()

query_cloud_filepath_2 = os.path.join(data_dir, '000582.bin')
query_scd_2 = bin2scd(query_cloud_filepath_2)
query_scd_2.tolist()

def get_row_avg():
    row_avg = []
    splitted_row_avg = []
    with open(("row_avg_" + args.sequence + ".txt"), 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            row_avg.append(line.rstrip())
    for i in range(0, len(row_avg)):
        splitted_row_avg.append(row_avg[i].split(", "))
        splitted_row_avg[i][0] = splitted_row_avg[i][0].replace("[", "")
        splitted_row_avg[i][-1] = splitted_row_avg[i][-1].replace("]", "")
    return splitted_row_avg

row_avg = get_row_avg()

def toBin1(ind):
    binarizedResult = []
    for i in range(0, len(query_scd)): # row
        res = []
        avg_value = float(row_avg[ind][i])
        for j in range(0, len(query_scd[i])):
            val = query_scd[i][j]
            if val < avg_value:
                res.append(0)
            elif val >= avg_value:
                res.append(1)
        binarizedResult.append(res)
    return binarizedResult

def toBin2(ind):
    binarizedResult = []
    for i in range(0, len(query_scd_2)): # row
        res = []
        avg_value = float(row_avg[ind][i])
        for j in range(0, len(query_scd_2[i])):
            val = query_scd_2[i][j]
            print(val)
            #print(float(row_avg[ind][i]))
            if val < avg_value:
                res.append(0)
            elif val >= avg_value:
                res.append(1)
        binarizedResult.append(res)
    return binarizedResult

def shiftedScd(scd, num):
    temp_scd = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(scd)): #20
        temp_scd[i] = scd[i][num:] + scd[i][: num]
    return temp_scd

def hamming_distance(first_scd, sec_scd): 
    distance = []
    for shift in range(0, 60):
        temp_scd = shiftedScd(first_scd, shift)
        dist = 0
        for i in range(len(first_scd)): #20
            for j in range(len(temp_scd[i])): # 60
                if temp_scd[i][j] != sec_scd[i][j]:
                    dist += 1
        distance.append(dist)
    return min(distance)

def hamming_distance2(first_scd, sec_scd): 
    distance = []
    for shift in range(0, 60):
        temp_scd = shiftedScd(first_scd, shift)
        temp_dist = []
        dist = 0
        for i in range(len(first_scd)): #20
            for j in range(len(temp_scd[i])): # 60
                if temp_scd[i][j] != sec_scd[i][j]:
                    dist += 1
            temp_dist.append(dist)
            dist = 0
        distance.append(mean(temp_dist))
    return min(distance)

def scd_distance(i_ind, j_ind):
    first_scd = toBin1(i_ind)
    sec_scd = toBin2(j_ind)
    hm_dist = hamming_distance(first_scd, sec_scd)
    return hm_dist

def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            #print(value)
            f.write(str(value))
            f.write('\n')

print(scd_distance(1340, 582))
#writeInFile(row_avg, "vals.txt")
#writeInFile(toBin1(1411), "binarized_data_1411.txt")
#writeInFile(toBin2(797), "binarized_data_1420.txt")