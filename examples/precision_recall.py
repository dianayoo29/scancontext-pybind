import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import numpy as np 

ground_truth_data = 790
sc_input = "loop_detection/info/info_00.txt"
sc_common = "loop_detection/info/info_common_loops_00.txt"

sc_ringkey_input = "ringkey/info/info_00.txt"
sc_ringkey_common = "ringkey/info/info_common_loops_00.txt"
sc_ringkey_10_input = "ringkey_10/info/info_00.txt"
sc_ringkey_10_common = "ringkey_10/info/info_common_loops_00.txt"

# Küszöbértékes módszer
bin_all_avg_input = "binarization/thresholding/all_avg/info/info_00.txt"
bin_all_avg_common = "binarization/thresholding/all_avg/info/info_common_loops_00.txt"

bin_all_median_input = "binarization/thresholding/all_median/info/info_00.txt"
bin_all_median_common = "binarization/thresholding/all_median/info/info_common_loops_00.txt"

bin_row_avg_input = "binarization/thresholding/row_avg/info/info_00.txt"
bin_row_avg_common = "binarization/thresholding/row_avg/info/info_common_loops_00.txt"

bin_row_median_input = "binarization/thresholding/row_median/info/info_00.txt"
bin_row_median_common = "binarization/thresholding/row_median/info/info_common_loops_00.txt"

# Kvantálás módszer/ intevallumok szerinti felbontás módszer
bin_all_2bit_input = "binarization/quantization/all_2bit/info/info_00.txt"
bin_all_2bit_common = "binarization/quantization/all_2bit/info/info_common_loops_00.txt"
bin_all_2bit_input_hm1 = "binarization/quantization/all_2bit/info/info_00_hm1.txt"
bin_all_2bit_common_hm1 = "binarization/quantization/all_2bit/info/info_common_loops_00_hm1.txt"

bin_all_3bit_input = "binarization/quantization/all_3bit/info/info_00.txt"
bin_all_3bit_common = "binarization/quantization/all_3bit/info/info_common_loops_00.txt"
bin_all_3bit_input_hm1 = "binarization/quantization/all_3bit/info/info_00_hm1.txt"
bin_all_3bit_common_hm1 = "binarization/quantization/all_3bit/info/info_common_loops_00_hm1.txt"

bin_row_2bit_input = "binarization/quantization/row_2bit/info/info_00.txt"
bin_row_2bit_common = "binarization/quantization/row_2bit/info/info_common_loops_00.txt"
bin_row_2bit_input_hm1 = "binarization/quantization/row_2bit/info/info_00_hm1.txt"
bin_row_2bit_common_hm1 = "binarization/quantization/row_2bit/info/info_common_loops_00_hm1.txt"

bin_row_3bit_input = "binarization/quantization/row_3bit/info/info_00.txt"
bin_row_3bit_common = "binarization/quantization/row_3bit/info/info_common_loops_00.txt"
bin_row_3bit_input_hm1 = "binarization/quantization/row_3bit/info/info_00_hm1.txt"
bin_row_3bit_common_hm1 = "binarization/quantization/row_3bit/info/info_common_loops_00_hm1.txt"

# Adaptív kvantálás módszer
bin_ad_all_2bit_input = "binarization/adaptive_quantization/ad_all_2bit/info/info_00.txt"
bin_ad_all_2bit_common = "binarization/adaptive_quantization/ad_all_2bit/info/info_common_loops_00.txt"
bin_ad_all_2bit_input_hm1 = "binarization/adaptive_quantization/ad_all_2bit/info/info_00_hm1.txt"
bin_ad_all_2bit_common_hm1 = "binarization/adaptive_quantization/ad_all_2bit/info/info_common_loops_00_hm1.txt"

