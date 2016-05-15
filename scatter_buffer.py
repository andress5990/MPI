"""
Collective communications example showing how to scatter buffers
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 4 python scatter_buffer.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = None
if rank == 0:
    sendbuf = np.arange(size*3)
    print 'Data to be scatter from root node: {data}'.format(data=sendbuf)

recvbuf = np.empty(3, dtype='int64')
comm.Scatter(sendbuf, recvbuf, root=0)

print "I am node {id} and got scatter data: {data}".format(id=rank, data=recvbuf)

MPI.Finalize()
