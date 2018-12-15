import subprocess
import linecache
import re

d = [0, 0, 0, 0, 0, 0]
f = open("data.txt",'w')

def get_data(file_path, line_number):
  return ' '.join(linecache.getline(file_path, line_number).split()).split(' ')[1]


i = [4, 2, 9, 5]
for a1 in range(3):
  for a2 in range(i[a1]):
    stats_path = 'd%dx%d/stats.txt'%(a1+1,a2)
    f.write('%s\n'%(get_data(stats_path, 3)))
f.close()