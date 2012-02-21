from Sbox1DPA import *
import sys, sqlite3

if len(sys.argv) < 5:
    print 'Usage: <keys> <num_traces> <ptext_file> <traces_file>'
    exit()

key = int(sys.argv[1], 16)
numTraces = int(sys.argv[2])
ptextFile = sys.argv[3]
tracesFile = sys.argv[4]

dpa = Sbox1DPA(key, numTraces)

print 'reading files..'
f = open(ptextFile, 'r')

for j, line in enumerate(f):
    if j == numTraces:
        print 'done with simulations...'
	break
    if j%100 == 0 and j!=0:  print 'Generating Simulation for '+str(j)+'th plain-text...'
    ptext = int(line, 2)
    dpa.generatePowerSimulationModel(ptext)

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
