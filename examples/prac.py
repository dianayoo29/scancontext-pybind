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

query_cloud_filepath = os.path.join(data_dir, '001594.bin')
query_scd = bin2scd(query_cloud_filepath)
query_scd.tolist()

query_cloud_filepath_2 = os.path.join(data_dir, '000149.bin')
query_scd_2 = bin2scd(query_cloud_filepath_2)
query_scd_2.tolist()
""""
def get_col_avg():
    col_avg = []
    splitted_col_avg = []
    with open(("binarization/thresholding/col_avg/col_avg.txt"), 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            col_avg.append(line.rstrip())
    for i in range(0, len(col_avg)):
        splitted_col_avg.append(col_avg[i].split(", "))
        splitted_col_avg[i][0] = splitted_col_avg[i][0].replace("[", "")
        splitted_col_avg[i][-1] = splitted_col_avg[i][-1].replace("]", "")
    return splitted_col_avg

col_avg = get_col_avg()

def toBin1(ind):
    binarizedResult = ""
    for i in range(0, len(query_scd)): # row
        for j in range(0, len(query_scd[i])):
            if query_scd[i][j] < float(col_avg[ind][j]):
                binarizedResult += "0"
            elif query_scd[i][j] >= float(col_avg[ind][j]):
                binarizedResult += "1"
    return binarizedResult

def toBin2(ind):
    binarizedResult = ""
    for i in range(0, len(query_scd_2)): # row
        for j in range(0, len(query_scd_2[i])):
            if query_scd_2[i][j] < float(col_avg[ind][j]):
                binarizedResult += "0"
            elif query_scd_2[i][j] >= float(col_avg[ind][j]):
                binarizedResult += "1"
    return binarizedResult

def hamming_distance(i_ind, j_ind): 
    first_scd = toBin1(i_ind)
    sec_scd = toBin2(j_ind)
    distance = 0
    L = len(first_scd)
    for i in range(L):
        if first_scd[i] != sec_scd[i]:
            distance += 1
    return distance

#print(hamming_distance(3391, 2440)) #355
#print(hamming_distance(1562, 112)) #482
#print(hamming_distance(1605, 161)) #167
#print("Col, avg: ")
#print(hamming_distance(3445, 442)) #177
#print(hamming_distance(1593, 148)) #177
"""
def get_all_median():
    all_median = []
    with open(("binarization/thresholding/all_avg/all_avg.txt"), 'r') as f:
        #for line in Lines:
        all_median = float(f.readline().rstrip())
    return all_median

all_median = get_all_median()
print(all_median)

def toBinMed1(ind):
    binarizedResult = []
    for row in query_scd:
        res = []
        for val in row:
            if val < all_median:
                res.append(0)
            elif val >= all_median:
                res.append(1)
        binarizedResult.append(res)
    return binarizedResult

def toBinMed2(ind):
    binarizedResult = []
    for row in query_scd_2:
        res = []
        for val in row:
            if val < all_median:
                res.append(0)
            elif val >= all_median:
                res.append(1)
        binarizedResult.append(res)
    return binarizedResult


def scd_distance(i_ind, j_ind):
    first_scd = toBinMed1(i_ind)
    #print(first_scd)
    sec_scd = toBinMed2(j_ind)
    hm_dist = hamming_distance(first_scd, sec_scd)
    return hm_dist

def hamming_distance(first_scd, sec_scd): 
    distance = []
    L = len(first_scd)
    for shift in range(0, 60):
        temp_scd = shiftedScd(first_scd, shift)
        dist = 0
        for i in range(L): #20
            for j in range(len(temp_scd[i])): # 60
                if temp_scd[i][j] != sec_scd[i][j]:
                    dist += 1
        distance.append(dist)
    return min(distance)

def shiftedScd(scd, num):
    temp_scd = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(scd)): #20
        #for j in range(len(scd[i])): # 60
        temp_scd[i] = scd[i][num:] + scd[i][: num]
            #temp_scd[i] += [scd[i][j]]
    return temp_scd

print("all_median: ")
print(scd_distance(1594, 149)) #30