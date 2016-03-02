import numpy as np

def s_curve(r, b, s):
    return 1 - (1 - s**r)**b
s = np.arange(.1, 1, .1)
print "{:>15} {:>15} {:>15} {:>15}".format("s", "r=3 and b=10", "r=6 and b=20", "r=5 and b=50")
for i,x,y,z in np.array([s, s_curve(3, 10, s), s_curve(6,20, s), s_curve(5, 20, s)]).T:
    print "{:15.1f} {:15.4f} {:15.4f} {:15.4f}".format(i,x,y,z)

def findthreshold(r, b):
    for i in np.arange(.1, .9, .0001):
        if np.abs(s_curve(r, b, i) - 0.5) <= .001:
            return i

def thresholdestimate(r, b):
    return (1/float(b))**(1/float(r))

r = 3
b = 10
print "r={}, b={}, threshold={:4f}, estimate={:4f}".format(r, b, findthreshold(r, b), thresholdestimate(r,b))
r = 6
b = 20
print "r={}, b={}, threshold={:4f}, estimate={:4f}".format(r, b, findthreshold(r, b), thresholdestimate(r,b))
r = 5
b = 50
print "r={}, b={}, threshold={:4f}, estimate={:4f}".format(r, b, findthreshold(r, b), thresholdestimate(r,b))
