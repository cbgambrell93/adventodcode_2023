import re

inputs = open("test.txt", "r")

cal_line = []
numbers = []
for line in inputs.readlines():
    cal_line.append(line)


for line in cal_line:
    isint = 0
    line_len = len(line)
    i = 0
    int_array = []
    while i < line_len:
        try:
            isint = int(line[i])
        except:
            isint = line[i]
        if isinstance(isint, int):
            int_array.append(isint)
        i+=1
    numbers.append(int(str(int_array[0]) + str(int_array[len(int_array)-1])))

print(sum(numbers))

