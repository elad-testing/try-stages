import time
import sys, os
'''
for _ in range(9):
  print('wait for something')
  time.sleep(60 * 5)
'''

if os.path.exists('/home/travis/build/elad-testing/done.txt'):
  print('\n\nANOTHER ONE DID IT!\n\n')
else:
  with open('/home/travis/build/elad-testing/done.txt', 'w') as f:
    f.write('done')
    print('\n\nIwrote\n\n')



for key, val in os.environ.items():
  print(key + ": " + val)


print('finished')