bin_ad_all_3bit_input = "binarization/adaptive_quantization/ad_all_3bit/info/info_00.txt"
bin_ad_all_3bit_common = "binarization/adaptive_quantization/ad_all_3bit/info/info_common_loops_00.txt"
bin_ad_all_3bit_input_hm1 = "binarization/adaptive_quantization/ad_all_3bit/info/info_00_hm1.txt"
bin_ad_all_3bit_common_hm1 = "binarization/adaptive_quantization/ad_all_3bit/info/info_common_loops_00_hm1.txt"

bin_ad_row_2bit_input = "binarization/adaptive_quantization/ad_row_2bit/info/info_00.txt"
bin_ad_row_2bit_common = "binarization/adaptive_quantization/ad_row_2bit/info/info_common_loops_00.txt"
bin_ad_row_2bit_input_hm1 = "binarization/adaptive_quantization/ad_row_2bit/info/info_00_hm1.txt"
bin_ad_row_2bit_common_hm1 = "binarization/adaptive_quantization/ad_row_2bit/info/info_common_loops_00_hm1.txt"

bin_ad_row_3bit_input = "binarization/adaptive_quantization/ad_row_3bit/info/info_00.txt"
bin_ad_row_3bit_common = "binarization/adaptive_quantization/ad_row_3bit/info/info_common_loops_00.txt"
bin_ad_row_3bit_input_hm1 = "binarization/adaptive_quantization/ad_row_3bit/info/info_00_hm1.txt"
bin_ad_row_3bit_common_hm1 = "binarization/adaptive_quantization/ad_row_3bit/info/info_common_loops_00_hm1.txt"

# Geometriai módszer
bin_geo_col_input = "binarization/geometric/column/info/info_00.txt"
bin_geo_col_common = "binarization/geometric/column/info/info_common_loops_00.txt"
bin_geo_row_input = "binarization/geometric/row/info/info_00.txt"
bin_geo_row_common = "binarization/geometric/row/info/info_common_loops_00.txt"

# 4. módszer - saját
bin_method_4_2bit_input = "binarization/method4/2bit/info/info_00.txt"
bin_method_4_2bit_common = "binarization/method4/2bit/info/info_common_loops_00.txt"
bin_method_4_3bit_input = "binarization/method4/3bit/info/info_00.txt"
bin_method_4_3bit_common = "binarization/method4/3bit/info/info_common_loops_00.txt"
bin_method_4_4bit_input = "binarization/method4/4bit/info/info_00.txt"
bin_method_4_4bit_common = "binarization/method4/4bit/info/info_common_loops_00.txt"

bin_method_4_3bit_intervals_input = "binarization/method4/3bit/info/info_00_intervals.txt"
bin_method_4_3bit_intervals_common = "binarization/method4/3bit/info/info_common_loops_00_intervals.txt"
bin_method_4_4bit_intervals_input = "binarization/method4/4bit/info/info_00_intervals.txt"
bin_method_4_4bit_intervals_common = "binarization/method4/4bit/info/info_common_loops_00_intervals.txt"

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

"""
def calculateAP(recall, precision):
    ap = 0
    rv_recall = list(reversed(recall))
    rv_precision = list(reversed(precision))
    for i in range(len(rv_recall)-1):
        ap += (rv_recall[i] - rv_recall[i+1]) * rv_precision[i]
    return ap
    #rv_recall = np.array(rv_recall)
    #rv_precision = np.array(rv_precision)
    #return np.sum((rv_recall[:-1] - rv_recall[1:]) * rv_precision[:-1])
    #return (1/len(precision))*(sum(precision))
"""
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
########################################################################################

# Scan Context - sima loop detection, ringkey nélkül
#sc_loop_counter = readInputFile(sc_input)
#sc_common_loop_counter = readInputFile(sc_common)
#sc_recall = calculate_recall(ground_truth_data, sc_common_loop_counter)
#sc_precision = calculate_precision(sc_loop_counter, sc_common_loop_counter)
#sc_ap = round(calculateAP(sc_recall, sc_precision), 4)

