import argparse

# python3 compare_loops.py --seq 00 
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seq", dest="seq", help="Choose a sequence[00|02|05|08]", required=True)
args = parser.parse_args()

for i in range(0, 2):
    gt_loops = []
    with open(("../ground_truth/ground_truth_loops_in_" + args.seq + ".txt")) as gt_00:
        print("../ground_truth/ground_truth_loops_in_" + args.seq + ".txt")
        Lines = gt_00.readlines()
        for line in Lines:
            gt_loops.append(line)

    sc_loops = []
    with open(("loops/loops_in_" + args.seq + "_" + str(i) + ".txt")) as sc_00:
        Lines = sc_00.readlines()
        for line in Lines:
            sc_loops.append(line)

    common_loops = []
    counter = 0
    common_loop_ids = []
    for loop in sc_loops:
        split_loop = loop.split(", ")
        loop_i = split_loop[0].replace("(", "").replace(")", "")
        if loop in gt_loops and loop_i not in common_loop_ids:
            common_loops.append(loop)
            common_loop_ids.append(loop_i)
            counter += 1

    with open(("common_loops/common_loops_" + args.seq + "_" + str(i) + ".txt"), 'w') as output:
        output.write(("Counter: " + str(counter)+ "\n"))
        for loop in common_loops:
            output.write(str(loop))
    with open(("info/info_common_loops_" + args.seq + ".txt"), 'a') as f:
        f.write(str(counter))
        f.write('\n')
    