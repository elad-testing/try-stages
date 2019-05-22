import time
import sys, os
'''
for _ in range(9):
  print('wait for something')
  time.sleep(60 * 5)
'''
print('my sha is: %s' % os.environ['SHA'])
print('my sha is: %s' % os.environ['$TRAVIS_PULL_REQUEST_SHA'])
print('finished')