##########################################################################
print("Ringkey")
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
print("Thresholding")
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
print("Intervals")
# BIN ALL 2BIT
bin_all_2bit_loop_counter_hm1 = readInputFile(bin_all_2bit_input_hm1)
bin_common_all_2bit_loop_counter_hm1 = readInputFile(bin_all_2bit_common_hm1)
bin_all_2bit_recall_hm1 = calculate_recall(ground_truth_data, bin_common_all_2bit_loop_counter_hm1)
bin_all_2bit_precision_hm1 = calculate_precision(bin_all_2bit_loop_counter_hm1, bin_common_all_2bit_loop_counter_hm1)
bin_all_2bit_ap_hm1 = round(calculateAP(bin_all_2bit_recall_hm1, bin_all_2bit_precision_hm1), 4)

bin_all_2bit_loop_counter = readInputFile(bin_all_2bit_input)
bin_common_all_2bit_loop_counter = readInputFile(bin_all_2bit_common)
bin_all_2bit_recall = calculate_recall(ground_truth_data, bin_common_all_2bit_loop_counter)
bin_all_2bit_precision = calculate_precision(bin_all_2bit_loop_counter, bin_common_all_2bit_loop_counter)
bin_all_2bit_ap = round(calculateAP(bin_all_2bit_recall, bin_all_2bit_precision), 4)

# BIN ALL 3BIT
bin_all_3bit_loop_counter_hm1 = readInputFile(bin_all_3bit_input_hm1)
bin_common_all_3bit_loop_counter_hm1 = readInputFile(bin_all_3bit_common_hm1)
bin_all_3bit_recall_hm1 = calculate_recall(ground_truth_data, bin_common_all_3bit_loop_counter_hm1)
bin_all_3bit_precision_hm1 = calculate_precision(bin_all_3bit_loop_counter_hm1, bin_common_all_3bit_loop_counter_hm1)
bin_all_3bit_ap_hm1 = round(calculateAP(bin_all_3bit_recall_hm1, bin_all_3bit_precision_hm1), 4)

bin_all_3bit_loop_counter = readInputFile(bin_all_3bit_input)
bin_common_all_3bit_loop_counter = readInputFile(bin_all_3bit_common)
bin_all_3bit_recall = calculate_recall(ground_truth_data, bin_common_all_3bit_loop_counter)
bin_all_3bit_precision = calculate_precision(bin_all_3bit_loop_counter, bin_common_all_3bit_loop_counter)
bin_all_3bit_ap = round(calculateAP(bin_all_3bit_recall, bin_all_3bit_precision), 4)

# BIN ROW 2BIT

bin_row_2bit_loop_counter_hm1 = readInputFile(bin_row_2bit_input_hm1)
bin_common_row_2bit_loop_counter_hm1 = readInputFile(bin_row_2bit_common_hm1)
bin_row_2bit_recall_hm1 = calculate_recall(ground_truth_data, bin_common_row_2bit_loop_counter_hm1)
bin_row_2bit_precision_hm1 = calculate_precision(bin_row_2bit_loop_counter_hm1, bin_common_row_2bit_loop_counter_hm1)
bin_row_2bit_ap_hm1 = round(calculateAP(bin_row_2bit_recall_hm1, bin_row_2bit_precision_hm1), 4)

bin_row_2bit_loop_counter = readInputFile(bin_row_2bit_input)
bin_common_row_2bit_loop_counter = readInputFile(bin_row_2bit_common)
bin_row_2bit_recall = calculate_recall(ground_truth_data, bin_common_row_2bit_loop_counter)
bin_row_2bit_precision = calculate_precision(bin_row_2bit_loop_counter, bin_common_row_2bit_loop_counter)
bin_row_2bit_ap = round(calculateAP(bin_row_2bit_recall, bin_row_2bit_precision), 4)

# BIN ROW 3BIT
bin_row_3bit_loop_counter_hm1 = readInputFile(bin_row_3bit_input_hm1)
bin_common_row_3bit_loop_counter_hm1 = readInputFile(bin_row_3bit_common_hm1)
bin_row_3bit_recall_hm1 = calculate_recall(ground_truth_data, bin_common_row_3bit_loop_counter_hm1)
bin_row_3bit_precision_hm1 = calculate_precision(bin_row_3bit_loop_counter_hm1, bin_common_row_3bit_loop_counter_hm1)
bin_row_3bit_ap_hm1 = round(calculateAP(bin_row_3bit_recall_hm1, bin_row_3bit_precision_hm1), 4)

