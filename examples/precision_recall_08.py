import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import numpy as np 

ground_truth_data = 332
sc_ringkey_input = "ringkey/info/info_08.txt"
sc_ringkey_common = "ringkey/info/info_common_loops_08.txt"
sc_ringkey_10_input = "ringkey_10/info/info_08.txt"
sc_ringkey_10_common = "ringkey_10/info/info_common_loops_08.txt"

# Küszöbértékes módszer
bin_all_avg_input = "binarization/thresholding/all_avg/info/info_08.txt"
bin_all_avg_common = "binarization/thresholding/all_avg/info/info_common_loops_08.txt"

bin_all_median_input = "binarization/thresholding/all_median/info/info_08.txt"
bin_all_median_common = "binarization/thresholding/all_median/info/info_common_loops_08.txt"

bin_row_avg_input = "binarization/thresholding/row_avg/info/info_08.txt"
bin_row_avg_common = "binarization/thresholding/row_avg/info/info_common_loops_08.txt"

bin_row_median_input = "binarization/thresholding/row_median/info/info_08.txt"
bin_row_median_common = "binarization/thresholding/row_median/info/info_common_loops_08.txt"

# Geometriai módszer
bin_geo_col_input = "binarization/geometric/column/info/info_08.txt"
bin_geo_col_common = "binarization/geometric/column/info/info_common_loops_08.txt"
bin_geo_row_input = "binarization/geometric/row/info/info_08.txt"
bin_geo_row_common = "binarization/geometric/row/info/info_common_loops_08.txt"


def calculate_precision(sc_loops, common_loops):
    precision_list = []
    for i in range(0, len(sc_loops)):
        TP = common_loops[i]
        TP_FP = sc_loops[i]
        if TP != 0 and TP_FP != 0:
            precision_list.append((TP/TP_FP))
        else:
            precision_list.append(0)
    return precision_list

def calculate_recall(gt_data, common_loops):
    recall_list = []
    TP_FN = gt_data
    for i in range(0, len(common_loops)):
        TP = common_loops[i]
        if TP != 0:
            recall_list.append((TP/TP_FN))
        else:
            recall_list.append(0)
    return recall_list

def readInputFile(file_name):
    loop_counter = []
    with open(file_name, "r") as input:
        Lines = input.readlines()
        for line in Lines:
            loop_counter.append(int(line))
    return loop_counter

def calculateAP(recall, precision):
    ap = 0
    rv_recall = list(reversed(recall))
    rv_precision = list(reversed(precision))
    rv_recall.append(0)
    rv_precision.append(1)
    rv_recall = np.array(rv_recall)
    rv_precision = np.array(rv_precision)
    counter = 0
    # recall max 0.5
    # precision min 0.5
    for i in range(len(rv_recall)-1):
        if rv_recall[i] >= 0.5 and rv_precision[i] >= 0.5:
            #print(rv_recall[i])
            counter += 1
        ap += (rv_recall[i] - rv_recall[i+1]) * rv_precision[i]
    print(counter)
    return ap

##########################################################################

# RINGKEY - Scan Context - 50
ringkey_sc_loop_counter = readInputFile(sc_ringkey_input)
ringkey_common_loop_counter = readInputFile(sc_ringkey_common)
ringkey_recall = calculate_recall(ground_truth_data, ringkey_common_loop_counter)
ringkey_precision = calculate_precision(ringkey_sc_loop_counter, ringkey_common_loop_counter)
ringkey_ap = round(calculateAP(ringkey_recall, ringkey_precision), 4)

# RINGKEY - Scan Context - 10
ringkey_10_sc_loop_counter = readInputFile(sc_ringkey_10_input)
ringkey_10_common_loop_counter = readInputFile(sc_ringkey_10_common)
ringkey_10_recall = calculate_recall(ground_truth_data, ringkey_10_common_loop_counter)
ringkey_10_precision = calculate_precision(ringkey_10_sc_loop_counter, ringkey_10_common_loop_counter)
ringkey_10_ap = round(calculateAP(ringkey_10_recall, ringkey_10_precision), 4)

##########################################################################
# BIN AVG ALL
bin_avg_all_loop_counter = readInputFile(bin_all_avg_input)
bin_avg_common_all_loop_counter = readInputFile(bin_all_avg_common)
bin_avg_all_recall = calculate_recall(ground_truth_data, bin_avg_common_all_loop_counter)
bin_avg_all_precision = calculate_precision(bin_avg_all_loop_counter, bin_avg_common_all_loop_counter)
bin_avg_all_ap = round(calculateAP(bin_avg_all_recall, bin_avg_all_precision), 4)
# BIN MEDIAN ALL
bin_median_all_loop_counter = readInputFile(bin_all_median_input)
bin_median_common_all_loop_counter = readInputFile(bin_all_median_common)
bin_median_all_recall = calculate_recall(ground_truth_data, bin_median_common_all_loop_counter)
bin_median_all_precision = calculate_precision(bin_median_all_loop_counter, bin_median_common_all_loop_counter)
bin_median_all_ap = round(calculateAP(bin_median_all_recall, bin_median_all_precision), 4)

