from Sbox1DPA import *
import sys, sqlite3
import matplotlib.pyplot as plt

if len(sys.argv) < 5:
    print 'Usage: <keys> <num_traces> <ptext_file> <traces_file>'
    exit()

key = int(sys.argv[1], 16)
numTraces = int(sys.argv[2])
ptextFile = sys.argv[3]
tracesFile = sys.argv[4]

ptexts = []

print 'reading files..'
f = open(ptextFile, 'r')

for j, line in enumerate(f):
    if j == numTraces:
	break
    ptexts.append(int(line, 2))

dpa = Sbox1DPA(key, numTraces, ptexts)

for key in xrange(64):
    dpa.generatePowerSimulationModel(key)

f1 = open(tracesFile, 'r')
 
print 'finding peak values...'
peaks = dpa.findPeaks(f1)
print 'attacking...'
correlations = dpa.attack(peaks)

results = dpa.findKey(correlations)

for item in results:
    print '('+hex(item[0])+', '+str(item[1])+')'

f.close()
f1.close()
print 'finished.'
