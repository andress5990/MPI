"""
Collective communications example showing how to send buffers using Bcast
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 4 python broadcast_buffer.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.arange(10, dtype='int64')
else:
    data = np.empty(10, dtype='int64')

comm.Bcast(data, root=0)

print "I am node {id} and I got this data: {data}".format(id=rank, data=data)
