"""
Collective communications example showing how to gather buffers
To execute this run: mpirun -np 3 python gather_buffer.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = np.random.random_integers(1, 10, 5)
print "I am node {id} and this is my data: {data}".format(id=rank, data=data)

recvbuf = None
if rank == 0:
    recvbuf = np.empty([size, 5], dtype='int64')
comm.Gather(data, recvbuf, root=0)
if rank == 0:
    print "\nGather data in root node: {data}. Dimensions: {dim}".format(data=recvbuf, dim=recvbuf.shape)
