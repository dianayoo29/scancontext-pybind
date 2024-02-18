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

for file in all_file_names:
    curr_file = os.path.join(data_dir, file)
    print(curr_file)
    scd = bin2scd(curr_file)
    all_scd.append(scd.tolist())

def get_quantiles():
    all_val = []
    with open(("three_bit_quantiles_" + args.sequence + ".txt"), 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            all_val.append(float(line.rstrip()))
    return all_val

all_val = get_quantiles()

def toBin(ind):
    binarizedResult = []
    for row in all_scd[ind]:
        res = []
        for value in row:
            val = value*1000
            if val < all_val[1]:
                res.append([0,0,0])
            elif val >= all_val[1] and val < all_val[2]:
                res.append([0,0,1])
            elif val >= all_val[2] and val < all_val[3]:
                res.append([0,1,0])
            elif val >= all_val[3] and val < all_val[4]:
                res.append([1,0,0])
            elif val >= all_val[4] and val < all_val[5]:
                res.append([0,1,1])
            elif val >= all_val[5] and val < all_val[6]:
                res.append([1,0,1])
            elif val >= all_val[6] and val < all_val[7]:
                res.append([1,1,0])
            elif val >= all_val[7]:
                res.append([1,1,1])
        binarizedResult.append(res)
    return binarizedResult

def shiftedScd(scd, num):
    temp_scd = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(scd)): #20
        temp_scd[i] = scd[i][num:] + scd[i][: num]
    return temp_scd

def scd_distance(i_ind, j_ind):
    first_scd = toBin(i_ind)
    sec_scd = toBin(j_ind)
    hm_dist = hamming_distance(first_scd, sec_scd)
    return hm_dist

def hamming_distance(first_scd, sec_scd): 
    distance = []
    for shift in range(0, 60):
        temp_scd = shiftedScd(first_scd, shift)
        dist = 0
        for i in range(len(temp_scd)): #20 sor
            for j in range(len(temp_scd[i])): # 60
                if temp_scd[i][j][0] != sec_scd[i][j][0]:
                    dist += 1
                if temp_scd[i][j][1] != sec_scd[i][j][1]:
                    dist += 1
                if temp_scd[i][j][2] != sec_scd[i][j][2]:
                    dist += 1
        distance.append(dist)
    return min(distance)

def hamming_distance2(first_scd, sec_scd): 
    distance = []
    for shift in range(0, 60):
        temp_scd = shiftedScd(first_scd, shift)
        temp_dist = []
        dist = 0
        for j in range(0, 60): # 60 érték 1 sorban
            for row in range(0, 20): # minden sorban végig megyek 
                if temp_scd[row][j][0] != sec_scd[row][j][0]:
                    dist += 1
                if temp_scd[row][j][1] != sec_scd[row][j][1]:
                    dist += 1
                if temp_scd[row][j][2] != sec_scd[row][j][2]:
                    dist += 1
            temp_dist.append(dist)
            dist = 0
        distance.append(mean(temp_dist))
    return min(distance)

"""
query_cloud_filepath = os.path.join(data_dir, '003391.bin')
query_scd = bin2scd(query_cloud_filepath)
query_scd.tolist()

query_cloud_filepath_2 = os.path.join(data_dir, '002440.bin')
query_scd_2 = bin2scd(query_cloud_filepath_2)
query_scd_2.tolist()

print(all_avg[0])

print(query_scd[0][0])
print(query_scd[0][1])

first_scd = ""
for row in query_scd:
    for val in row:
        if val < all_avg[0]:
            first_scd += "0"
        elif val >= all_avg[0]:
            first_scd += "1"

sec_scd = ""
for row in query_scd_2:
    for val in row:
        if val < all_avg[0]:
            sec_scd += "0"
        elif val >= all_avg[0]:
            sec_scd += "1"

"""

threshold = 300
threshold_counter = 0
while threshold < 420:
    counter = 0
    loops = []
    loops_i = []
    loops_i_tuple = []
    for i in range(51, len(all_scd)):
        print(i)
        top_ringkey = []
        ringkey_euclidean_distance = []
        counter_ring_i = 0
        ring_elements_i = []
        loops_i_tuple = []
        for value in all_scd[i]:
            for val in value:
                if val != 0:
                    counter_ring_i += 1
            ring_elements_i.append(counter_ring_i)
            counter_ring_i = 0
        vc_ring_elements_i = np.array(ring_elements_i)

        for j in range(0, i-50):
            counter_ring_j = 0
            ring_elements_j = []
            for value in all_scd[j]:
                for val in value:
                    if val != 0:
                        counter_ring_j += 1
                ring_elements_j.append(counter_ring_j)
                counter_ring_j = 0
            vc_ring_elements_j = np.array(ring_elements_j)
            ringkey_euclidean_distance.append((j, np.linalg.norm((vc_ring_elements_i - vc_ring_elements_j))))
            j += 1

        ringkey_euclidean_distance.sort(key=lambda a: a[1])
        ring_key_counter = 0

        if len(ringkey_euclidean_distance) >= 50:
            while ring_key_counter < 50:
                top_ringkey.append((i, ringkey_euclidean_distance[ring_key_counter][0]))
                ring_key_counter += 1
        else:
            for m in range(0, len(ringkey_euclidean_distance)):
                top_ringkey.append((i, ringkey_euclidean_distance[m][0]))

        for ringkey in top_ringkey:
            distance = scd_distance(i, ringkey[1])
            if (distance <= threshold) and (i in loops_i):
                for dist in loops_i_tuple:
                    if dist[0] == i and distance < dist[1]:
                        loops_i_tuple.remove(dist)
                        loops_i_tuple.append((ringkey[0], distance, ringkey[1]))
                        loops.remove((dist[0], dist[2]))
                        loops.append((ringkey[0], ringkey[1]))
            elif distance <= threshold:
                loops.append((ringkey[0],ringkey[1]))
                loops_i.append(ringkey[0])
                loops_i_tuple.append((ringkey[0], distance, ringkey[1]))
                counter += 1
        i += 1
    with open(("loops/loops_in_" + args.sequence + "_" + str(threshold_counter) + ".txt"), 'w') as f:
        for loop in loops:
            f.write(str(loop))
            f.write('\n')
    with open(("info/info_" + args.sequence + ".txt"), 'a') as f:
        f.write(str(counter))
        f.write('\n')
    threshold += 20
    threshold_counter += 1

#print(-9.117150306701660156e-01 == -0.911715030670166) lett egy float konvertálás ezért változott meg