import time
import sys, os
'''
for _ in range(9):
  print('wait for something')
  time.sleep(60 * 5)
'''


print("timeout after change:" + os.environ['TIMEOUT'])


print("This is what I have: \n" + str(os.environ.items()))


print('finished')
