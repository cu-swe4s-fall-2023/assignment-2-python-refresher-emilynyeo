import sys

file_name = sys.argv[1]
country_name = sys.argv[2]
out_file = sys.argv[3]

f = open(out_file, 'w')  # Open the output file for writing ('w' mode).
for line in open(file_name):
    data = line.rstrip().split(',')
    if data[0] == country_name:
        f.write(str(float(data[2]) + float(data[3])) + '\n')