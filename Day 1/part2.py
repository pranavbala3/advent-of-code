import re

def calculate_sum(filename):
    f = open(filename, "r")
    sum = 0
    for line in f:
        num_string = ""
        line = re.sub('one', 'one1one', line)
        line = re.sub('two', 'two2two', line)
        line = re.sub('three', 'three3three', line)
        line = re.sub('four', 'four4four', line)
        line = line =re.sub('five', 'five5five', line)
        line = re.sub('six', 'six6six', line)
        line = re.sub('seven', 'seven7seven', line)
        line = re.sub('eight', 'eight8eight', line)
        line = re.sub('nine', 'nine9nine', line)
        for char in line:
            if char.isnumeric():
                num_string += char
        line_num = int(num_string[0]+num_string[-1])
        sum += line_num
    return sum

print(calculate_sum("input.txt"))