bin_row_3bit_loop_counter = readInputFile(bin_row_3bit_input)
bin_common_row_3bit_loop_counter = readInputFile(bin_row_3bit_common)
bin_row_3bit_recall = calculate_recall(ground_truth_data, bin_common_row_3bit_loop_counter)
bin_row_3bit_precision = calculate_precision(bin_row_3bit_loop_counter, bin_common_row_3bit_loop_counter)
bin_row_3bit_ap = round(calculateAP(bin_row_3bit_recall, bin_row_3bit_precision), 4)

##########################################################################
print("Adaptive Quant")
# BIN ALL 2BIT ADAPTIVE QUANTIZATION
bin_ad_all_2bit_loop_counter_hm1 = readInputFile(bin_ad_all_2bit_input_hm1)
bin_ad_common_all_2bit_loop_counter_hm1 = readInputFile(bin_ad_all_2bit_common_hm1)
bin_ad_all_2bit_recall_hm1 = calculate_recall(ground_truth_data, bin_ad_common_all_2bit_loop_counter_hm1)
bin_ad_all_2bit_precision_hm1 = calculate_precision(bin_ad_all_2bit_loop_counter_hm1, bin_ad_common_all_2bit_loop_counter_hm1)
bin_ad_all_2bit_ap_hm1 = round(calculateAP(bin_ad_all_2bit_recall_hm1, bin_ad_all_2bit_precision_hm1), 4)

bin_ad_all_2bit_loop_counter = readInputFile(bin_ad_all_2bit_input)
bin_ad_common_all_2bit_loop_counter = readInputFile(bin_ad_all_2bit_common)
bin_ad_all_2bit_recall = calculate_recall(ground_truth_data, bin_ad_common_all_2bit_loop_counter)
bin_ad_all_2bit_precision = calculate_precision(bin_ad_all_2bit_loop_counter, bin_ad_common_all_2bit_loop_counter)
bin_ad_all_2bit_ap = round(calculateAP(bin_ad_all_2bit_recall, bin_ad_all_2bit_precision), 4)

# BIN ALL 3BIT ADAPTIVE QUANTIZATION
bin_ad_all_3bit_loop_counter_hm1 = readInputFile(bin_ad_all_3bit_input_hm1)
bin_ad_common_all_3bit_loop_counter_hm1 = readInputFile(bin_ad_all_3bit_common_hm1)
bin_ad_all_3bit_recall_hm1 = calculate_recall(ground_truth_data, bin_ad_common_all_3bit_loop_counter_hm1)
bin_ad_all_3bit_precision_hm1 = calculate_precision(bin_ad_all_3bit_loop_counter_hm1, bin_ad_common_all_3bit_loop_counter_hm1)
bin_ad_all_3bit_ap_hm1 = round(calculateAP(bin_ad_all_3bit_recall_hm1, bin_ad_all_3bit_precision_hm1), 4)

bin_ad_all_3bit_loop_counter = readInputFile(bin_ad_all_3bit_input)
bin_ad_common_all_3bit_loop_counter = readInputFile(bin_ad_all_3bit_common)
bin_ad_all_3bit_recall = calculate_recall(ground_truth_data, bin_ad_common_all_3bit_loop_counter)
bin_ad_all_3bit_precision = calculate_precision(bin_ad_all_3bit_loop_counter, bin_ad_common_all_3bit_loop_counter)
bin_ad_all_3bit_ap = round(calculateAP(bin_ad_all_3bit_recall, bin_ad_all_3bit_precision), 4)

