#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#open the file and get rid of the $
# data = np.loadtxt(u"C:\Users\eduar\OneDrive\Desktop\g823_2022175_1523.log", dtype = "str",
# delimiter="$")
filename = 'g823_2022175_1523.log'

#data = np.loadtxt(filename, delimiter="$", dtype="str")

field_value_list = []
signal_value_list = []
for line in open(filename,'r'):
    split_line = line.split(',')
    #print(split_line)
    field_value_str = split_line[0][2:]
    field_value = float(field_value_str)
    field_value_list.append(field_value)
    #print(field_value)

    signal_value_str = split_line[1].replace('\n','')
    signal_value = int(signal_value_str)
    signal_value_list.append(signal_value)


#remove leading whitespace
#data.strip

#test print (remove this eventually)
#print(data[:5])

field_value_array = np.array(field_value_list)
signal_value_array = np.array(signal_value_list)

# x data is a numpy array of times, 10 points per second -- 0,0.1,0.2, etc...
# the same length as the two data arrays

# example plot:
plt.plot(field_value_array)
plt.savefig('field_value.png')

# x = data[:, 0]
# y = data[:, 1]


# #plot 1:
# x = np.array
# y = np.array(-------)
#
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title("-------")
#
#
# #plot 2:
# x = np.array(------)
# y = np.array(------)
#
# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.title("-------")
#
# plt.suptitle("Mag. Test Data")
# plt.show()
