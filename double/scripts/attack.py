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
    ptext = line.split()
    ptext1 = int(ptext[0],2)
    ptext2 = int(ptext[1],2)
    ptexts.append((ptext1, ptext2))

dpa = Sbox1DPA(key, numTraces, ptexts, 4096)

for key in xrange(4096):
    key1 = (key & 0xFC0) >> 6
    key2 = (key & 0x3F)
    dpa.generatePowerSimulationModel2(key1, key2)    

f1 = open(tracesFile, 'r')
 
print 'finding peak values...'
peaks = dpa.findPeaks(f1)
print 'attacking...'
correlations = dpa.attack(peaks)

results = dpa.findKey(correlations)

for index in xrange(len(results)):
    if hex(results[index][0]) == '0x1c4':
        print index, results[index]

for item in results[:40]:
    print '('+hex(item[0])+', '+str(item[1])+')'

f.close()
f1.close()
print 'finished.'