# BIN Row 2BIT ADAPTIVE QUANTIZATION
bin_ad_row_2bit_loop_counter_hm1 = readInputFile(bin_ad_row_2bit_input_hm1)
bin_ad_common_row_2bit_loop_counter_hm1 = readInputFile(bin_ad_row_2bit_common_hm1)
bin_ad_row_2bit_recall_hm1 = calculate_recall(ground_truth_data, bin_ad_common_row_2bit_loop_counter_hm1)
bin_ad_row_2bit_precision_hm1 = calculate_precision(bin_ad_row_2bit_loop_counter_hm1, bin_ad_common_row_2bit_loop_counter_hm1)
bin_ad_row_2bit_ap_hm1 = round(calculateAP(bin_ad_row_2bit_recall_hm1, bin_ad_row_2bit_precision_hm1), 4)

bin_ad_row_2bit_loop_counter = readInputFile(bin_ad_row_2bit_input)
bin_ad_common_row_2bit_loop_counter = readInputFile(bin_ad_row_2bit_common)
bin_ad_row_2bit_recall = calculate_recall(ground_truth_data, bin_ad_common_row_2bit_loop_counter)
bin_ad_row_2bit_precision = calculate_precision(bin_ad_row_2bit_loop_counter, bin_ad_common_row_2bit_loop_counter)
bin_ad_row_2bit_ap = round(calculateAP(bin_ad_row_2bit_recall, bin_ad_row_2bit_precision), 4)

# BIN Row 3BIT ADAPTIVE QUANTIZATION
bin_ad_row_3bit_loop_counter_hm1 = readInputFile(bin_ad_row_3bit_input_hm1)
bin_ad_common_row_3bit_loop_counter_hm1 = readInputFile(bin_ad_row_3bit_common_hm1)
bin_ad_row_3bit_recall_hm1 = calculate_recall(ground_truth_data, bin_ad_common_row_3bit_loop_counter_hm1)
bin_ad_row_3bit_precision_hm1 = calculate_precision(bin_ad_row_3bit_loop_counter_hm1, bin_ad_common_row_3bit_loop_counter_hm1)
bin_ad_row_3bit_ap_hm1 = round(calculateAP(bin_ad_row_3bit_recall_hm1, bin_ad_row_3bit_precision_hm1), 4)

bin_ad_row_3bit_loop_counter = readInputFile(bin_ad_row_3bit_input)
bin_ad_common_row_3bit_loop_counter = readInputFile(bin_ad_row_3bit_common)
bin_ad_row_3bit_recall = calculate_recall(ground_truth_data, bin_ad_common_row_3bit_loop_counter)
bin_ad_row_3bit_precision = calculate_precision(bin_ad_row_3bit_loop_counter, bin_ad_common_row_3bit_loop_counter)
bin_ad_row_3bit_ap = round(calculateAP(bin_ad_row_3bit_recall, bin_ad_row_3bit_precision), 4)

##########################################################################
print("Geometric")
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

############################################################################################
print("New method")
# method 4, 2bit
bin_method_4_2bit_loop_counter = readInputFile(bin_method_4_2bit_input)
bin_common_method_4_2bit_loop_counter = readInputFile(bin_method_4_2bit_common)
bin_method_4_2bit_recall = calculate_recall(ground_truth_data, bin_common_method_4_2bit_loop_counter)
bin_method_4_2bit_precision = calculate_precision(bin_method_4_2bit_loop_counter, bin_common_method_4_2bit_loop_counter)
bin_method_4_2bit_ap = round(calculateAP(bin_method_4_2bit_recall, bin_method_4_2bit_precision), 4)

# method 4, 3bit
bin_method_4_3bit_loop_counter = readInputFile(bin_method_4_3bit_input)
bin_common_method_4_3bit_loop_counter = readInputFile(bin_method_4_3bit_common)
bin_method_4_3bit_recall = calculate_recall(ground_truth_data, bin_common_method_4_3bit_loop_counter)
bin_method_4_3bit_precision = calculate_precision(bin_method_4_3bit_loop_counter, bin_common_method_4_3bit_loop_counter)
bin_method_4_3bit_ap = round(calculateAP(bin_method_4_3bit_recall, bin_method_4_3bit_precision), 4)

