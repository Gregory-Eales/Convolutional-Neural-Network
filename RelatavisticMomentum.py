import numpy as np


def gamma(v):
	c = 299792458 #m/s
	return 1/np.sqrt(1 - np.square(v)/np.square(c))


def velocity_calculator(m1, m2, v1):
	c = 299792458 #m/s
	gamma1 = gamma(v1)
	x = gamma1*m1*v1/m2
	v2 = np.sqrt(np.square(x)/(1+np.square(x/c)))
	return v2

m1 = 1
m2 = 100000000
v1 = 299792458.000*(0.99999999999999)

v2 = velocity_calculator(m1, m2, v1)
print((v2/299792458) * 100, "%")

