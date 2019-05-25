import time
import sys, os
'''
for _ in range(9):
  print('wait for something')
  time.sleep(60 * 5)
'''


print("timeout after change:" + os.environ['TIMEOUT'])


for key, val in os.environ.items():
  print(key + ": " + val)


print('finished')
