import os 
import time
import numpy as np 
import open3d as o3d
import pyscancontext as sc
import argparse

# python3 loop_detection.py --seq 00

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

print('')

def calc_scd_dist_and_time(scd1, scd2):
    ts = time.time()
    distance, argmin_rot_idx = scm.scd_distance(scd1, scd2)
    te = time.time()
    t_elaps = te - ts
    return distance, t_elaps

print('')

for file in all_file_names:
    curr_file = os.path.join(data_dir, file)
    print(curr_file)
    all_scd.append(bin2scd(curr_file))

#print(calc_scd_dist_and_time(bin2scd(os.path.join(data_dir, '000000.bin')), bin2scd(os.path.join(data_dir, '004540.bin'))))
#print(calc_scd_dist_and_time((all_scd[0]), all_scd[4540]))

threshold = 0.46
threshold_counter = 0
loops = []
while threshold <= 0.5:
    counter = 0
    loops = []
    loops_i = []
    loops_i_tuple = []
    for i in range(51, len(all_scd)-1):
        print(i)
        loops_i_tuple = []
        for j in range(0, i-50):
            print(loops_i_tuple)
            distance, t1 = calc_scd_dist_and_time(all_scd[i], all_scd[j])
            if (distance <= threshold) and (i in loops_i):
                for dist in loops_i_tuple:
                    if dist[0] == i and distance < dist[1]:
                        loops_i_tuple.remove(dist)
                        loops_i_tuple.append((i, distance, j))
                        loops.remove((dist[0], dist[2]))
                        loops.append((i, j))
                #counter += 1
            elif distance <= threshold:
                loops.append((i,j))
                loops_i.append(i)
                loops_i_tuple.append((i, distance, j))
                #j += 1
                counter += 1
                #break
            j += 1
        i += 1
    
    with open(("loops/loops_in_" + args.sequence + "_" + str(threshold_counter) + ".txt"), 'w') as f:
        for loop in loops:
            f.write(str(loop))
            f.write('\n')
    with open(("info/info_" + args.sequence + ".txt"), 'a') as f:
        f.write(str(counter))
        f.write('\n')
    threshold += 0.01
    threshold_counter += 1

#print("data length: " + str(len(all_scd)-1))
#print("counter: " + str(counter))

#np.savetxt("output_00.txt", bin2scd(os.path.join(data_dir, '000000.bin')))