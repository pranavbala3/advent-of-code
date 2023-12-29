
def calculate_sum(filename):
    f = open(filename, "r")
    sum = 0
    for line in f:
        num_string = ""
        for char in line:
            if char.isnumeric():
                num_string += char
        line_num = int(num_string[0]+num_string[-1])
        sum += line_num
    return sum

print(calculate_sum("input.txt"))