# BIN AVG ROW
bin_avg_row_loop_counter = readInputFile(bin_row_avg_input)
bin_avg_common_row_loop_counter = readInputFile(bin_row_avg_common)
bin_avg_row_recall = calculate_recall(ground_truth_data, bin_avg_common_row_loop_counter)
bin_avg_row_precision = calculate_precision(bin_avg_row_loop_counter, bin_avg_common_row_loop_counter)
bin_avg_row_ap = round(calculateAP(bin_avg_row_recall, bin_avg_row_precision), 4)

# BIN MEDIAN ROW
bin_median_row_loop_counter = readInputFile(bin_row_median_input)
bin_median_common_row_loop_counter = readInputFile(bin_row_median_common)
bin_median_row_recall = calculate_recall(ground_truth_data, bin_median_common_row_loop_counter)
bin_median_row_precision = calculate_precision(bin_median_row_loop_counter, bin_median_common_row_loop_counter)
bin_median_row_ap = round(calculateAP(bin_median_row_recall, bin_median_row_precision), 4)

##########################################################################

# BIN GEO COL
bin_geo_col_loop_counter = readInputFile(bin_geo_col_input)
bin_common_geo_col_loop_counter = readInputFile(bin_geo_col_common)
bin_geo_col_recall = calculate_recall(ground_truth_data, bin_common_geo_col_loop_counter)
bin_geo_col_precision = calculate_precision(bin_geo_col_loop_counter, bin_common_geo_col_loop_counter)
bin_geo_col_ap = round(calculateAP(bin_geo_col_recall, bin_geo_col_precision), 4)

# BIN GEO ROW
bin_geo_row_loop_counter = readInputFile(bin_geo_row_input)
bin_common_geo_row_loop_counter = readInputFile(bin_geo_row_common)
bin_geo_row_recall = calculate_recall(ground_truth_data, bin_common_geo_row_loop_counter)
bin_geo_row_precision = calculate_precision(bin_geo_row_loop_counter, bin_common_geo_row_loop_counter)
bin_geo_row_ap = round(calculateAP(bin_geo_row_recall, bin_geo_row_precision), 4)

##########################################################################

plt1.plot(ringkey_recall, ringkey_precision, 'o-r', label = "ScanContext-50-with-RingKey")
plt1.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = "ScanContext-10-with-RingKey")
plt1.xlabel('Recall')
plt1.ylabel('Precision')
plt1.legend() 
plt1.show()

# Method 1 - Thresholding
plt.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50-with-RingKey" + "(AP=" + str(ringkey_ap) + ")"))
plt.plot(bin_avg_all_recall, bin_avg_all_precision, 'o-g', label = ("Binarized-ScanContext-50-AVG-All" + "(AP=" + str(bin_avg_all_ap) + ")"))
plt.plot(bin_median_all_recall, bin_median_all_precision, 'o-b', label = ("Binarized-ScanContext-50-MEDIAN-All" + "(AP=" + str(bin_median_all_ap) + ")"))
plt.plot(bin_avg_row_recall, bin_avg_row_precision, 'o-c', label = ("Binarized-ScanContext-50-AVG-Row" + "(AP=" + str(bin_avg_row_ap) + ")"))
plt.plot(bin_median_row_recall, bin_median_row_precision, 'o-y', label = ("Binarized-ScanContext-50-MEDIAN-Row" + "(AP=" + str(bin_median_row_ap) + ")"))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend() 
plt.show()

plt4.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50-with-RingKey" + "(AP=" + str(ringkey_ap) + ")"))
plt4.plot(bin_geo_col_recall, bin_geo_col_precision, 'o-m', label = ("Binarized-ScanContext-Geometric-COLUMN" + "(AP=" + str(bin_geo_col_ap) + ")"))
plt4.plot(bin_geo_row_recall, bin_geo_row_precision, 'o-b', label = ("Binarized-ScanContext-Geometric-ROW" + "(AP=" + str(bin_geo_row_ap) + ")"))
plt4.xlabel('Recall')
plt4.ylabel('Precision')
plt4.legend() 
plt4.show()
