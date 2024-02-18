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
data_dir_name = "data/" + args.sequence + "/velodyne"
data_dir = os.path.join(curr_dir, data_dir_name)

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

"""
all_values = [2, 3, 5, 1, 0, -1, -5, 2, 1, 5, 4]
quantiles = []
min_val = min(all_values)
max_val = max(all_values)
distance_between_min_max = (max_val - min_val) + 1
t = round(distance_between_min_max/2)
d = round(t/2)
k = t + d

# -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#  1   2   3   4   5  6  7  8  9  10 11
#      ^           ^     ^
#          ^          ^        ^

# -5  <  -3  <  0  <  3  <  5
#    00     01     10    11
print(str(min_val) + "min: "+ str(max_val))
print(distance_between_min_max)
print(t)
print(d)
print(k)
temp = []
for i in range(len(all_values)):
    if all_values[i] >= -5 and all_values[i] < -3:
        temp.append("00")
    elif all_values[i] >= -3 and all_values[i] < 0:
        temp.append("01")
    elif all_values[i] >= 0 and all_values[i] < 3:
        temp.append("10")
    elif all_values[i] >= 3 and all_values[i] <= 5:
        temp.append("11")

print(temp)
# ['10', '11', '11', '10', '10', '01', '00', '10', '10', '11', '11']
"""


query_cloud_filepath = os.path.join(data_dir, '001594.bin')
query_scd = bin2scd(query_cloud_filepath)
query_scd.tolist()

query_cloud_filepath_2 = os.path.join(data_dir, '000149.bin')
query_scd_2 = bin2scd(query_cloud_filepath_2)
query_scd_2.tolist()


def get_quantiles():
    all_val = []
    with open(("binarization/quantization/all/two_bit_quantiles.txt"), 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            all_val.append(int(line.rstrip()))
    return all_val

all_val = get_quantiles()

print_bin_1 = []
def toBin1(ind):
    binarizedResult = []
    for row in query_scd:
        res = []
        for value in row:
            val = value*1000
            if val < all_val[1]:
                res.append("00")
            elif val >= all_val[1] and val < all_val[2]:
                res.append("01")
            elif val >= all_val[2] and val < all_val[3]:
                res.append("10")
            elif val >= all_val[3]:
                res.append("11")
        binarizedResult.append(res)
    return binarizedResult

#-21
#-13
#-5
#2

def toBin2(ind):
    binarizedResult = []
    for row in query_scd_2:
        res = []
        for value in row:
            val = value*1000
            if val < all_val[1]:
                res.append("00")
            elif val >= all_val[1] and val < all_val[2]:
                res.append("01")
            elif val >= all_val[2] and val < all_val[3]:
                res.append("10")
            elif val >= all_val[3]:
                res.append("11")
        binarizedResult.append(res)
    return binarizedResult


def scd_distance(i_ind, j_ind):
    first_scd = toBin1(i_ind)
    #print(first_scd)
    sec_scd = toBin2(j_ind)
    hm_dist = hamming_distance(first_scd, sec_scd)
    return hm_dist

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

#print(scd_distance(1594, 149))


def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            #print(value)
            f.write(str(value))
            f.write('\n')

writeInFile(query_scd, "vals.txt")
writeInFile(toBin1(111) ,"2bin_vals.txt")