bin_method_4_3bit_intervals_loop_counter = readInputFile(bin_method_4_3bit_intervals_input)
bin_common_method_4_3bit_intervals_loop_counter = readInputFile(bin_method_4_3bit_intervals_common)
bin_method_4_3bit_intervals_recall = calculate_recall(ground_truth_data, bin_common_method_4_3bit_intervals_loop_counter)
bin_method_4_3bit_intervals_precision = calculate_precision(bin_method_4_3bit_intervals_loop_counter, bin_common_method_4_3bit_intervals_loop_counter)
bin_method_4_3bit_intervals_ap = round(calculateAP(bin_method_4_3bit_intervals_recall, bin_method_4_3bit_intervals_precision), 4)

# method 4, 4bit
bin_method_4_4bit_loop_counter = readInputFile(bin_method_4_4bit_input)
bin_common_method_4_4bit_loop_counter = readInputFile(bin_method_4_4bit_common)
bin_method_4_4bit_recall = calculate_recall(ground_truth_data, bin_common_method_4_4bit_loop_counter)
bin_method_4_4bit_precision = calculate_precision(bin_method_4_4bit_loop_counter, bin_common_method_4_4bit_loop_counter)
bin_method_4_4bit_ap = round(calculateAP(bin_method_4_4bit_recall, bin_method_4_4bit_precision), 4)

# method 4, 4bit with intervals
bin_method_4_4bit_intervals_loop_counter = readInputFile(bin_method_4_4bit_intervals_input)
bin_common_method_4_4bit_intervals_loop_counter = readInputFile(bin_method_4_4bit_intervals_common)
bin_method_4_4bit_intervals_recall = calculate_recall(ground_truth_data, bin_common_method_4_4bit_intervals_loop_counter)
bin_method_4_4bit_intervals_precision = calculate_precision(bin_method_4_4bit_intervals_loop_counter, bin_common_method_4_4bit_intervals_loop_counter)
bin_method_4_4bit_intervals_ap = round(calculateAP(bin_method_4_4bit_intervals_recall, bin_method_4_4bit_intervals_precision), 4)

#plt1.plot(sc_recall, sc_precision, 'o-b', label = ("ScanContext-without-Ringkey" + "(AP=" + str(sc_ap) + ")"))
#plt1.title(label="Ismétlődő pontok detektálása [KITTI 00]") 
plt1.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt1.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt1.xlabel('Recall')
plt1.ylabel('Precision')
plt1.xlim(0.1, 1.05)
plt1.ylim(0.1, 1.05)
plt1.legend()
plt1.show()

# Method 1 - Thresholding
#plt1.title(label="Binarizálás határértékkel[Scan Context-50]") 
plt.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt.plot(bin_avg_all_recall, bin_avg_all_precision, 'o-m', label = ("Dataset-AVG" + "(AP=" + str(bin_avg_all_ap) + ")"))
plt.plot(bin_median_all_recall, bin_median_all_precision, 'o-b', label = ("Dataset-Median" + "(AP=" + str(bin_median_all_ap) + ")"))
plt.plot(bin_avg_row_recall, bin_avg_row_precision, 'o-c', label = ("Row-AVG" + "(AP=" + str(bin_avg_row_ap) + ")"))
plt.plot(bin_median_row_recall, bin_median_row_precision, 'o-y', label = ("Row-Median" + "(AP=" + str(bin_median_row_ap) + ")"))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim(0.1, 1.05)
plt.ylim(0.1, 1.05)
plt.legend() 
plt.show()

