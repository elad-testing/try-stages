import time
import sys, os
'''
for _ in range(9):
  print('wait for something')
  time.sleep(60 * 5)
'''

print("timeout:" + os.environ['TIMEOUT'])

os.putenv("TIMEOUT", "42")

print("timeout after change:" + os.environ['TIMEOUT'])


print("This is what I have: \n" + str(os.environ.items()))


print('my sha is: %s' % os.environ['SHA'])
print('my pr is: %s' % os.environ['$TRAVIS_PULL_REQUEST_SHA'])
print('finished')
