import subprocess
import linecache
import re

d1 = [256, 512, 1024, 2048, 4096]
d2 = [4, 8, 16, 32, 64, 128, 256]
d = [0, 0, 0, 0, 0, 0]
c = 1
f = open("data.txt")

def get_data(file_path, line_number):
  return linecache.getline(file_path, line_number).strip().split(' ')[1]

for a1 in d2:
  for a2 in d2:
    for a3 in d1:
      stats_path = 'hw3_%d/stats.txt'
      d[0] = get_data(stats_path,3)
      d[1] = get_data(stats_path,475)
      d[2] = get_data(stats_path,584)
      d[3] = get_data(stats_path,463)
      d[4] = get_data(stats_path,469)
      d[5] = get_data(stats_path,792)
      f.write('%s\n'%(' '.join(d)))
f.close()