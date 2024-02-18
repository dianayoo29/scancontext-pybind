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
data_dir_name = "../../../data/" + args.sequence + "/velodyne"
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

query_cloud_filepath = os.path.join(data_dir, '001561.bin')
query_scd = bin2scd(query_cloud_filepath)
query_scd.tolist()

query_cloud_filepath_2 = os.path.join(data_dir, '000111.bin')
query_scd_2 = bin2scd(query_cloud_filepath_2)
query_scd_2.tolist()


def get_quantiles():
    row_quant = []
    splitted_row_quant = []
    with open(("two_bit_quantiles_for_rows.txt"), 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            row_quant.append(line.rstrip())
    temp_row = []
    quants = []
    for i in range(0, len(row_quant)):
        temp_row.append(row_quant[i].split("], ["))
        temp_row[i][0] = temp_row[i][0].replace("[", "")
        temp_row[i][-1] = temp_row[i][-1].replace("]", "")
        for j in range(len(temp_row[i])):
            quants.append(temp_row[i][j].split(", "))
        splitted_row_quant.append(quants)
        quants = []
    return splitted_row_quant

all_quantiles = get_quantiles()
print(all_quantiles[0][0])

def toBin1(ind):
    binarizedResult = []
    for i in range(0, len(query_scd)): # egy sor az all_scd[ind][i]
        res = []
        for j in range(0, len(query_scd[i])): # egy érték a soron belül
            val = query_scd[i][j]
            if val == 0.0:
                res.append([0,0])
            elif val < float(all_quantiles[ind][i][0]):
                res.append([0,1])
            elif val >= float(all_quantiles[ind][i][0]) and val < float(all_quantiles[ind][i][1]):
                res.append([1,0])
            elif val >= float(all_quantiles[ind][i][1]):
                res.append([1,1])
        binarizedResult.append(res)
    return binarizedResult

def toBin2(ind):
    binarizedResult = []
    for i in range(0, len(query_scd_2)): # egy sor az all_scd[ind][i]
        res = []
        for j in range(0, len(query_scd_2[i])): # egy érték a soron belül
            val = query_scd_2[i][j]
            if val == 0.0:
                res.append([0,0])
            elif val < float(all_quantiles[ind][i][0]):
                res.append([0,1])
            elif val >= float(all_quantiles[ind][i][0]) and val < float(all_quantiles[ind][i][1]):
                res.append([1,0])
            elif val >= float(all_quantiles[ind][i][1]):
                res.append([1,1])
        binarizedResult.append(res)
    return binarizedResult
def scd_distance(i_ind, j_ind):
    first_scd = toBin1(i_ind)
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
        print("len(temp_scd) =" + str(len(temp_scd)))
        print("len(temp_scd[0]) = " + str(len(temp_scd[0])))
        print("len(temp_scd[0][0]) = " + str(len(temp_scd[0][0])))
        for i in range(len(temp_scd)): #20
            for j in range(len(temp_scd[i])): # 60
                if temp_scd[i][j][0] != sec_scd[i][j][0] and temp_scd[i][j][1] != sec_scd[i][j][1]:
                    dist += 2
                elif temp_scd[i][j][0] != sec_scd[i][j][0] or temp_scd[i][j][1] != sec_scd[i][j][1]:
                    dist += 1
        distance.append(dist)
    return min(distance)

def writeInFile(allValues, fileName):
    with open((fileName), 'w') as f:
        for value in allValues:
            #print(value)
            f.write(str(value))
            f.write('\n')

print(scd_distance(1561, 111))
#writeInFile(query_scd, "vals.txt")
#writeInFile(query_scd_2, "vals2.txt")
#writeInFile(toBin1(1561) ,"2bin_vals_for_rows.txt")
#writeInFile(toBin2(111) ,"2bin_vals_for_rows_2.txt")