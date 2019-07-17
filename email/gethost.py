
# see stackoverflow/4760215
import subprocess

p = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out1, err1 = p.communicate()
print 'out:', out1
print 'err:', err1
