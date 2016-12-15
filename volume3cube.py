from numpy import linspace
import matplotlib.pyplot as plt

l = linspace(1, 3, 3)

v = l*l*l
print v
plt.plot(l, v)
plt.xlabel(u'l')
plt.ylabel(u'v')
plt.show()


