import numpy
import pylab

# https://stackoverflow.com/questions/3765056/combine-picture-and-plot-with-python-matplotlib

fig = pylab.figure()
axplot = fig.add_axes([0.07,0.25,0.90,0.70])
axplot.plot(numpy.random.randn(100))
numicons = 8
for k in range(numicons):
    axicon = fig.add_axes([0.07+0.11*k,0.05,0.1,0.1])
    axicon.imshow(numpy.random.rand(4,4),interpolation='nearest')
    axicon.set_xticks([])
    axicon.set_yticks([])
fig.show()
fig.savefig('iconsbelow.png')
