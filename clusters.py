# https://stackoverflow.com/questions/8940049/how-would-you-group-cluster-these-three-areas-in-arrays-in-python

from math import sqrt

def stat(lst):
    """Calculate mean and std deviation from the input list."""
    n = float(len(lst))
    mean = sum(lst) / n
    stdev = sqrt((sum(x*x for x in lst) / n) - (mean * mean))
    return mean, stdev

def parse(lst, n):
    cluster = []
    for i in lst:
        if len(cluster) <= 1:
            cluster.append(i)
            continue

        mean,stdev = stat(cluster)
        if abs(mean - i) > n * stdev:
            yield cluster
            cluster[:] = []

        cluster.append(i)
    yield cluster           # yield the last cluster
