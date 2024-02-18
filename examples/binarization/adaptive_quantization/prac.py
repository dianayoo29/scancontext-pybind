import numpy as np 

def calculateQuantileForAll(all_values):
    quantiles = []
    temp_all_values = all_values
    for i in temp_all_values:
        if i == 0.0:
            temp_all_values.remove(i)
    quantiles.append(np.quantile(temp_all_values, .33))
    quantiles.append(np.quantile(temp_all_values, .66))
    quantiles.sort()
    return quantiles

# 00 -> 0.0
# 01 -> x < 33
# 10 -> 33 < x < 66
# 11 -> x > 66

all_values = [0.0, -0.9203001260757446, -1.721894900004069, -1.846898106428293, -1.6886239051818848, 0.0,
              0.3678230692942937, -1.8247564334135788, -1.6725625038146972, 0.0, -0.9203001260757446, -1.721894900004069, -1.846898106428293, -1.6886239051818848, 0.0,
              0.3678230692942937, -1.8247564334135788, -1.6725625038146972, 0.0]
print(calculateQuantileForAll(all_values))
