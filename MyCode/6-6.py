import time
import random
import re

bases = ['a', 'c', 'g', 't']
sequenceList = []
for n in range(0,250000000):
    sequenceList.append(random.choice(bases))
chromosome = ''.join(sequenceList)
searchPattern = 'tat.at'
nsearch = 100000
t1 = time.time()
for n in range(0,nsearch):
    result = re.finditer(searchPattern,chromosome)
t2 = time.time()
print('Average search time was', (t2-t1)/float(nsearch), 'seconds')

nmatches = 0
for match in result:
    nmatches += 1
print('Number of search hit = ', nmatches)