#plt2.title(label="Binarizálás kvantálással [Scan Context-50]") 
plt2.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt2.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt2.plot(bin_all_2bit_recall_hm1, bin_all_2bit_precision_hm1, 'o-y', label = ("Q-Dataset[2 bit|HM1]" + "(AP=" + str(bin_all_2bit_ap_hm1) + ")"))
plt2.plot(bin_all_2bit_recall, bin_all_2bit_precision, '*-y', label = ("Q-Dataset[2 bit|HM2]" + "(AP=" + str(bin_all_2bit_ap) + ")")) #Kvantálás az egész adathalmaz kvantiliseivel
plt2.plot(bin_all_3bit_recall_hm1, bin_all_3bit_precision_hm1, 'o-b', label = ("Q-Dataset[3 bit|HM1]" + "(AP=" + str(bin_all_3bit_ap_hm1) + ")"))
plt2.plot(bin_all_3bit_recall, bin_all_3bit_precision, '*-b', label = ("Q-Dataset[3 bit|HM2]" + "(AP=" + str(bin_all_3bit_ap) + ")"))
plt2.plot(bin_row_2bit_recall_hm1, bin_row_2bit_precision_hm1, 'o-k', label = ("Q-Row[2 bit|HM1]" + "(AP=" + str(bin_row_2bit_ap_hm1) + ")"))
plt2.plot(bin_row_2bit_recall, bin_row_2bit_precision, '*-k', label = ("Q-Row[2 bit|HM2]" + "(AP=" + str(bin_row_2bit_ap) + ")"))
plt2.plot(bin_row_3bit_recall_hm1, bin_row_3bit_precision_hm1, 'o-m', label = ("Q-Row[3 bit|HM1]" + "(AP=" + str(bin_row_3bit_ap_hm1) + ")"))
plt2.plot(bin_row_3bit_recall, bin_row_3bit_precision, '*-m', label = ("Q-Row[3 bit|HM2]" + "(AP=" + str(bin_row_3bit_ap) + ")"))

plt2.xlabel('Recall')
plt2.ylabel('Precision')
plt2.xlim(0.1, 1.05)
plt2.ylim(0.1, 1.05)
plt2.legend() 
plt2.show()


plt3.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt3.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt3.plot(bin_ad_all_2bit_recall_hm1, bin_ad_all_2bit_precision_hm1, 'o-k', label = ("AQ-Dataset[2 bit|HM1]" + "(AP=" + str(bin_ad_all_2bit_ap_hm1) + ")"))
plt3.plot(bin_ad_all_2bit_recall, bin_ad_all_2bit_precision, '*-k', label = ("AQ-Dataset[2 bit|HM2]" + "(AP=" + str(bin_ad_all_2bit_ap) + ")")) # Binarized-ScanContext-AdaptiveQuantization-ALL-2bit-HM2
plt3.plot(bin_ad_all_3bit_recall_hm1, bin_ad_all_3bit_precision_hm1, 'o-m', label = ("AQ-Dataset[3 bit|HM1]" + "(AP=" + str(bin_ad_all_3bit_ap_hm1) + ")"))
plt3.plot(bin_ad_all_3bit_recall, bin_ad_all_3bit_precision, '*-m', label = ("AQ-Dataset[3 bit|HM2]" + "(AP=" + str(bin_ad_all_3bit_ap) + ")"))
plt3.plot(bin_ad_row_2bit_recall_hm1, bin_ad_row_2bit_precision_hm1, 'o-c', label = ("AQ-Row[2 bit|HM1]" + "(AP=" + str(bin_ad_row_2bit_ap_hm1) + ")"))
plt3.plot(bin_ad_row_2bit_recall, bin_ad_row_2bit_precision, '*-c', label = ("AQ-Row[2 bit|HM2]" + "(AP=" + str(bin_ad_row_2bit_ap) + ")"))
plt3.plot(bin_ad_row_3bit_recall_hm1, bin_ad_row_3bit_precision_hm1, 'o-b', label = ("AQ-Row[3 bit|HM1]" + "(AP=" + str(bin_ad_row_3bit_ap_hm1) + ")"))
plt3.plot(bin_ad_row_3bit_recall, bin_ad_row_3bit_precision, '*-b', label = ("AQ-Row[3 bit|HM2]" + "(AP=" + str(bin_ad_row_3bit_ap) + ")"))
plt3.xlabel('Recall')
plt3.ylabel('Precision')
plt3.xlim(0.1, 1.05)
plt3.ylim(0.1, 1.05)
plt3.legend() 
plt3.show()


plt4.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt4.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt4.plot(bin_geo_col_recall, bin_geo_col_precision, 'o-m', label = ("Rule-based-COLUMN" + "(AP=" + str(bin_geo_col_ap) + ")"))
plt4.plot(bin_geo_row_recall, bin_geo_row_precision, 'o-b', label = ("Rule-based-ROW" + "(AP=" + str(bin_geo_row_ap) + ")"))
plt4.xlabel('Recall')
plt4.ylabel('Precision')
plt4.xlim(0.1, 1.05)
plt4.ylim(0.1, 1.05)
plt4.legend() 
plt4.show()

#plt5.title("ScanContext binarizált adatokon - 4. módszer")
plt5.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt5.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt5.plot(bin_method_4_2bit_recall, bin_method_4_2bit_precision, 'o-m', label = ("Max-Height-2bit" + "(AP=" + str(bin_method_4_2bit_ap) + ")"))
plt5.plot(bin_method_4_3bit_recall, bin_method_4_3bit_precision, 'o-c', label = ("Max-Height-AQ-3bit" + "(AP=" + str(bin_method_4_3bit_ap) + ")"))
plt5.plot(bin_method_4_3bit_intervals_recall, bin_method_4_3bit_intervals_precision, 'o-k', label = ("Max-Height-Q-3bit" + "(AP=" + str(bin_method_4_3bit_intervals_ap) + ")"))
plt5.plot(bin_method_4_4bit_recall, bin_method_4_4bit_precision, 'o-y', label = ("Max-Height-AQ-4bit" + "(AP=" + str(bin_method_4_4bit_ap) + ")"))
plt5.plot(bin_method_4_4bit_intervals_recall, bin_method_4_4bit_intervals_precision, 'o-b', label = ("Max-Height-Q-4bit" + "(AP=" + str(bin_method_4_4bit_intervals_ap) + ")"))
plt5.xlabel('Recall')
plt5.ylabel('Precision')
plt5.xlim(0.1, 1.05)
plt5.ylim(0.1, 1.05)
plt5.legend() 
plt5.show()


plt6.plot(ringkey_recall, ringkey_precision, 'o-r', label = ("ScanContext-50" + "(AP=" + str(ringkey_ap) + ")"))
plt6.plot(ringkey_10_recall, ringkey_10_precision, 'o-g', label = ("ScanContext-10" + "(AP=" + str(ringkey_10_ap) + ")"))
plt6.plot(bin_median_all_recall, bin_median_all_precision, 'o-b', label = ("Dataset-Median" + "(AP=" + str(bin_median_all_ap) + ")"))
plt6.plot(bin_all_2bit_recall, bin_all_2bit_precision, 'o-y', label = ("Q-Dataset[2 bit|HM2]" + "(AP=" + str(bin_all_2bit_ap) + ")")) #Kvantálás az egész adathalmaz kvantiliseivel
plt6.plot(bin_ad_all_3bit_recall, bin_ad_all_3bit_precision, 'o-m', label = ("AQ-Dataset[3 bit|HM2]" + "(AP=" + str(bin_ad_all_3bit_ap) + ")"))
plt6.plot(bin_geo_col_recall, bin_geo_col_precision, 'o-k', label = ("Rule-based-COLUMN" + "(AP=" + str(bin_geo_col_ap) + ")"))
plt6.plot(bin_method_4_4bit_recall, bin_method_4_4bit_precision, 'o-c', label = ("Max-Height-AQ-4bit" + "(AP=" + str(bin_method_4_4bit_ap) + ")"))
plt6.xlabel('Recall')
plt6.ylabel('Precision')
plt6.xlim(0.1, 1.05)
plt6.ylim(0.1, 1.05)
plt6.legend() 
plt6.show()